import os

from flask import Flask, render_template, request
from location_resolver import LocationResolver
from monitor import Monitor

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

    total_filtered = input.perform_earthquake_analytics(location=[new_location.latitude, new_location.longitude], radius=radius)[0]
    minor_filtered = input.perform_earthquake_analytics(location=[new_location.latitude, new_location.longitude], radius=radius)[1]
    moderate_filtered = input.perform_earthquake_analytics(location=[new_location.latitude, new_location.longitude], radius=radius)[2]
    strong_filtered = input.perform_earthquake_analytics(location=[new_location.latitude, new_location.longitude], radius=radius)[3]
    closest_filtered = input.perform_earthquake_analytics(location=[new_location.latitude, new_location.longitude], radius=radius)[4]
    strongest_worldwide = input.perform_earthquake_analytics(location=[new_location.latitude, new_location.longitude], radius=radius)[11]

    refresh = request.args.get('refresh', default=1000, type=int)

    return render_template("bootstrap.html", location=new_location_text, radius=radius, refresh=refresh, total_filtered=total_filtered,
                           minor_filtered=minor_filtered, moderate_filtered=moderate_filtered, strong_filtered=strong_filtered,
                           closest_filtered=closest_filtered, strongest_worldwide=strongest_worldwide)


@app.route('/map')
def map():
    return render_template('my_map.html')


@app.route('/manual')
def manual():
    return render_template('manual.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


if __name__ == "__main__":
    app.run(debug=True)

