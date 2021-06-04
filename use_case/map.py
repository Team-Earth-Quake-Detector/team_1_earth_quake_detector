class Map:
    def __init__(self):
        pass

    def get_overlay(self):
        pass

    def set_up_map(self):
        """ Customizes OpenStreetMap """
        # Set up basic OpenStreetMap
        current_location = geocoder.ip('me')
        map_osm = folium.Map(location=[(current_location.latlng[0]), (current_location.latlng[1])],
                             zoom_start=5,
                             tiles='StamenTerrain',
                             control_scale=True)