import folium
import branca.colormap as cm
import geocoder


class Overlay: #Basisklasse für alle overlays
    def __init__(self):
        pass

    def apply_overlay(self, map):
        pass

    def add_to_layer_control(self, map):
        pass


class EarthquakeOverlay(Overlay):

    def __init__(self, earthquake_data_clean):
        super().__init__()
        self.earthquake_data_clean = earthquake_data_clean

    def apply_overlay(self, map):
        current_location = [(geocoder.ip('me').latlng[0]), (geocoder.ip('me').latlng[1])]
        colormap = cm.LinearColormap(colors=['orange', 'red'], index=[0, 10], vmin=0, vmax=10)

        for earthquake in self.earthquake_data_clean:
            location = (earthquake["latitude"], earthquake["longitude"])
            tooltip_text = f"Time: {earthquake['time']}\n Magnitude: {earthquake['magnitude']}"
            radius = earthquake['magnitude'] * 50000
            folium.Circle(
                location=location,
                tooltip=tooltip_text,
                radius=radius,
                fill=True,
                color=colormap(earthquake['magnitude']),
                weight=1,
                fill_opacity=0.5
            ).add_to(map)

            lines = []
            lines.append(current_location)
            lines.append(location)
            folium.PolyLine(
                lines,
                color="grey",
                dash_array=10,
                popup=f"{round(earthquake['distance'], 2)} km"
            ).add_to(map)


class TectonicOverlay(Overlay):

    def apply_overlay(self, map):
        """Add tectonic plates"""
        url = 'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json'

        folium.GeoJson(
            url,
            name='Tectonic plates'
        ).add_to(map)

    def add_to_layer_control(self, map):
        folium.LayerControl().add_to(map)
