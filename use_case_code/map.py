from flask import request

import folium
import geocoder


class Map:
    def __init__(self, lat: float = 0, long: float = 0):
        if lat == 0 and long == 0:
            self.current_location = [(geocoder.ip('me').latlng[0]), (geocoder.ip('me').latlng[1])]
        else:
            self.current_location = [lat, long]

    def set_up_map(self, location=None):
        if location is None:
            location = self.current_location

        zoom_start_dict = {}
        for i in range(0, 19):
            zoom_start_dict[100 + i * 50] = 7.0 - i * 0.1
        user_provided_radius = request.args.get('radius', default=250, type=int)

        self.map = folium.Map(location=location,
                             zoom_start=zoom_start_dict[user_provided_radius],
                             tiles='OpenStreetMap',
                             control_scale=True)
        folium.Marker(location).add_to(self.map)

    def save_map(self, file_name):
        self.map.save(file_name)
