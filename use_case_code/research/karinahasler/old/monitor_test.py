from use_case_code.research.karinahasler.old.data_collector_test import DataCollector


class Monitor:
    def __init__(self):
        pass

    def collect_data(self):
        self.data_collector = DataCollector()
        self.data_collector.data

    def relocate(self, long: float, lat: float, radius: float):
        self.long = input("long")
        self.lat = input()
        self.radius = input()
        # get new coordinates
        # input/search fields


