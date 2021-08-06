import folium
import webbrowser
import branca.colormap as cm
import requests
from datetime import datetime
import geocoder
import geopy.distance

user_provided_location = [35.652832, 139.839478]
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

#file_path = r"/templates/earthquake_map.html"
#map_osm.save(file_path) # Save as html file
#webbrowser.open(file_path) # Default browser open


total_number_of_filtered_earthquakes = len(earthquake_data_clean)
if total_number_of_filtered_earthquakes == 0:
    pass
elif total_number_of_filtered_earthquakes == 1:
    print(f"There has been {total_number_of_filtered_earthquakes} earthquake within a distance of {user_provided_radius} km of your specified location within the last 24 hours.")
else:
    print(f"There have been {total_number_of_filtered_earthquakes} earthquakes within a distance of {user_provided_radius} km of your specified location within the last 24 hours.")

minor_earthquakes = []
for earthquake in earthquake_data_clean:
    if earthquake["magnitude"] <= 2.5:
        minor_earthquakes.append(earthquake)

number_of_minor_earthquakes = len(minor_earthquakes)
if number_of_minor_earthquakes == 0:
    pass
elif number_of_minor_earthquakes == 1:
    print(f"{number_of_minor_earthquakes} of these earthquakes was a minor earthquake with a magnitude below or equal to 2.5. These types of earthquakes occur frequently and are unlikely to cause damage.")
else:
    print(f"{number_of_minor_earthquakes} of these earthquakes were minor earthquakes with a magnitude below or equal to 2.5. These types of earthquakes occur frequently and are unlikely to cause damage.")

moderate_earthquakes = []
for earthquake in earthquake_data_clean:
    if 2.5 < earthquake["magnitude"] <= 6.0:
        moderate_earthquakes.append(earthquake)

number_of_moderate_earthquakes = len(moderate_earthquakes)
if number_of_moderate_earthquakes == 0:
    pass
elif number_of_moderate_earthquakes == 1:
    print(f"{number_of_moderate_earthquakes} of these earthquakes was a moderate earthquake with a magnitude between 2.5 and 6.0. These types of earthquakes occur less often and might cause damage.")
else:
    print(f"{number_of_moderate_earthquakes} of these earthquakes were moderate earthquakes with a magnitude between 2.5 and 6.0. These types of earthquakes occur less often and might cause damage.")

strong_earthquakes = []
for earthquake in earthquake_data_clean:
    if earthquake["magnitude"] > 6.0:
        strong_earthquakes.append(earthquake)

number_of_strong_earthquakes = len(strong_earthquakes)
if number_of_strong_earthquakes == 0:
    pass
elif number_of_strong_earthquakes == 1:
    print(f"{number_of_strong_earthquakes} of these earthquakes was a strong earthquake with a magnitude above 6.0. These types of earthquakes occur rarely and are likely to cause major damage.")
else:
    print(f"{number_of_strong_earthquakes} of these earthquakes were strong earthquake with a magnitude above 6.0. These types of earthquakes occur rarely and are likely to cause major damage.")


closest_earthquake = min(earthquake['distance'] for earthquake in earthquake_data_clean)
print(f"The closest earthquake was at {round(closest_earthquake, 2)} km of your specified location.")

strongest_filtered_earthquake = max(earthquake['magnitude'] for earthquake in earthquake_data_clean)
print(f"The strongest earthquake within your specified region had a magnitude of {strongest_filtered_earthquake}.")

total_number_of_earthquakes_worldwide = len(earthquake_data)
print(f"Within the last 24 hours, {total_number_of_earthquakes_worldwide} occurences of earthquakes have been recorded worldwide.")

strongest_earthquake_worldwide = max(earthquake['magnitude'] for earthquake in earthquake_data)
print(f"The strongest earthquake worldwide within the last 24 hours had a magnitude of {strongest_earthquake_worldwide}.")
