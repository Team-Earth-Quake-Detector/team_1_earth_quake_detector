import folium
import webbrowser
import branca.colormap as cm
import requests
from datetime import datetime
import geocoder
import geopy.distance

user_provided_location = [50.7338, 2.3024]
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
            "place": element["properties"]["place"],
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
    earthquake["distance"] = round(distance, 2)
    if distance <= user_provided_radius:
        earthquake_data_clean.append(earthquake)

# Set up basic OpenStreetMap #integrated in map
map_osm = folium.Map(location=user_provided_location,
                     zoom_start=5,
                     tiles='StamenTerrain',
                     control_scale=True)
folium.Marker(user_provided_location).add_to(map_osm)

# Visualize earthquake data
colormap = cm.LinearColormap(colors=['orange', 'red'], index=[0,10],vmin=0,vmax=10)

for earthquake in earthquake_data_clean:
    earthquake_location = (earthquake["latitude"], earthquake["longitude"])
    tooltip_text = f"Time: {earthquake['time']}\n Magnitude: {earthquake['magnitude']}"
    circle_radius = earthquake['magnitude'] * 50000
    folium.Circle(
        location=earthquake_location,
        tooltip=tooltip_text,
        radius=circle_radius,
        fill=True,
        color=colormap(earthquake['magnitude']),
        weight=1,
        fill_opacity=0.5
    ).add_to(map_osm)

    lines = []
    lines.append(user_provided_location)
    lines.append(earthquake_location)
    folium.PolyLine(
        lines,
        color="grey",
        weight=1.5,
        dash_array=10,
        popup=f"{round(earthquake['distance'], 2)} km"
    ).add_to(map_osm)

# Add tectonic plates
url = 'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json'

folium.GeoJson(
    url,
    name='Tectonic plates'
).add_to(map_osm)

# Add layer control
folium.LayerControl().add_to(map_osm)

map_osm.save("earthquake_analytics_test.html")

#closest_earthquake = min([earthquake['distance'] for earthquake in earthquake_data_clean], default="-")
#place_of_closest_earthquake =
#print(f"The closest earthquake was at {round(closest_earthquake, 2)} km of your specified location.")


def get_closest_earthquake_worldwide():
    distances = []
    for i in range(len(earthquake_data)):
        distances.append(earthquake_data[i]["distance"])
    minimum_distance = min(distances)
    index_of_earthquake_with_minimum_distance = distances.index(min(distances))
    place_of_minimum_distance = earthquake_data[index_of_earthquake_with_minimum_distance]["place"]
    return minimum_distance, place_of_minimum_distance


print(get_closest_earthquake_worldwide())
