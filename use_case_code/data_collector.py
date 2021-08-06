from datetime import datetime

import geopy.distance
import requests
import geocoder

from earthquake import EarthquakeList


class DataCollector:
    def __init__(self, lat: float = 0, long: float = 0):
        if lat == 0 and long == 0:
            self.current_location = [(geocoder.ip('me').latlng[0]), (geocoder.ip('me').latlng[1])]
        else:
            self.current_location = [lat, long]

    def load_data(self):
        """ Get data from API"""
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
        response = requests.get(url)
        self.earthquakes = response.json()['features']

    def prep_data(self):
        """ Extract relevant features: id, longitude, latitude, time, magnitude"""
        self.load_data()
        self.earthquake_data = []
        for element in self.earthquakes:
            time = str(datetime.fromtimestamp(element["properties"]["time"] / 1000))
            dict = {"id": element["id"],
                    "longitude": element["geometry"]["coordinates"][0],
                    "latitude": element["geometry"]["coordinates"][1],
                    "time": time,
                    "magnitude": element["properties"]["mag"],
                    "distance": ""
                    }
            self.earthquake_data.append(dict)
        eql = EarthquakeList(self.earthquakes)

    def filter_radius(self, location=None, user_provided_radius: int = 250):
        self.prep_data()
        """ Filter data from API by radius"""
        if location is None:
            location = self.current_location
        self.earthquake_data_clean = []
        for earthquake in self.earthquake_data:
            starting_point = location
            earthquake_location = (earthquake["latitude"], earthquake["longitude"])
            distance = geopy.distance.distance(starting_point, earthquake_location).km
            earthquake["distance"] = distance
            if distance <= user_provided_radius:
                self.earthquake_data_clean.append(earthquake)
        return self.earthquake_data_clean

    def earthquake_analytics(self, user_provided_radius: int = 250):
        total_number_of_filtered_earthquakes = len(self.earthquake_data_clean)
        if total_number_of_filtered_earthquakes == 0:
            pass
        elif total_number_of_filtered_earthquakes == 1:
            print(f"There has been {total_number_of_filtered_earthquakes} earthquake within a distance of {user_provided_radius} km of your specified location within the last 24 hours.")
        else:
            print(f"There have been {total_number_of_filtered_earthquakes} earthquakes within a distance of {user_provided_radius} km of your specified location within the last 24 hours.")

        minor_earthquakes = []
        for earthquake in self.earthquake_data_clean:
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
        for earthquake in self.earthquake_data_clean:
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
        for earthquake in self.earthquake_data_clean:
            if earthquake["magnitude"] > 6.0:
                strong_earthquakes.append(earthquake)

        number_of_strong_earthquakes = len(strong_earthquakes)
        if number_of_strong_earthquakes == 0:
            pass
        elif number_of_strong_earthquakes == 1:
            print(f"{number_of_strong_earthquakes} of these earthquakes was a strong earthquake with a magnitude above 6.0. These types of earthquakes occur rarely and are likely to cause major damage.")
        else:
            print(f"{number_of_strong_earthquakes} of these earthquakes were strong earthquake with a magnitude above 6.0. These types of earthquakes occur rarely and are likely to cause major damage.")

        closest_earthquake = min(earthquake['distance'] for earthquake in self.earthquake_data_clean)
        print(f"The closest earthquake was at {round(closest_earthquake, 2)} km of your specified location.")

        strongest_filtered_earthquake = max(earthquake['magnitude'] for earthquake in self.earthquake_data_clean)
        print(f"The strongest earthquake within your specified region had a magnitude of {strongest_filtered_earthquake}.")

        total_number_of_earthquakes_worldwide = len(self.earthquake_data)
        print(f"Within the last 24 hours, {total_number_of_earthquakes_worldwide} occurences of earthquakes have been recorded worldwide.")

        strongest_earthquake_worldwide = max(earthquake['magnitude'] for earthquake in self.earthquake_data)
        print(f"The strongest earthquake worldwide within the last 24 hours had a magnitude of {strongest_earthquake_worldwide}.")

        return total_number_of_filtered_earthquakes, number_of_minor_earthquakes, number_of_moderate_earthquakes, number_of_strong_earthquakes,\
               closest_earthquake, strongest_filtered_earthquake, total_number_of_earthquakes_worldwide, strongest_earthquake_worldwide
