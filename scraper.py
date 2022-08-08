from dataclasses import dataclass
from xml.dom.pulldom import SAX2DOM


import googlemaps
from dotenv import load_dotenv

load_dotenv()

gmaps = googlemaps.Client(key="API_KEY")


def search(restaurant):
    print("searching " + restaurant)
