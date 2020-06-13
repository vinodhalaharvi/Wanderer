import os
import warnings
from random import randint

import numpy as np
import pandas as pd
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
from sklearn.cluster import DBSCAN
from sklearn.decomposition import NMF
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale

pd.set_option('display.max_columns', 20)
np.set_printoptions(suppress=True)

main_path = '../..'

warnings.filterwarnings('ignore')

print(os.listdir(main_path))

data_file_path = f'{main_path}/data/london_20k.csv'

data_type = {
    'photo_id': 'object',
    'owner': 'object',
    'faves': 'float16',
    'lat': 'float32',
    'lon': 'float32',
    'taken': 'datetime64'
}

raw = pd.read_csv(data_file_path,
                  engine='python',
                  sep=',',
                  encoding='utf-8',
                  dtype=data_type,
                  decimal=',')
data_dim = raw.shape

print(f'Dataframe dimentions: {data_dim}', f'\n{"-" * 50}\nData Types:\n{raw.dtypes}')
raw.head()

data = raw[['photo_id', 'owner', 'lat', 'lon', 'taken']]

missing_nan = data.isna().sum()

print('TOTAL MISSINGS:', missing_nan, sep='\n')

data = data.dropna(subset=['lat', 'lon'])
new_size = len(data.index)
print(f'{"-" * 50}\n{data_dim[0] - new_size} empty rows are removed.')


def HDBSCAN(df, epsilon, minPts, x='lat', y='lon'):
    # Find most centered sample in a cluster
    def getCenterMostPts(cluster):
        centroid = (MultiPoint(cluster.values).centroid.x, MultiPoint(cluster.values).centroid.y)
        centermost_point = min(cluster.values, key=lambda point: great_circle(point, centroid).m)
        return tuple(centermost_point)

    m_per_rad = 6371.0088 * 1000
    eps_rad = epsilon / m_per_rad
    photo_coords = df.loc[:, {x, y}]
    photo_coords = photo_coords[['lat', 'lon']]
    db = DBSCAN(eps=eps_rad, min_samples=minPts, algorithm='ball_tree', metric='haversine').fit(
        np.radians(photo_coords))
    cluster_labels = db.labels_ + 1
    num_clusters = len(set(cluster_labels))

    # Put clusters and their subset of coords in an array
    clusters = pd.Series([photo_coords[cluster_labels == n] for n in range(num_clusters)])

    # Find centroid of each cluster
    centroids = clusters.map(getCenterMostPts)

    # Pull rows from original data frame where row numbers match the clustered data
    rows = clusters.apply(lambda c: c.index.values)
    clustered_df = rows.apply(lambda row_num: df.loc[row_num])

    # Append cluster numbers and centroid coords to each clustered dataframe
    lats, lons = zip(*centroids)
    new_df = []
    for i, v in clustered_df.iteritems():
        v.loc[:, 'cluster_num'] = i
        v.loc[:, 'cent_lat'] = lats[i]
        v.loc[:, 'cent_lon'] = lons[i]
        new_df.append(v)
    new_df = pd.concat(new_df)

    return new_df


cdata = HDBSCAN(data, epsilon=120, minPts=10)
print(f'Number of clusters: {len(cdata.cluster_num.unique())}')

clean_data = cdata[cdata.cluster_num != 0]


def mostFreqStr(array):
    array = [i for i in array if str(i) != 'nan']
    if len(array) != 0:
        counts = np.unique(array, return_counts=True)[1]
        max_index = np.argmax(counts)
        freq_bin = array[max_index]
        return freq_bin
    else:
        return np.nan


def medTimestamps(array):
    if len(array) == 1:
        return array[0]
    else:
        if len(array) % 2 == 0:
            delta = array[int(len(array) / 2)] - array[int(len(array) / 2 - 1)]
            median = pd.Timestamp(array[int(len(array) / 2 - 1)] + delta)
        else:
            time = pd.Timestamp(array[int(len(array) / 2)]).time()
            ser = pd.Series(array)
            date = pd.Timestamp.fromordinal(
                int(ser.apply(lambda x: pd.to_datetime(x).toordinal()).median(skipna=True))).date()
            median = pd.Timestamp.combine(date, time)
        return median


POI = pd.DataFrame(columns=['location_id', 'user_id', 'lat', 'lon', 'visit_time'])
threshold = np.timedelta64(6, 'h')

