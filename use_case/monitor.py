from data_collector import DataCollector
from map import Map
from overlay import EarthquakeOverlay, TectonicOverlay
from geopy.geocoders import Nominatim


class Monitor:
    def __init__(self):
        pass

    def collect_default_data(self):
        self.data_collector = DataCollector()
        self.data_collector.filter_radius()

    def build_default_map(self):
        self.collect_default_data()
        self.map = Map()
        earthquake_overlay = EarthquakeOverlay(self.data_collector.earthquake_data_clean)
        earthquake_overlay.apply_overlay(self.map.map)
        tectonic_overlay = TectonicOverlay()
        tectonic_overlay.apply_overlay(self.map.map)
        tectonic_overlay.add_to_layer_control(self.map.map)
        return self.map

    def relocate(self, location=None, coordinates=None, radius: int = 250):
        self.new_location = DataCollector()
        if location is not None:
            geolocator = Nominatim(user_agent="team_1_earthquake_detector")
            location_latitude = geolocator.geocode(location).latitude
            location_longitude = geolocator.geocode(location).longitude
            location_coordinates = (location_latitude, location_longitude)
            return self.new_location.filter_radius(location_coordinates, radius)

        if coordinates is not None:
            return self.new_location.filter_radius(coordinates, radius)

        # get new coordinates
        # input/search fields

    def build_new_map(self):
        self.relocate()
        self.map = Map()
        earthquake_overlay = EarthquakeOverlay(self.new_location.earthquake_data_clean)
        earthquake_overlay.apply_overlay(self.map.map)
        tectonic_overlay = TectonicOverlay()
        tectonic_overlay.apply_overlay(self.map.map)
        tectonic_overlay.add_to_layer_control(self.map.map)
        return self.map
