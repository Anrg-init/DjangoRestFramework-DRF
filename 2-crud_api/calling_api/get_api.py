import requests
import json

URL = "http://127.0.0.1:8000/core/"


def get_data():
    r = requests.get(URL)
    data = r.json()
    print(data)

get_data()