for i, g in clean_data.groupby(by='cluster_num'):
    l = {}
    l['location_id'] = randint(100000, 999999)
    l['lat'] = g.cent_lat.unique()[0]
    l['lon'] = g.cent_lon.unique()[0]

    for u in g.owner.unique():
        l['user_id'] = u
        taken = g.loc[g.owner == u, 'taken'].sort_values()
        t_indices = taken.keys()
        t_values = taken.values
        visit_times = []

        if len(t_values) == 1:
            l['visit_time'] = pd.Timestamp(t_values[0])
            POI = POI.append(l, ignore_index=True)

        else:
            for t in range(1, len(t_values)):
                if t_values[t] - t_values[t - 1] < threshold:
                    visit_times.append(t_values[t - 1])
                else:
                    visit_times.append(t_values[t - 1])
                    l['visit_time'] = medTimestamps(visit_times)
                    POI = POI.append(l, ignore_index=True)
                    visit_times = []

prefiltered_file_path = f'{main_path}/data/prefiltered.csv'
POI.to_csv(prefiltered_file_path)

data_type = {
    'faves': 'float16',
    'lat': 'float32',
    'lon': 'float32',
    'visit_time': 'datetime64'
}

LPD = pd.read_csv(prefiltered_file_path, engine='python', sep=',', encoding='utf-8', dtype=data_type, decimal=',')
#  mockedup data with random values. In real life you should get this using a weather service api
LPD['weather'] = np.random.randint(1, 10, LPD.shape[0])
LPD['season'] = np.random.randint(1, 4, LPD.shape[0])
LPD['daytime'] = np.random.randint(1, 3, LPD.shape[0])
LPD['rating'] = np.random.randint(1, 5, LPD.shape[0])
LPD = LPD.set_index(keys=['user_id', 'location_id'])

visit_limit = LPD.groupby(level=[0, 1])['visit_time'].count()
visit_limit = visit_limit[visit_limit > 3]
mask = LPD.index.isin(visit_limit.index) == True
X = LPD[mask]
y = X.index.get_level_values(0)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=70)

train_rating = X_train.groupby(['location_id', 'user_id'])['visit_time'].count().reset_index(name='rating')
train_rating.head(10)


def normalize(df):
    # Normalize number of visit into a range of 1 to 5
    df['rating'] = minmax_scale(df.rating, feature_range=[1, 5])
    return df


r_df = normalize(train_rating)

r_df = train_rating.pivot_table(
    index='user_id',
    columns='location_id',
    values='rating',
    fill_value=0
)


def calSparcity(m):
    m = m.fillna(0)
    non_zeros = np.count_nonzero(m) / np.prod(m.shape) * 100
    sparcity = 100 - non_zeros
    print(f'The sparcity percentage of matrix is %{round(sparcity, 2)}')


calSparcity(r_df)


def improved_asym_cosine(m, mf=False, **kwarg):
    # Cosine similarity matrix distance
    cosine = cosine_similarity(m)

    # Asymmetric coefficient
    def asymCo(X, Y):
        co_rated_item = np.intersect1d(np.nonzero(X), np.nonzero(Y)).size
        coeff = co_rated_item / np.count_nonzero(X)
        return coeff

    asym_ind = pairwise_distances(m, metric=asymCo)

    # Sorensen similarity matrix distance
    sorensen = 1 - pairwise_distances(np.array(m, dtype=bool), metric='dice')

    # User influence coefficient
    def usrInfCo(m):
        binary = m.transform(lambda x: x >= x[x != 0].mean(), axis=1) * 1
        res = pairwise_distances(binary, metric=lambda x, y: (x * y).sum() / y.sum() if y.sum() != 0 else 0)
        return res

    usr_inf_ind = usrInfCo(m)

    similarity_matrix = np.multiply(np.multiply(cosine, asym_ind), np.multiply(sorensen, usr_inf_ind))

    usim = pd.DataFrame(similarity_matrix, m.index, m.index)

    # Check if matrix factorization was True
    if mf:
        # Binary similarity matrix
        binary = np.invert(usim.values.astype(bool)) * 1
        model = NMF(**kwarg)
        W = model.fit_transform(usim)
        H = model.components_
        factorized_usim = np.dot(W, H) * binary + usim
        usim = pd.DataFrame(factorized_usim, m.index, m.index)

    return usim


s_df = improved_asym_cosine(r_df)
calSparcity(s_df)

contexts = X_train.filter(['season', 'daytime', 'weather']).apply(lambda x: (x.season, x.daytime, x.weather),
                                                                  axis=1).reset_index(name='context')
