from data_collector import DataCollector

class EarthquakeAnalytics:

    def __init__(self, earthquake_data, earthquake_data_clean):
        self.earthquake_data = earthquake_data
        self.earthquake_data_clean = earthquake_data_clean

    def get_total_filtered_earthquakes(self, location=None, radius: int = 250):
        if location is None:
            self.data_collector = DataCollector()
            total_filtered_earthquakes = len(self.data_collector.filter_radius())
            return total_filtered_earthquakes

        if location is not None:
            self.new_location = DataCollector()
            total_filtered_earthquakes = len(self.new_location.filter_radius(location=location, user_provided_radius=radius))
            return total_filtered_earthquakes

    def get_filtered_minor_earthquakes(self):
        minor_earthquakes = []
        for earthquake in self.earthquake_data_clean:
            if earthquake["magnitude"] <= 2.5:
                minor_earthquakes.append(earthquake)

        filtered_minor_earthquakes = len(minor_earthquakes)
        if filtered_minor_earthquakes == 0:
            pass
        elif filtered_minor_earthquakes == 1:
            print(f"{filtered_minor_earthquakes} of these earthquakes was a minor earthquake with a magnitude below or equal to 2.5. These types of earthquakes occur frequently and are unlikely to cause damage.")
        else:
            print(f"{filtered_minor_earthquakes} of these earthquakes were minor earthquakes with a magnitude below or equal to 2.5. These types of earthquakes occur frequently and are unlikely to cause damage.")
        return filtered_minor_earthquakes

    def get_filtered_moderate_earthquakes(self):
        moderate_earthquakes = []
        for earthquake in self.earthquake_data_clean:
            if 2.5 < earthquake["magnitude"] <= 6.0:
                moderate_earthquakes.append(earthquake)

        filtered_moderate_earthquakes = len(moderate_earthquakes)
        if filtered_moderate_earthquakes == 0:
            pass
        elif filtered_moderate_earthquakes == 1:
            print(f"{filtered_moderate_earthquakes} of these earthquakes was a moderate earthquake with a magnitude between 2.5 and 6.0. These types of earthquakes occur less often and might cause damage.")
        else:
            print(f"{filtered_moderate_earthquakes} of these earthquakes were moderate earthquakes with a magnitude between 2.5 and 6.0. These types of earthquakes occur less often and might cause damage.")
        return filtered_moderate_earthquakes

    def get_filtered_strong_earthquakes(self):
        strong_earthquakes = []
        for earthquake in self.earthquake_data_clean:
            if earthquake["magnitude"] > 6.0:
                strong_earthquakes.append(earthquake)

        filtered_strong_earthquakes = len(strong_earthquakes)
        if filtered_strong_earthquakes == 0:
            pass
        elif filtered_strong_earthquakes == 1:
            print(f"{filtered_strong_earthquakes} of these earthquakes was a strong earthquake with a magnitude above 6.0. These types of earthquakes occur rarely and are likely to cause major damage.")
        else:
            print(f"{filtered_strong_earthquakes} of these earthquakes were strong earthquake with a magnitude above 6.0. These types of earthquakes occur rarely and are likely to cause major damage.")
        return filtered_strong_earthquakes

    def get_closest_earthquake(self):
        closest_earthquake = min(earthquake['distance'] for earthquake in self.earthquake_data_clean)
        print(f"The closest earthquake was at {round(closest_earthquake, 2)} km of your specified location.")
        return closest_earthquake

    def get_strongest_filtered_earthquake(self):
        strongest_filtered_earthquake = max(earthquake['magnitude'] for earthquake in self.earthquake_data_clean)
        print(f"The strongest earthquake within your specified region had a magnitude of {strongest_filtered_earthquake}.")
        return strongest_filtered_earthquake

    def get_total_earthquakes_worldwide(self):
        total_earthquakes_worldwide = len(self.earthquake_data)  # total_earthquakes_worldwide
        print(f"Within the last 24 hours, {total_earthquakes_worldwide} occurences of earthquakes have been recorded worldwide.")
        return total_earthquakes_worldwide

    def get_strongest_earthquake_worldwide(self):
        strongest_earthquake_worldwide = max(earthquake['magnitude'] for earthquake in self.earthquake_data)
        print(f"The strongest earthquake worldwide within the last 24 hours had a magnitude of {strongest_earthquake_worldwide}.")
        return strongest_earthquake_worldwide
