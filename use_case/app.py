from flask import Flask, render_template
import os

from use_case.data_collector import DataCollector
from use_case.earthquake import Earthquake

app = Flask(__name__)

picFolder = os.path.join('static', 'images')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

"""
@app.route("/")
def index():
    logo_hsd = os.path.join(app.config['UPLOAD_FOLDER'], 'HSD_Logo.png')
    return render_template("index.html", user_image=logo_hsd)
"""

@app.route("/map")
def draw_map():
    #dc = DataCollector()
    #eq = Earthquake(dc.earthquake_data_clean)
    return render_template("earthquakes.html")

if __name__ == "__main__":
    app.run(debug=True)

