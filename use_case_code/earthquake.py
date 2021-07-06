from datetime import datetime

from use_case_code.map import Map
from use_case_code.research.karinahasler.overlay_test import Overlay, EarthquakeOverlay, TectonicOverlay
from typing import List # iterate over each element


# List of earthquakes
# Apply methods to individual earthquake


class EarthquakeList():
    def __init__(self, json):
        self.earthquakes = []
        self.json = json
        for element in self.json:
            time = str(datetime.fromtimestamp(element["properties"]["time"] / 1000))
            dict = {"id": element["id"],
                    "longitude": element["geometry"]["coordinates"][0],
                    "latitude": element["geometry"]["coordinates"][1],
                    "time": time,
                    "magnitude": element["properties"]["mag"]
                    }
            self.earthquakes.append(Earthquake(dict))

    def __len__(self):
        return len(self.earthquakes)

    def filter_by_magnitude(self, magnitude: float = 2.5):
        pass


class Earthquake:
    def __init__(self, data):
        self.long = data["longitude"]
        self.lat = data["latitude"]
        self.mag = data["magnitude"]
        self.id = data["id"]
        self.time = data["time"]

    def get_map(self, map):
        self.map = Map()
        self.map.set_up_map()
        self.map.add_overlay(EarthquakeOverlay())
        self.map.add_overlay(TectonicOverlay())
        self.map.save_map('earthquakes.html')

    def render(self, map):
        """ Show map on Monitor """
        pass

#Earthquake und Map verbinden