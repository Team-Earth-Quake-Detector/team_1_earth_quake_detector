from map.py import Map()

class Overlay:
    pass

    def get_earthquake_overlay(self):
        """Visualize earthquake data"""
        colormap = cm.LinearColormap(colors=['orange', 'red'], index=[0, 10], vmin=0, vmax=10)

        for earthquake in earthquake_data:
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
            ).add_to(map_osm)

    def get_tectonic_plates_overlay(self):
        """Add tectonic plates"""
        url = 'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json'

        folium.GeoJson(
            url,
            name='Tectonic plates'
        ).add_to(map_osm)

    def get_layer_control_overlay(self):
        """Add layer control"""
        folium.LayerControl().add_to(map_osm)

        file_path = r"/templates/earthquake_map.html"
        map_osm.save(file_path)  # Save as html file
        webbrowser.open(file_path)  # Default browser open