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
        #self.refresh()

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

    def filter_radius(self, location=None, radius: int = 15000): # change radius to 250 later
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
            if distance <= radius:
                self.earthquake_data_clean.append(earthquake)
        return self.earthquake_data_clean

    def earthquake_analytics(self):
        number_of_earthquakes = len(self.earthquake_data_clean)
        closest_earthquake = min(earthquake['distance'] for earthquake in self.earthquake_data_clean)
        return number_of_earthquakes, closest_earthquake
