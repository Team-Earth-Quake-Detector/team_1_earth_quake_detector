from flask import Flask, render_template
import os

from use_case.data_collector import DataCollector
from use_case.earthquake import Earthquake

app = Flask(__name__)

@app.route("/map")
def draw_map():
    dc = DataCollector()
    eq = Earthquake(dc.earthquake_data_clean)
    sm =

@app.route("/")
def index():
    return render_template("earthquakes.html")

if __name__ == "__main__":
    app.run(debug=True)

