class Earthquake:
    def __init__(self, data):
        self.long = data["longitude"]
        pass

    def render(self, map):
        return"HTML"