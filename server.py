from os import environ
from flask import *
import display
import base64

app = Flask(__name__)

@app.route("/")
def homepage():
    imageString = display.pygameOutputImage(800, 800, 1)
    # image = base64.b64decode(imageString)
    print(imageString)
    return render_template('main.html', imageString=imageString)

app.run(environ.get('PORT'))
# app.run()