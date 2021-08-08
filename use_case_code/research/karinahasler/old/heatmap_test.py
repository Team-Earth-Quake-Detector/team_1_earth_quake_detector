import folium
import requests
from datetime import datetime
import geopy.distance
from folium.plugins import HeatMap

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

heat_data = [[earthquake["latitude"], earthquake["longitude"]] for earthquake in earthquake_data_clean]

# Set up basic OpenStreetMap #integrated in map
map_osm = folium.Map(location=user_provided_location,
                     zoom_start=5,
                     tiles='OpenStreetMap',
                     control_scale=True)
folium.Marker(user_provided_location).add_to(map_osm)

HeatMap(heat_data).add_to(map_osm)
folium.LayerControl().add_to(map_osm)

map_osm.save("heatmap_test.html")
