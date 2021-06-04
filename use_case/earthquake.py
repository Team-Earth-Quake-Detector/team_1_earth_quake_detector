from use_case.map import Map


class Earthquake:
    def __init__(self, data):
        self.long = data["longitude"]
        self.lat = data["latitude"]
        self.mag = data["magnitude"]
        self.id = data["id"]
        self.time = data["time"]

    def get_map(self):
        self.map = Map()

    def render(self, map):
        """ Show map on Monitor """
        self.map
        return"HTML"