IF = contexts.groupby(['location_id', 'context'])['context'].count() / contexts.groupby(['context'])['context'].count()
IDF = np.log10(
    contexts.groupby(['location_id', 'user_id'])['user_id'].count().sum() / contexts.groupby(['location_id'])[
        'user_id'].count())
contexts_weight = (IF * IDF).to_frame().rename(columns={0: 'weight'})

lc_df = contexts_weight.pivot_table(
    index='context',
    columns='location_id',
    values='weight',
    fill_value=0
)

calSparcity(lc_df)

cs_df = pd.DataFrame(cosine_similarity(lc_df), index=lc_df.index, columns=lc_df.index)
calSparcity(cs_df)


def CF(user_id, location_id, s_matrix):
    r = np.array(r_df)
    s = np.array(s_matrix)
    users = r_df.index
    locations = r_df.columns
    l = np.where(locations == location_id)[0]
    u_idx = np.where(users == user_id)[0]

    # Means of all users
    means = np.array([np.mean(row[row != 0]) for row in r])
    wmean_rating = 0
    # Check if l is in r_rating
    if location_id in r_df:
        # Find similar users rated the location that target user hasn't visited
        idx = np.nonzero(r[:, l])[0]
        sim_scores = s[u_idx, idx].flatten()
        sim_users = zip(idx, sim_scores)

        # Check if there is any similar user to target user
        if idx.any():
            sim_ratings = r[idx, l]
            sim_means = means[idx]
            numerator = (sim_scores * (sim_ratings - sim_means)).sum()
            denominator = np.absolute(sim_scores).sum()
            weight = (numerator / denominator) if denominator != 0 else 0
            wmean = means[u_idx] + weight
            wmean_rating = wmean[0]

    else:
        wmean_rating = 0

    return wmean_rating


def CaCF_Post(user_id, location_id, s_matrix, c_current, delta):
    # Calculate cf
    initial_pred = CF(user_id, location_id, s_matrix)

    if location_id in r_df:
        r = np.array(r_df)
        users = r_df.index
        locations = r_df.columns
        l = np.where(locations == location_id)[0]
        c_profile = contexts
        all_cnx = contexts.context.unique().tolist()
        c = np.array(c_profile)
        u_idx = np.where(users == user_id)[0]
        c_current = tuple(c_current)

        # Get contexts of similar users visited the location
        l_cnx = np.array(c_profile.loc[c_profile.location_id == location_id, ['user_id', 'context']])

        if c_current in all_cnx:
            # Find similarity of the current context to location contexts
            cnx_scores = np.array([[uid, cs_df[c_current][cx]] for uid, cx in l_cnx])

            # Filter users whose similarity bigger than delta
            filtered_scores = cnx_scores[cnx_scores[:, 1].astype(float) > delta]

            # Location popularity based on current context
            visit_prob = len(filtered_scores) / len(cnx_scores)

        else:
            visit_prob = 1

        return initial_pred * visit_prob

    else:
        return initial_pred


test_rating = X_test.groupby(['location_id', 'user_id'])['visit_time'].count().reset_index(name='rating')
test_rating = normalize(test_rating)
r_df_test = test_rating.pivot_table(index='user_id', columns='location_id', values='rating', fill_value=0)


def EACOS_CaCF_Post(user_id, location_id, c_current, delta):
    res = CaCF_Post(user_id, location_id, s_df, c_current, delta)
    return res


def predict(target_user, model, option=None):
    true = r_df_test.loc[target_user]

    # Check if model is context-aware 
    if option:
        pred_val = []
        for l in true.index:
            delta = option.get('delta')
            c_current = tuple(X_test.xs(target_user)[['season', 'daytime', 'weather']].head(1).values[0])
            r = model(user_id=target_user, location_id=l, c_current=c_current, delta=delta)
            pred_val.append(r)
    else:
        pred_val = [model(user_id=target_user, location_id=l) for l in true.index]

    pred = pd.Series(pred_val, index=true.index)

    return pred


user = '41087279@N00'
options = {
    'delta': .3
}


def item_relevancy(col):
    relevant = 1
    r_color = 'background-color: lime'
    nr_color = 'background-color: red'
    res = []
    for v in col:
        if v > relevant:
            res.append(r_color)
        elif (v > 0) & (v <= relevant):
            res.append(nr_color)
        else:
            res.append('')
    return res


true = r_df_test.loc[user]
pred = predict(user, EACOS_CaCF_Post, option=options)

with pd.option_context("display.max_rows", None):
    prediction = pd.DataFrame({'true': true, 'pred': pred})

top_10 = prediction.nlargest(10, 'pred')
top_10.style.apply(lambda col: item_relevancy(col))

