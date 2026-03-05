import requests
import json

URLS = "http://127.0.0.1:8000/core/create_data"

data = {"name": "alex pandey", "roll":69, "city":"lucknow"}

def create_data():
    json_data = json.dumps(data)
    r = requests.post(URLS, data = json_data)
    data = r.json()
    print(data)


create_data()
