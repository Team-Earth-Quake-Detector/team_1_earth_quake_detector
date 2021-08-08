import folium
import webbrowser
import branca.colormap as cm
import requests
from datetime import datetime
import geocoder
import geopy.distance
from folium import plugins
from folium.plugins import HeatMap
import numpy as np
import pandas as pd

user_provided_location = [34.052235, -118.243683]
user_provided_radius = 1000

#integrated in data_collector
response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
earthquakes = response.json()['features']

#integrated in data_collector
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
    starting_point = user_provided_location
    earthquake_location = (earthquake["latitude"], earthquake["longitude"])
    distance = geopy.distance.distance(user_provided_location, earthquake_location).km
    earthquake["distance"] = distance
    if distance <= user_provided_radius:
        earthquake_data_clean.append(earthquake)

values = [[earthquake["latitude"], earthquake["longitude"]] for earthquake in earthquake_data_clean]
keys = [[earthquake["time"]] for earthquake in earthquake_data_clean]
heat_data = {str(keys[i]): values[i] for i in range(len(keys))}

test_values = [[33.9333333, -117.9738333], [38.5745, -119.4725], [38.5706, -119.4573]]
test_keys = [1, 2, 3]
test_data = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
#print(test_data)

# Set up basic OpenStreetMap #integrated in map
map_osm = folium.Map(location=user_provided_location,
                     zoom_start=5,
                     tiles='OpenStreetMap',
                     control_scale=True)
folium.Marker(user_provided_location).add_to(map_osm)

heatmap_with_time = plugins.HeatMapWithTime(data=test_values, auto_play=True, max_opacity=0.8)
heatmap_with_time.add_to(map_osm)

map_osm.save("heatmap_with_time_test.html")

