import folium
import geocoder


class Map:
    def __init__(self):
        self.overlays = []
        self.set_up_map()

    def set_up_map(self):
        """ Customizes OpenStreetMap """
        # Set up basic OpenStreetMap
        current_location = [(geocoder.ip('me').latlng[0]), (geocoder.ip('me').latlng[1])]
        self.map = folium.Map(location=current_location,
                             zoom_start=5,
                             tiles='StamenTerrain',
                             control_scale=True)
        folium.Marker(current_location).add_to(self.map)

    def save_map(self, file_name):
        self.map.save(file_name) # don't save

