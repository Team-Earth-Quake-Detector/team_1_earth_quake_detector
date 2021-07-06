from datetime import datetime

import geopy
import geopy.distance
import requests
import geocoder
from geopy.geocoders import Nominatim


current_location = [(geocoder.ip('me').latlng[0]), (geocoder.ip('me').latlng[1])]


def filter_radius_test(location=None, radius: int = 250):
    if location is None:
        location = current_location

    """ Get data from API"""
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    response = requests.get(url)
    earthquakes = response.json()['features']

    earthquake_data = []
    for element in earthquakes:
        time = str(datetime.fromtimestamp(element["properties"]["time"] / 1000))
        dict = {"id": element["id"],
                "longitude": element["geometry"]["coordinates"][0],
                "latitude": element["geometry"]["coordinates"][1],
                "time": time,
                "magnitude": element["properties"]["mag"],
                "distance": ""
                }
        earthquake_data.append(dict)

    earthquake_data_clean = []
    for earthquake in earthquake_data:
        starting_point = location
        earthquake_location = (earthquake["latitude"], earthquake["longitude"])
        distance = geopy.distance.distance(starting_point, earthquake_location).km
        earthquake["distance"] = distance
        if distance <= radius:
            earthquake_data_clean.append(earthquake)

    print(earthquake_data_clean)


def relocate(location=None, coordinates=None, radius: int = 250):
    if location is not None:
        geolocator = Nominatim(user_agent="team_1_earthquake_detector")
        location_latitude = geolocator.geocode(location).latitude
        location_longitude = geolocator.geocode(location).longitude
        location_coordinates = (location_latitude, location_longitude)
        filter_radius_test(location_coordinates, radius)

    if coordinates is not None:
        filter_radius_test(coordinates, radius)


lat = input("Enter a latitude value between -90 and 90")
long = input("Enter a longitude value between -180 and 180")
new_coordinates = (lat, long)
new_location = input("Enter a location")
radius = int(input("Enter a radius in km"))

relocate(coordinates=new_coordinates, radius=radius)
relocate(location=new_location, radius=radius)
# relocate(coordinates=(34.052234, -118.243685), radius=250)
# relocate(location="Los Angeles", radius=250)
