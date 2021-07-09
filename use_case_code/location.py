from __future__ import annotations
__author__ = "Thomas Zeutschler"
import math
from math import sin, cos, acos, asin, sqrt, atan2, radians, degrees
import numpy as np


class Location:
    """
    Wraps a location made of latitude and Longitude.
    """
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Position([lat: {self.latitude}, lon:{self.longitude}])"

    def __str__(self):
        return f"[lat: {self.latitude}, lon:{self.longitude}]"

    def clone(self) -> Location:
        """Create of shallow copy of the Location instance."""
        return Location(self.latitude, self.longitude)

    def __sub__(self, other) -> float:
        """
        Returns the distance between 2 locations in km.
        """
        # ToDo by TZ: calculate and return the distance between the 2 locations. Hint: look below...
        raise NotImplementedError

    def get_country(self):
        # ToDo by TZ: evaluate and country of the location.
        #  If there is non e.g. over the ocean, return None
        raise NotImplementedError

    def get_city(self):
        # ToDo by TZ: evaluate and the city nearest to the location.
        #  If there is no city, return the self.__str__()
        raise NotImplementedError

    def get_address(self):
        # ToDo by TZ: return the full address of the location, whatever it is.
        raise NotImplementedError

    def distance_to(self, other: Location) -> float:
        """
        Return the distance of 2 locations in km.
        """
        earth_radius = 6373.0
        lat1 = radians(self.latitude)
        lon1 = radians(self.longitude)
        lat2 = radians(other.latitude)
        lon2 = radians(other.longitude)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        return earth_radius * 2 * atan2(sqrt(a), sqrt(1 - a))

    def shift_latitude(self, km: float) -> Location:
        """
        Returns a location shifted by certain kilometers along the latitude of the current location (north <-> south).
        """
        # ToDo by TZ: Please implement....
        raise NotImplementedError

    def shift_longitude(self, km: float) -> Location:
        """
        Returns a location shifted by certain kilometers along the longitude of the current location (west <-> east).
        """
        # ToDo by TZ: Please implement....
        raise NotImplementedError

    def shift(self, km_lat: float, km_lon: float) -> Location:
        """
        Returns a location shifted by certain kilometers along the longitude and latitude.
        """
        return self.displace(0, km_lat).displace(90, km_lon)

    def center(self, other: Location) -> Location:
        """
        Evaluates the location in the center (middle) of the current and another location.
        """
        lat = radians(self.latitude)
        lon = radians(self.longitude)
        x = cos(lat) * cos(lon)
        y = cos(lat) * sin(lon)
        z = sin(lat)

        lat = radians(other.latitude)
        lon = radians(other.longitude)
        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)

        x = x / 2
        y = y / 2
        z = z / 2
        central_lon = atan2(y, x)
        central_square_root = sqrt(x * x + y * y)
        central_lat = atan2(z, central_square_root)

        return Location(degrees(central_lat), degrees(central_lon))

    def displace(self, theta: float, distance: float):
        """
        Displace a location by theta degrees counterclockwise and some km in that direction.
        Notes:
            http://www.movable-type.co.uk/scripts/latlong.html            0 DEGREES IS THE VERTICAL Y AXIS! IMPORTANT!
        Args:
            theta:    A number in degrees.
            distance: A number in meters.
        Returns:
            A new LatLng.
        """
        earth_radius = 6373.0
        pi = math.pi
        delta = distance /earth_radius
        theta = radians(theta)
        lat1 = radians(self.latitude)
        lng1 = radians(self.longitude)

        lat2 = asin(sin(lat1) * cos(delta) + cos(lat1) * sin(delta) * cos(theta))

        lng2 = lng1 + atan2(sin(theta) * sin(delta) * cos(lat1), cos(delta) - sin(lat1) * sin(lat2))
        lng2 = (lng2 + 3 * pi) % (2 * pi) - pi

        return Location(degrees(lat2), degrees(lng2))

