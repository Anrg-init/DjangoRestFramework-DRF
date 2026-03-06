import requests
import json

URL = "http://127.0.0.1:8000/core/createdata/"

p_data = {"name":"sahil", "roll":1001, "city":"lundpuru"}

headers = {"Content-Type": "application/json"}

def get_data():
    json_data = json.dumps(p_data)
    r = requests.post(URL, json_data, headers=headers)
    doto = r.json()
    print(doto)

get_data()