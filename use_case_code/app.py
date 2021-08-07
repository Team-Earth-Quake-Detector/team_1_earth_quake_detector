import os

from flask import Flask, render_template, request
from location_resolver import LocationResolver
from monitor import Monitor
from data_collector import DataCollector

app = Flask(__name__)


@app.route("/")
def index():
    resolver = LocationResolver()
    new_location_text = request.args.get('location', default=resolver.address, type=str)
    new_resolver = LocationResolver(new_location_text)
    new_location = new_resolver.location

    radius = request.args.get('radius', default=250, type=int)

    input = Monitor()
    my_map = input.build_map(coordinates=[new_location.latitude, new_location.longitude], radius=radius)
    my_map.save_map(os.path.join(app.root_path, "templates", "my_map.html"))

    #total = input.test_get_total_filtered_earthquakes(location=[new_location.latitude, new_location.longitude])

    total = input.test_perform_earthquake_analytics(location=[new_location.latitude, new_location.longitude], radius=radius)
    #analytics = DataCollector()
    #total = analytics.get_total_filtered_earthquakes()

    refresh = request.args.get('refresh', default=300, type=int)

    return render_template("bootstrap.html", location=new_location_text, radius=radius, refresh=refresh, total=total) # render html

@app.route('/map')
def map():
    return render_template('my_map.html')

if __name__ == "__main__":
    app.run(debug=True)

