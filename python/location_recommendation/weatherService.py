""" 
    Weather: (1=clear-day, 2=clear-night, 3=rain, 4=snow,
              5=sleet, 6=wind, 7=fog, 8=cloudy, 9=partly-cloudy-day, 10=partly-cloudy-night)
    Season: (1=spring, 2=summer, 3=autumn, 4=winter)
    Daytime: (1=day, 2=night, 3=midnight)
    weatherService = "Some API call"
    weather = weatherService.getWeather(lat, lon, time)
    season = weatherService.getSeason(lat, lon, time)
    daytime = weatherService.getDaytime(lat, lon, time)
    return weather, season, daytime

"""

import requests
from datetime import datetime, timezone, timedelta


class weatherService:
    def __init__(self):
        self.__baseurl = "https://community-open-weather-map.p.rapidapi.com"
        self.__headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "ee3f817fbfmsh8f8ec88d2a5cd97p116caajsncf67afe46867"
        }

    def __queryWeather(self, lat: float, lon: float, dt: datetime = None):

        querystring = {
            "units": "metric",
            "lat": str(lat),
            "lon": str(lon)
        }

        if dt is None:
            url = self.__baseurl + "/weather"
        else:
            url = self.__baseurl + "/onecall/timemachine"
            querystring['dt'] = round(dt.replace(tzinfo=timezone.utc).timestamp())

        response = requests.request("GET", url,
                                    headers=self.__headers,
                                    params=querystring)
        if response:
            return response.json()
        else:
            print('Request returned an error for  ' + str(querystring))

    def __extractMainFromResponse(resp: dict):
        if resp:
            # weather conditions
            # https://openweathermap.org/weather-conditions
            try:
                print(resp['weather'][0]['main'])
            except KeyError:
                try:
                    print(resp['current']['weather'][0]['main'])
                except KeyError:
                    print(resp)

    def getWeather(self, lat: float, lon: float, dt: datetime = None):
        resp = self.__queryWeather(lat, lon, dt)
        if resp:
            # weather conditions
            # https://openweathermap.org/weather-conditions
            condition = ''
            try:
                condition = resp['weather'][0]['main']
            except KeyError:
                try:
                    condition = resp['current']['weather'][0]['main']
                except KeyError:
                    print(resp)
            if condition is not None:
                return condition.lower()

    def getDaytime(self, lat: float, lon: float, dt: datetime = None):
        url = "https://geo-services-by-mvpc-com.p.rapidapi.com/sun_positions"
        if dt is None:
            dt = datetime.today()

        querystring = {
            "date": dt.date().isoformat(),
            "location": str(lat) + ',' + str(lon)
        }

        headers = {
            'x-rapidapi-host': "geo-services-by-mvpc-com.p.rapidapi.com",
            'x-rapidapi-key': "ee3f817fbfmsh8f8ec88d2a5cd97p116caajsncf67afe46867"
        }

        response = requests.request("GET", url,
                                    headers=headers, params=querystring)

        if response:
            data = response.json()['data']
            sunrise = datetime.strptime(data['sunrise'],
                                        "%Y-%m-%dT%H:%M:%S%z")
            sunset = datetime.strptime(data['sunset'],
                                       "%Y-%m-%dT%H:%M:%S%z")
            if (dt.replace(tzinfo=sunrise.tzinfo) > sunrise
                    and dt.replace(tzinfo=sunrise.tzinfo) < sunset):
                return 'day'
            else:
                return 'night'


dt = datetime.utcnow()
aDay = timedelta(1)
dt = datetime.fromtimestamp(1592077233)
yesterday = dt - aDay
print(yesterday)
weather = weatherService()

print(weather.getWeather(40.4165000, -3.7025600))  # Madrid
print(weather.getWeather(41.390205, 2.154007, yesterday))  # Barcelona

print(weather.getDaytime(40.4165000, -3.7025600))  # Madrid
print(weather.getDaytime(41.390205, 2.154007, yesterday))  # Barcelona
