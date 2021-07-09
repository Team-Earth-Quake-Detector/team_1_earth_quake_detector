import os

from flask import Flask, render_template

from monitor import Monitor

app = Flask(__name__)


@app.route("/")
def index():
    input = Monitor()
    my_map = input.build_map()
    my_map.save_map(os.path.join(app.root_path, "templates", "my_map.html"))
    #my_map = input.build_map(coordinates=(34.052234, -118.243685), radius=250)
    #my_map.save_map(os.path.join(app.root_path, "templates", "my_map.html"))
    return render_template("index.html", location="TBD", radius="TBD",) # render html


@app.route('/map')
def map():
    return render_template('my_map.html')

if __name__ == "__main__":
    app.run(debug=True)

