from os import environ
from flask import *
import display
import base64

app = Flask(__name__)

@app.route("/")
def homepage():
    imageString = display.pygameOutputImage(800, 800, 1)
    return render_template('main.html', imageString=imageString)

if __name__ == "__main__":
    app.run(environ.get('PORT'))