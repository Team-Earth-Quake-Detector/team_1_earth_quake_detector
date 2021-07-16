from location import Location
import geocoder
from geopy.geocoders import Nominatim


class LocationResolver:
    """
    Resolves a location by a given city or location name
    """
    def __init__(self, address: str = ""):
        g = geocoder.osm(address)
        geo_data = g.osm
        self.query = address
        self.address = g.address
        self.json = geo_data
        if self.json:
            self.latitude = float(geo_data.get('y'))
            self.longitude = float(geo_data.get('x'))
            self.location = Location(self.latitude, self.longitude)
        else:
            self.get_current_location()

    def get_current_location(self):
        self.latitude = geocoder.ip('me').latlng[0]
        self.longitude = geocoder.ip('me').latlng[1]
        geolocator = Nominatim(user_agent="team_1_earthquake_detector")
        current_location = geolocator.reverse(f"{self.latitude}, {self.longitude}")
        self.address = current_location.address
        self.location = Location(self.latitude, self.longitude)
        self.query = "My location"
        return current_location
