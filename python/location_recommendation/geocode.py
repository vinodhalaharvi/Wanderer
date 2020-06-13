from geopy.geocoders import Nominatim

if __name__ == '__main__':
    geoLocator = Nominatim(user_agent="travelX")
    address = "Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC"
    code = geoLocator.geocode(address)
    if code is not None:
        print(code.address)
        print(code.latitude, code.longitude)
        location = geoLocator.reverse(f"{code.latitude} {code.longitude}")
        print(location.latitude, location.longitude)
    else:
        print("No address found ")
