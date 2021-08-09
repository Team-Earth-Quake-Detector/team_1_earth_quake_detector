from datetime import datetime

import geopy.distance
import requests
import ipinfo


class DataCollector:
    def __init__(self, lat: float = 0, long: float = 0):
        if lat == 0 and long == 0:
            access_token = "62d93ea5300e80"
            handler = ipinfo.getHandler(access_token)
            ip_address = '92.188.181.161'
            details = handler.getDetails(ip_address)
            self.current_location = [(details.loc[0:7]), (details.loc[8:14])]
        else:
            self.current_location = [lat, long]

    def load_data(self):
        """ Get data from USGS API"""
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
        response = requests.get(url)
        self.earthquakes = response.json()['features']

    def prep_data(self):
        """ Extract relevant features: id, longitude, latitude, place, time, magnitude"""
        self.load_data()
        self.earthquake_data = []
        for element in self.earthquakes:
            time = str(datetime.fromtimestamp(element["properties"]["time"] / 1000))
            dict = {"id": element["id"],
                    "longitude": element["geometry"]["coordinates"][0],
                    "latitude": element["geometry"]["coordinates"][1],
                    "place": element["properties"]["place"],
                    "time": time,
                    "magnitude": element["properties"]["mag"],
                    "distance": ""
                    }
            self.earthquake_data.append(dict)
        return self.earthquake_data

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
            earthquake["distance"] = round(distance, 2)
            if distance <= user_provided_radius:
                self.earthquake_data_clean.append(earthquake)
        return self.earthquake_data_clean
