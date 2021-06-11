from use_case.map import Map
from overlay import Overlay, EarthquakeOverlay , TectonicOverlay

class Earthquake:
    def __init__(self, data):
        self.long = data["longitude"]
        self.lat = data["latitude"]
        self.mag = data["magnitude"]
        self.id = data["id"]
        self.time = data["time"]

    def get_map(self):
        self.map = Map()
        self.map.add_overlay(EarthquakeOverlay())
        self.map.add_overlay(TectonicOverlay())
        self.map.save('earthquakes.html')

    def render(self, map):
        """ Show map on Monitor """
        pass

#Earthquake und Map verbinden