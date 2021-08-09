from flask import request

import folium
import ipinfo


class Map:
    def __init__(self, lat: float = 0, long: float = 0):
        self.overlays = []
        if lat == 0 and long == 0:
            access_token = "62d93ea5300e80"
            handler = ipinfo.getHandler(access_token)
            ip_address = '92.188.181.161'
            details = handler.getDetails(ip_address)
            self.current_location = [(details.loc[0:7]), (details.loc[8:14])]
        else:
            self.current_location = [lat, long]

    def set_up_map(self, location=None):
        """ Customizes OpenStreetMap """
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
