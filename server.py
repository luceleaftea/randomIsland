from os import environ
from flask import *
import display

app = Flask(__name__)

@app.route("/")
def homepage():
    # imageString = display.pygameOutputImage(800, 800, 1)
    colorMap = display.generateColorMapForHTMLCanvas(800, 800)
    return render_template('main.html', colorMap=colorMap)

if __name__ == "__main__":
    app.run(environ.get('PORT'))