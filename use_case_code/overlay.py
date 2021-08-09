import folium
from folium.features import DivIcon
from folium.plugins import HeatMap
import branca.colormap as cm
import geocoder


class Overlay:
    def __init__(self, lat: float = 0, long: float = 0):
        if lat == 0 and long == 0:
            self.current_location = [(geocoder.ip('me').latlng[0]), (geocoder.ip('me').latlng[1])]
        else:
            self.current_location = [lat, long]


class EarthquakeOverlay(Overlay):

    def __init__(self, earthquake_data_clean):
        super().__init__()
        self.earthquake_data_clean = earthquake_data_clean

    def apply_circle_markers(self, map):
        colormap = cm.LinearColormap(colors=['orange', 'red'], index=[0, 10], vmin=0, vmax=10)

        circle_markers = folium.FeatureGroup(name='Circle markers')
        map.add_child(circle_markers)

        for earthquake in self.earthquake_data_clean:
            earthquake_location = (earthquake["latitude"], earthquake["longitude"])
            tooltip_text = f"Time: {earthquake['time']}\n Magnitude: {earthquake['magnitude']}"
            radius = earthquake['magnitude'] * 50000
            folium.Circle(
                location=earthquake_location,
                tooltip=tooltip_text,
                radius=radius,
                fill=True,
                color=colormap(earthquake['magnitude']),
                weight=1,
                fill_opacity=0.5
            ).add_to(circle_markers)

    def apply_magnitude_markers(self, map):
        magnitude_markers = folium.FeatureGroup(name='Magnitude markers')
        map.add_child(magnitude_markers)

        for earthquake in self.earthquake_data_clean:
            earthquake_location = (earthquake["latitude"], earthquake["longitude"])
            folium.Marker(earthquake_location,
                          icon=DivIcon(
                              icon_size=(150, 36),
                              icon_anchor=(0, 0),
                              html='<div style="font-size: 10pt; color: grey">%s</div>' % earthquake['magnitude'])
                          ).add_to(magnitude_markers)

    def apply_connective_lines(self, map, location=None):
        if location is None:
            location = self.current_location

        connective_lines = folium.FeatureGroup(name='Connective lines')
        map.add_child(connective_lines)

        for earthquake in self.earthquake_data_clean:
            earthquake_location = (earthquake["latitude"], earthquake["longitude"])
            lines = []
            lines.append(location)
            lines.append(earthquake_location)
            folium.PolyLine(
                lines,
                color="grey",
                weight=1.5,
                dash_array=10,
                popup=f"{earthquake['distance']} km"
            ).add_to(connective_lines)

    def apply_heatmap(self, map):
        heat_data = [[earthquake["latitude"], earthquake["longitude"]] for earthquake in self.earthquake_data_clean]
        HeatMap(heat_data, name="Heatmap", show=False).add_to(map)


class TectonicOverlay(Overlay):

    def apply_overlay(self, map):
        url = 'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json'

        folium.GeoJson(url, name='Tectonic plates').add_to(map)

    def add_to_layer_control(self, map):
        folium.LayerControl().add_to(map)
