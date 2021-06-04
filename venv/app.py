from flask import Flask, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static', 'images')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder


@app.route("/")
def index():
    logo_hsd = os.path.join(app.config['UPLOAD_FOLDER'], 'HSD_Logo.png')
    return render_template("test_4.html", user_image=logo_hsd)


@app.route("/index")
def hello():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)
