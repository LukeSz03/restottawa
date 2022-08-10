from lib2to3.pytree import convert
import requests
import os
import json

from dotenv import load_dotenv

load_dotenv()


def clean_results(response):
    # assign json results to variable
    api_json = response.text

    # convert json object to Python dictionary
    api_dict = json.loads(api_json)

    # store value of "results" key i.e. a list of the restaurants, inside a variable
    restaurants = api_dict["results"]

    # delete all keys in every element except the key "name"
    for i in restaurants:
        for k in list(i):
            if k != "name" and k != "rating":
                del i[k]
        print(i)


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

    clean_results(response)


search("mexicanrestaurants")
