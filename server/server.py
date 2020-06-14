from flask import Flask, request, jsonify
from geopy import Nominatim

app = Flask(__name__)
geoLocator = Nominatim(user_agent="travelX")

requestJson = """{
  "_userId": "41087279@N00"
  "email": "foo.bar@gmail.com",
  "location": {
    "lat": 10.1,
    "lon": 11.11
  }
}"""


def geocode(address):
    code = geoLocator.geocode(address)
    return code.latitude, code.longitude


def geocodeReverse(lat, lon):
    location = geoLocator.reverse(f'{lat} {lon}')
    return location.address


@app.route("/", methods=["GET"])
def get_homepage():
    return "<strong>TravelX App</strong>"


@app.route("/api", methods=["POST"])
def get_response():
    json = request.get_json()
    user, email, lat, lon = json["_userId"], json["email"], json["location"]["lat"], json["location"]["lon"]
    text = f'user: {user}; email: {email}; lat: {lat}; lon: {lon}; address: {geocodeReverse(lat, lon)}'
    res = {
        "request": text
    }
    return jsonify(res)


if __name__ == "__main__":
    app.debug = True  # debug
    print("Starting server on http://0.0.0.0:5000/")
    app.run(host="0.0.0.0")
