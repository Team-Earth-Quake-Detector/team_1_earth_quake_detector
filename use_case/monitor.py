from data_collector import DataCollector
from map import Map
from overlay import EarthquakeOverlay, TectonicOverlay


class Monitor:
    def __init__(self):
        pass

    def collect_data(self):
        self.data_collector = DataCollector()
        self.data_collector.filter_radius()

    def build_map(self):
        self.collect_data()
        self.map = Map()
        earthquake_overlay = EarthquakeOverlay(self.data_collector.earthquake_data_clean)
        earthquake_overlay.apply_overlay(self.map.map)
        tectonic_overlay = TectonicOverlay()
        tectonic_overlay.apply_overlay(self.map.map)
        tectonic_overlay.add_to_layer_control(self.map.map)
        return self.map

    def relocate(self, long: float, lat: float, radius: float):
        self.long = input("long")
        self.lat = input()
        self.radius = input()
        # get new coordinates
        # input/search fields


