def getWeather(lat, lon, time):
    # Weather: (1
    #           =clear-day, 2=clear-night, 3=rain, 4=snow,
    #           5=sleet, 6=wind, 7=fog, 8=cloudy, 9=partly-cloudy-day, 10=partly-cloudy-night)
    # Season: (1=spring, 2=summer, 3=autumn, 4=winter)
    # Daytime: (1=day, 2=night, 3=midnight)
    weatherService = "Some API call"
    weather = weatherService.getWeather(lat, lon, time)
    season = weatherService.getSeason(lat, lon, time)
    daytime = weatherService.getDaytime(lat, lon, time)
    return weather, season, daytime
