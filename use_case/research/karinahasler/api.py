import folium
import webbrowser
import branca.colormap as cm
import requests
from datetime import datetime
import geocoder
import geopy.distance

#integrated in data_collector
response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
earthquakes = response.json()['features']

#integrated in data_collector
earthquake_data = []
for element in earthquakes:
    time = str(datetime.fromtimestamp(element["properties"]["time"] / 1000))
    dict = {"id": element["id"],
            "longitude": element["geometry"]["coordinates"][0],
            "latitude": element["geometry"]["coordinates"][1],
            "time": time,
            "magnitude": element["properties"]["mag"]
            }
    earthquake_data.append(dict)

duesseldorf = (51.2277411, 6.7734556)
radius = 7500

earthquake_data_clean = []
for earthquake in earthquake_data:
    starting_point = duesseldorf
    location = (earthquake["latitude"], earthquake["longitude"])
    distance = geopy.distance.distance(starting_point, location).km
    if distance <= radius:
        earthquake_data_clean.append(earthquake)


# Set up basic OpenStreetMap #integrated in map
current_location = geocoder.ip('me')
map_osm = folium.Map(location=[(current_location.latlng[0]), (current_location.latlng[1])],
                     zoom_start=5,
                     tiles='StamenTerrain',
                     control_scale=True)

# Visualize earthquake data
colormap = cm.LinearColormap(colors=['orange','red'], index=[0,10],vmin=0,vmax=10)

for earthquake in earthquake_data_clean:
    location = (earthquake["latitude"], earthquake["longitude"])
    tooltip_text = f"Time: {earthquake['time']}\n Magnitude: {earthquake['magnitude']}"
    radius = earthquake['magnitude'] * 50000
    folium.Circle(
        location=location,
        tooltip=tooltip_text,
        radius=radius,
        fill=True,
        color=colormap(earthquake['magnitude']),
        weight=1,
        fill_opacity=0.5
    ).add_to(map_osm)

# Add tectonic plates
url = 'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json'

folium.GeoJson(
    url,
    name='Tectonic plates'
).add_to(map_osm)

# Add layer control
folium.LayerControl().add_to(map_osm)

map_osm.save("map_osm.html")

#file_path = r"/templates/earthquake_map.html"
#map_osm.save(file_path) # Save as html file
#webbrowser.open(file_path) # Default browser open
