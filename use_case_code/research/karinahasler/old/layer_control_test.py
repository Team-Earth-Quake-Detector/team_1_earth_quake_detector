import folium
import requests
from datetime import datetime
import geopy.distance
from folium.plugins import HeatMap
import branca.colormap as cm

user_provided_location = [34.052235, -118.243683]
user_provided_radius = 1000

# Retrieve data from USGS
response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
earthquakes = response.json()['features']

# Prepare data
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

# Set up basic OpenStreetMap
map_osm = folium.Map(location=user_provided_location,
                     zoom_start=5,
                     tiles='OpenStreetMap',
                     control_scale=True)
folium.Marker(user_provided_location).add_to(map_osm)

# Create heatmap
heat_data = [[earthquake["latitude"], earthquake["longitude"]] for earthquake in earthquake_data_clean]
HeatMap(heat_data, name="Heatmap", show=False).add_to(map_osm)

# Create marker for each earthquake
colormap = cm.LinearColormap(colors=['orange', 'red'], index=[0, 10], vmin=0, vmax=10)

circle_markers = folium.FeatureGroup(name='Circle markers')
map_osm.add_child(circle_markers)

for earthquake in earthquake_data_clean:
    earthquake_location = (earthquake["latitude"], earthquake["longitude"])
    tooltip_text = f"Time: {earthquake['time']}\n Magnitude: {earthquake['magnitude']}"
    radius = earthquake['magnitude'] * 50000
    folium.Circle(
        location=earthquake_location,
        tooltip=tooltip_text,
        radius=radius,
        fill=True,
        color=colormap(earthquake['magnitude']),
        weight=1,
        fill_opacity=0.5
    ).add_to(circle_markers)

connective_lines = folium.FeatureGroup(name='Connective lines')
map_osm.add_child(connective_lines)

for earthquake in earthquake_data_clean:
    earthquake_location = (earthquake["latitude"], earthquake["longitude"])
    lines = []
    lines.append(user_provided_location)
    lines.append(earthquake_location)
    folium.PolyLine(
        lines,
        color="grey",
        weight=1.5,
        dash_array=10,
        popup=f"{round(earthquake['distance'], 2)} km"
    ).add_to(connective_lines)

# Add tectonic plates
url = 'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json'

folium.GeoJson(url, name='Tectonic plates').add_to(map_osm)

# Add layer control
folium.LayerControl().add_to(map_osm)

# Save map
map_osm.save("layer_control_test.html")
