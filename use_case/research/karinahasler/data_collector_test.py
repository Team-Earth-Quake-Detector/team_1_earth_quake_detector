from datetime import datetime

import geopy.distance
import requests


class DataCollector:
    def __init__(self, long: float = 51.2, lat: float = 6.7, radius: float = 15000): #Düsseldorf default -later current location
        self.long = long
        self.lat = lat
        self.radius = radius
        #self.refresh()

    def load_data(self):
        """ Get data from API"""
        response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
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
                    "magnitude": element["properties"]["mag"]
                    }
            self.earthquake_data.append(dict)

    def filter_radius(self):
        self.prep_data()
        """ Filter data from API by radius"""
        self.earthquake_data_clean = []
        for earthquake in self.earthquake_data:
            starting_point = (self.lat, self.long)
            location = (earthquake["latitude"], earthquake["longitude"])
            distance = geopy.distance.distance(starting_point, location).km
            if distance <= self.radius:
                self.earthquake_data_clean.append(earthquake)

