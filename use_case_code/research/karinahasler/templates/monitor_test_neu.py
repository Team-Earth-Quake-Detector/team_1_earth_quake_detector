from data_collector_test_neu import DataCollector
from map_test_neu import Map
from overlay_test_neu import EarthquakeOverlay, TectonicOverlay
from earthquake_analytics_test_neu import EarthquakeAnalytics
from geopy.geocoders import Nominatim


class Monitor:
    def __init__(self):
        pass

    def collect_default_data(self):
        self.data_collector = DataCollector()
        self.data_collector.filter_radius()

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

    def build_map(self, location=None, coordinates=None, radius=None):
        self.map = Map()

        if location is None and coordinates is None:
            self.map.set_up_map()
            self.collect_default_data()
            earthquake_overlay = EarthquakeOverlay(self.data_collector.earthquake_data_clean)
            earthquake_overlay.apply_circle_markers(self.map.map)
            earthquake_overlay.apply_magnitude_markers(self.map.map)
            earthquake_overlay.apply_connective_lines(self.map.map)
            earthquake_overlay.apply_heatmap(self.map.map)
            tectonic_overlay = TectonicOverlay()
            tectonic_overlay.apply_overlay(self.map.map)
            tectonic_overlay.add_to_layer_control(self.map.map)
            return self.map

        if location is not None or coordinates is not None:
            self.map.set_up_map(location=coordinates)
            self.relocate(location=location, coordinates=coordinates, radius=radius)
            earthquake_overlay = EarthquakeOverlay(self.new_location.earthquake_data_clean)
            earthquake_overlay.apply_circle_markers(self.map.map)
            earthquake_overlay.apply_magnitude_markers(self.map.map)
            earthquake_overlay.apply_connective_lines(self.map.map, coordinates)
            earthquake_overlay.apply_heatmap(self.map.map)
            tectonic_overlay = TectonicOverlay()
            tectonic_overlay.apply_overlay(self.map.map)
            tectonic_overlay.add_to_layer_control(self.map.map)
            return self.map

    def perform_earthquake_analytics(self, location=None, radius=None):
        self.data_collector = DataCollector()
        self.data_collector.prep_data()
        self.data_collector.filter_radius()
        earthquake_analytics = EarthquakeAnalytics(self.data_collector.earthquake_data, self.data_collector.earthquake_data_clean)

        total_filtered = earthquake_analytics.get_total_filtered_earthquakes(location=location, radius=radius)
        minor_filtered = earthquake_analytics.get_filtered_minor_earthquakes(location=location, radius=radius)
        moderate_filtered = earthquake_analytics.get_filtered_moderate_earthquakes(location=location, radius=radius)
        strong_filtered = earthquake_analytics.get_filtered_strong_earthquakes(location=location, radius=radius)
        closest_filtered = earthquake_analytics.get_closest_filtered_earthquake(location=location, radius=radius)
        place_of_closest_filtered = earthquake_analytics.get_place_of_closest_filtered_earthquake(location=location, radius=radius)
        strongest_filtered = earthquake_analytics.get_strongest_filtered_earthquake(location=location, radius=radius)
        total_worldwide = earthquake_analytics.get_total_earthquakes_worldwide()
        minor_worldwide = earthquake_analytics.get_minor_earthquakes_worldwide()
        moderate_worldwide = earthquake_analytics.get_moderate_earthquakes_worldwide()
        strong_worldwide = earthquake_analytics.get_strong_earthquakes_worldwide()
        strongest_worldwide = earthquake_analytics.get_strongest_earthquake_worldwide()
        place_of_strongest_worldwide = earthquake_analytics.get_place_of_strongest_earthquake_worldwide()

        return total_filtered, minor_filtered, moderate_filtered, strong_filtered, closest_filtered, place_of_closest_filtered, \
               strongest_filtered, total_worldwide, minor_worldwide, moderate_worldwide, strong_worldwide, strongest_worldwide,\
               place_of_strongest_worldwide
