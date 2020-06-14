# Wanderer
TravelScrum Hackathon Project Wanderer

## Install
```pip install -r requirements.txt```

## Run 
```cd python/location_recommendation && python recommend.py```

This will train the model using the sample file in `data/london_10k.csv` and run the python flask server.

### Motivation and sample data
https://www.kaggle.com/amiralisa/context-aware-recommender/comments


### Client API request
Request files: 
```
#user1.json
{
  "_userId": "41087279@N00",
  "email": "user1@gmail.com"
}

#user2.json
{
  "_userId": "7344912@N05",
  "email": "user2@gmail.com"
}
```

Make a Request
```
$ cd client
$ curl -H "Content-Type: application/json" --data @user1.json localhost:5000/api
{
  "1":{
    "location_id":766277,
    "lat":51.5010986328,
    "lon":-0.1703319997,
    "pred":3.2272727273,
    "covidSafetyRating":3
  },
  "2":{
    "location_id":811547,
    "lat":51.492931366,
    "lon":-0.1475320011,
    "pred":3.2272727273,
    "covidSafetyRating":2
  },
  "0":{
    "location_id":325510,
    "lat":51.5133018494,
    "lon":-0.0857840031,
    "pred":2.9193942176,
    "covidSafetyRating":2
  }

$ curl -H "Content-Type: application/json" --data @user2.json localhost:5000/api
{
  "0":{
    "location_id":893200,
    "lat":51.5032997131,
    "lon":-0.1513399929,
    "pred":1.5454545455,
    "covidSafetyRating":2
  },
  "1":{
    "location_id":811547,
    "lat":51.492931366,
    "lon":-0.1475320011,
    "pred":1.5454545455,
    "covidSafetyRating":3
  },
  "2":{
    "location_id":787533,
    "lat":51.4561386108,
    "lon":-0.3416489959,
    "pred":1.5454545455,
    "covidSafetyRating":3
  }
}
```
