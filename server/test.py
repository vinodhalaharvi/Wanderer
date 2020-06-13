

import json
import requests

home = requests.get('http://127.0.0.1:5000/').text

print(home)

inp = {
  "email": "foo.bar@gmail.com",
  "location": {
    "lat": 10.1,
    "lon": 11.11
  }
}
# inp = json.dumps(inp)
header = {"Content-Type": "application/json"}

get_url = 'http://127.0.0.1:5000/recommend/' \
          '?email=sree@wanderer.com&location=10.2,22.34'
recommend = requests.get(get_url, headers=header)
print(recommend.text)

# recommend = requests.post('http://127.0.0.1:5000/recommend/', json=inp,
#                           headers=header)
# print(recommend.text)
