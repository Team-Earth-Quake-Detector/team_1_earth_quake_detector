__author__ = "Thomas Zeutschler"


class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Position([lat: {self.latitude}, lon:{self.longitude}])"

    def __str__(self):
        return f"[lat: {self.latitude}, lon:{self.longitude}]"
