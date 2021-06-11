from folium import folium
from folium.plugins import geocoder

from use_case.overlay import Overlay


class Map:
    def __init__(self):
        self.overlays = []
        self.set_up_map()

    def set_up_map(self):
        """ Customizes OpenStreetMap """
        # Set up basic OpenStreetMap
        current_location = geocoder.ip('me')
        self.map = folium.Map(location=[(current_location.latlng[0]), (current_location.latlng[1])],
                             zoom_start=5,
                             tiles='StamenTerrain',
                             control_scale=True)
        # save our map to an interactive html file
        #m.save('earthquakes.html')

    def save_map(self, file_name):
        self.map.save(file_name)

    def add_overlay(self,overlay:Overlay):
        self.overlays.append(overlay)
        overlay.apply_overlay(self.map)
#Map und overlay verbinden