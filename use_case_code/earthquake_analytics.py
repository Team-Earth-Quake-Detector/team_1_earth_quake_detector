from data_collector import DataCollector
import geocoder


class EarthquakeAnalytics:
    def __init__(self, earthquake_data, earthquake_data_clean):
        self.earthquake_data = earthquake_data
        self.earthquake_data_clean = earthquake_data_clean
        self.data_collector = DataCollector()
        self.new_location = DataCollector()

    def get_total_filtered_earthquakes(self, location=None, radius: int = 250):
        total_filtered_earthquakes = len(self.new_location.filter_radius(location=location, user_provided_radius=radius))
        return total_filtered_earthquakes

    def get_filtered_minor_earthquakes(self, location=None, radius: int = 250):
        minor_earthquakes = []
        for earthquake in self.new_location.filter_radius(location=location, user_provided_radius=radius):
            if earthquake["magnitude"] <= 2.5:
                minor_earthquakes.append(earthquake)
        filtered_minor_earthquakes = len(minor_earthquakes)
        return filtered_minor_earthquakes

    def get_filtered_moderate_earthquakes(self, location=None, radius: int = 250):
        moderate_earthquakes = []
        for earthquake in self.new_location.filter_radius(location=location, user_provided_radius=radius):
            if 2.5 < earthquake["magnitude"] <= 6.0:
                moderate_earthquakes.append(earthquake)
        filtered_moderate_earthquakes = len(moderate_earthquakes)
        return filtered_moderate_earthquakes

    def get_filtered_strong_earthquakes(self, location=None, radius: int = 250):
        strong_earthquakes = []
        for earthquake in self.new_location.filter_radius(location=location, user_provided_radius=radius):
            if earthquake["magnitude"] > 6.0:
                strong_earthquakes.append(earthquake)
        filtered_strong_earthquakes = len(strong_earthquakes)
        return filtered_strong_earthquakes

    def get_closest_filtered_earthquake(self, location=None):
        closest_filtered_earthquake = min([earthquake['distance'] for earthquake in self.new_location.filter_radius(location=location, user_provided_radius=15000)], default="-")
        return closest_filtered_earthquake

    def get_place_of_closest_filtered_earthquake(self, location=None):
        earthquake_data_clean = self.new_location.filter_radius(location=location, user_provided_radius=15000)
        distances = []
        for i in range(len(earthquake_data_clean)):
            distances.append(earthquake_data_clean[i]["distance"])
        if len(earthquake_data_clean) != 0:
            index_of_closest_filtered_earthquake = distances.index(min(distances))
            place_of_closest_filtered_earthquake = earthquake_data_clean[index_of_closest_filtered_earthquake]["place"]
            return place_of_closest_filtered_earthquake
        else:
            return "-"

    def get_strongest_filtered_earthquake(self, location=None, radius: int = 250):
        strongest_filtered_earthquake = max([earthquake['magnitude'] for earthquake in self.new_location.filter_radius(location=location, user_provided_radius=radius)], default="-")
        return strongest_filtered_earthquake

    def get_total_earthquakes_worldwide(self):
        total_earthquakes_worldwide = len(self.data_collector.prep_data())
        return total_earthquakes_worldwide

    def get_minor_earthquakes_worldwide(self):
        minor_earthquakes = []
        for earthquake in self.new_location.prep_data():
            if earthquake["magnitude"] <= 2.5:
                minor_earthquakes.append(earthquake)
        minor_earthquakes_worldwide = len(minor_earthquakes)
        return minor_earthquakes_worldwide

    def get_moderate_earthquakes_worldwide(self):
        moderate_earthquakes = []
        for earthquake in self.new_location.prep_data():
            if 2.5 < earthquake["magnitude"] <= 6.0:
                moderate_earthquakes.append(earthquake)
        moderate_earthquakes_worldwide = len(moderate_earthquakes)
        return moderate_earthquakes_worldwide

    def get_strong_earthquakes_worldwide(self):
        strong_earthquakes = []
        for earthquake in self.new_location.prep_data():
            if earthquake["magnitude"] > 6.0:
                strong_earthquakes.append(earthquake)
        strong_earthquakes_worldwide = len(strong_earthquakes)
        return strong_earthquakes_worldwide

    def get_strongest_earthquake_worldwide(self):
        strongest_earthquake_worldwide = max([earthquake['magnitude'] for earthquake in self.data_collector.prep_data()], default="-")
        return strongest_earthquake_worldwide

    def get_place_of_strongest_earthquake_worldwide(self):
        earthquake_data = self.data_collector.prep_data()
        magnitudes = []
        for i in range(len(earthquake_data)):
            magnitudes.append(earthquake_data[i]["magnitude"])
        if len(earthquake_data) != 0:
            index_of_strongest_earthquake_worldwide = magnitudes.index(max(magnitudes))
            place_of_strongest_earthquake_worldwide = earthquake_data[index_of_strongest_earthquake_worldwide]["place"]
            return place_of_strongest_earthquake_worldwide
        else:
            return "-"
