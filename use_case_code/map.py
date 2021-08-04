from math import sqrt

from flask import request

import folium
import geocoder


class Map:
    def __init__(self, lat: float = 0, long: float = 0):
        self.overlays = []
        if lat == 0 and long == 0:
            self.current_location = [(geocoder.ip('me').latlng[0]), (geocoder.ip('me').latlng[1])]
        else:
            self.current_location = [lat, long]

    def set_up_map(self, location=None):
        """ Customizes OpenStreetMap """
        # Set up basic OpenStreetMap
        if location is None:
            location = self.current_location
        user_provided_radius = request.args.get('radius', default=250, type=int)
        self.map = folium.Map(location=location,
                             zoom_start=((1 / user_provided_radius) * sqrt(user_provided_radius) * 100),
                             tiles='OpenStreetMap',
                             control_scale=True)
        folium.Marker(location).add_to(self.map)

    def save_map(self, file_name):
        self.map.save(file_name) # don't save

