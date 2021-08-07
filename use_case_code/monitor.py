from data_collector import DataCollector
from map import Map
from overlay import EarthquakeOverlay, TectonicOverlay
from earthquake_analytics import EarthquakeAnalytics
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
            earthquake_overlay.apply_overlay(self.map.map)
            earthquake_overlay.apply_heatmap(self.map.map)
            tectonic_overlay = TectonicOverlay()
            tectonic_overlay.apply_overlay(self.map.map)
            tectonic_overlay.add_to_layer_control(self.map.map)
            return self.map

        if location is not None or coordinates is not None:
            self.map.set_up_map(location=coordinates)
            self.relocate(location=location, coordinates=coordinates, radius=radius)
            earthquake_overlay = EarthquakeOverlay(self.new_location.earthquake_data_clean)
            earthquake_overlay.apply_overlay(self.map.map, coordinates)
            earthquake_overlay.apply_heatmap(self.map.map)
            tectonic_overlay = TectonicOverlay()
            tectonic_overlay.apply_overlay(self.map.map)
            tectonic_overlay.add_to_layer_control(self.map.map)
            return self.map

    def test_get_total_filtered_earthquakes(self, location=None):
        if location is None:
            self.data_collector = DataCollector()
            total_filtered_earthquakes = len(self.data_collector.filter_radius())
            return total_filtered_earthquakes

        if location is not None:
            self.new_location = DataCollector()
            total_filtered_earthquakes = len(self.new_location.filter_radius(location=location))
            return total_filtered_earthquakes

    def test_perform_earthquake_analytics(self, location=None, radius=None):
        self.data_collector = DataCollector()
        self.data_collector.prep_data()
        self.data_collector.filter_radius()
        earthquake_analytics = EarthquakeAnalytics(self.data_collector.earthquake_data, self.data_collector.earthquake_data_clean)

        total = earthquake_analytics.get_total_filtered_earthquakes(location=location, radius=radius)

        return total

    def perform_earthquake_analytics(self, location=None, coordinates=None, radius: int = 250):
        self.data_collector = DataCollector()


        if location is None and coordinates is None:
            self.data_collector.prep_data()
            self.data_collector.filter_radius()
            earthquake_analytics = EarthquakeAnalytics(self.data_collector.earthquake_data, self.data_collector.earthquake_data_clean)
            total_earthquakes_worldwide = earthquake_analytics.get_total_earthquakes_worldwide()
            strongest_earthquake_worldwide = earthquake_analytics.get_strongest_earthquake_worldwide()
            return total_earthquakes_worldwide, strongest_earthquake_worldwide

        if location is not None:
            relocate_location = self.relocate(location=location)
            earthquake_analytics = EarthquakeAnalytics(relocate_location.earthquake_data, relocate_location.earthquake_data_clean)

            total_filtered_earthquakes = earthquake_analytics.get_total_filtered_earthquakes()
            filtered_minor_earthquakes = earthquake_analytics.get_filtered_minor_earthquakes()
            filtered_moderate_earthquakes = earthquake_analytics.get_filtered_moderate_earthquakes()
            filtered_strong_earthquakes = earthquake_analytics.get_filtered_strong_earthquakes()
            closest_earthquake = earthquake_analytics.get_closest_earthquake()
            strongest_filtered_earthquake = earthquake_analytics.get_strongest_filtered_earthquake()
            total_earthquakes_worldwide = earthquake_analytics.get_total_earthquakes_worldwide()
            strongest_earthquake_worldwide = earthquake_analytics.get_strongest_earthquake_worldwide()
            return total_filtered_earthquakes, filtered_minor_earthquakes, filtered_moderate_earthquakes, filtered_strong_earthquakes, closest_earthquake, strongest_filtered_earthquake, total_earthquakes_worldwide, strongest_earthquake_worldwide

        if coordinates is not None:
            relocate_coordinates = self.relocate(coordinates=coordinates)
            earthquake_analytics = EarthquakeAnalytics(relocate_coordinates.earthquake_data,
                                                       relocate_coordinates.earthquake_data_clean)

            total_filtered_earthquakes = earthquake_analytics.get_total_filtered_earthquakes()
            filtered_minor_earthquakes = earthquake_analytics.get_filtered_minor_earthquakes()
            filtered_moderate_earthquakes = earthquake_analytics.get_filtered_moderate_earthquakes()
            filtered_strong_earthquakes = earthquake_analytics.get_filtered_strong_earthquakes()
            closest_earthquake = earthquake_analytics.get_closest_earthquake()
            strongest_filtered_earthquake = earthquake_analytics.get_strongest_filtered_earthquake()
            total_earthquakes_worldwide = earthquake_analytics.get_total_earthquakes_worldwide()
            strongest_earthquake_worldwide = earthquake_analytics.get_strongest_earthquake_worldwide()
            return total_filtered_earthquakes, filtered_minor_earthquakes, filtered_moderate_earthquakes, filtered_strong_earthquakes, closest_earthquake, strongest_filtered_earthquake, total_earthquakes_worldwide, strongest_earthquake_worldwide
