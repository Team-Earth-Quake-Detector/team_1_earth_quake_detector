import os

from flask import Flask, render_template

from monitor import Monitor

app = Flask(__name__)


@app.route("/")
def index():
    input = Monitor()
    my_map = input.build_map()
    my_map.save_map(os.path.join(app.root_path, "templates", "my_map.html"))
    return render_template("my_map.html") # render html
    # return my_map._repr_html_() # Extract map only -> Beautiful Soap


if __name__ == "__main__":
    app.run(debug=True)

