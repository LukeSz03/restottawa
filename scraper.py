import requests
import os

from dotenv import load_dotenv

load_dotenv()


def info_sort(results):
    # CLEAN INFORMATION
    print(results.text)
    # for item in results:
    #     item.text


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

    info_sort(response)
