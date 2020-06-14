diff --git a/python/location_recommendation/recommendation.py b/python/location_recommendation/recommendation.py
index 75f334c..af4f492 100644
--- a/python/location_recommendation/recommendation.py
+++ b/python/location_recommendation/recommendation.py
@@ -43,7 +43,6 @@ data_dim = raw.shape
 
 print(f'Dataframe dimentions: {data_dim}', f'\n{"-" * 50}\nData Types:\n{raw.dtypes}')
 raw.head()
-
 data = raw[['photo_id', 'owner', 'lat', 'lon', 'taken']]
 
 missing_nan = data.isna().sum()
@@ -94,23 +93,11 @@ def HDBSCAN(df, epsilon, minPts, x='lat', y='lon'):
     return new_df
 
 
-cdata = HDBSCAN(data, epsilon=120, minPts=10)
+cdata = HDBSCAN(data, epsilon=280, minPts=70)
 print(f'Number of clusters: {len(cdata.cluster_num.unique())}')
-
 clean_data = cdata[cdata.cluster_num != 0]
 
 
-def mostFreqStr(array):
-    array = [i for i in array if str(i) != 'nan']
-    if len(array) != 0:
-        counts = np.unique(array, return_counts=True)[1]
-        max_index = np.argmax(counts)
-        freq_bin = array[max_index]
-        return freq_bin
-    else:
-        return np.nan
-
-
 def medTimestamps(array):
     if len(array) == 1:
         return array[0]
@@ -172,7 +159,7 @@ LPD = pd.read_csv(prefiltered_file_path, engine='python', sep=',', encoding='utf
 LPD['weather'] = np.random.randint(1, 10, LPD.shape[0])
 LPD['season'] = np.random.randint(1, 4, LPD.shape[0])
 LPD['daytime'] = np.random.randint(1, 3, LPD.shape[0])
-LPD['rating'] = np.random.randint(1, 5, LPD.shape[0])
+# LPD['rating'] = np.random.randint(1, 5, LPD.shape[0])
 LPD = LPD.set_index(keys=['user_id', 'location_id'])
 
 visit_limit = LPD.groupby(level=[0, 1])['visit_time'].count()
@@ -405,4 +392,6 @@ with pd.option_context("display.max_rows", None):
 
 top_10 = prediction.nlargest(10, 'pred')
 top_10.style.apply(lambda col: item_relevancy(col))
-
+foo = top_10.reset_index()
+bar = foo.set_index('location_id').join(POI.set_index('location_id')).drop_duplicates(subset=["lat", "lon"])
+print("Done")
\ No newline at end of file
diff --git a/python/location_recommendation/server.py b/python/location_recommendation/server.py
index e69de29..7f73143 100644
--- a/python/location_recommendation/server.py
+++ b/python/location_recommendation/server.py
@@ -0,0 +1,11 @@
+def serverModelFile(model):
+   pass
+
+
+def loadModelFile():
+   pass
+
+
+if __name__ == '__main__':
+   model = loadModelFile()
+   serverModelFile(model)
diff --git a/python/location_recommendation/weatherService.py b/python/location_recommendation/weatherService.py
index e69de29..6245f78 100644
--- a/python/location_recommendation/weatherService.py
+++ b/python/location_recommendation/weatherService.py
@@ -0,0 +1,11 @@
+def getWeather(lat, lon, time):
+    # Weather: (1
+    #           =clear-day, 2=clear-night, 3=rain, 4=snow,
+    #           5=sleet, 6=wind, 7=fog, 8=cloudy, 9=partly-cloudy-day, 10=partly-cloudy-night)
+    # Season: (1=spring, 2=summer, 3=autumn, 4=winter)
+    # Daytime: (1=day, 2=night, 3=midnight)
+    weatherService = "Some API call"
+    weather = weatherService.getWeather(lat, lon, time)
+    season = weatherService.getSeason(lat, lon, time)
+    daytime = weatherService.getDaytime(lat, lon, time)
+    return weather, season, daytime
