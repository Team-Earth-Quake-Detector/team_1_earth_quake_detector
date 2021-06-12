import os

from flask import Flask, render_template

from use_case.research.karinahasler.data_collector_test import DataCollector
from use_case.research.karinahasler.map_test import Map
from use_case.research.karinahasler.overlay_test import EarthquakeOverlay, TectonicOverlay

app = Flask(__name__)


@app.route("/")
def index():
    my_map = Map()
    dc = DataCollector()
    dc.filter_radius()
    eqov = EarthquakeOverlay(dc.earthquake_data_clean)
    eqov.apply_overlay(my_map.map)
    tcov = TectonicOverlay()
    tcov.apply_overlay(my_map.map)
    tcov.add_to_layer_control(my_map.map)
    my_map.save_map(os.path.join(app.root_path, "templates", "my_map.html"))
    return render_template("my_map.html")


if __name__ == "__main__":
    app.run(debug=True)

