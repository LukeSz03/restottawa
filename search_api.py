import requests
import os
import json

from dotenv import load_dotenv

load_dotenv()


def search(name):
    url = (
        "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
        + name
        + "&key="
        + os.environ.get("API_KEY")
    )

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    info = response.text
    print(info)


search("mexicanrestaurants")
