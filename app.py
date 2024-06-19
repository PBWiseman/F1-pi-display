#pip install Flask
#py -3 -m venv .venv
#.venv\Scripts\activate
#for debugging
#flask run --debug
#for connection to pi that I can edit. without debug when I actually run it
#Open ngrok and run: ngrok http --domain=fun-sharply-skylark.ngrok-free.app 5000
from flask import Flask
from markupsafe import escape
import MVF1API;

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route("/driver/<number>")
# def show_driver(number):
#     return OpenF1Api.get_driver(escape(number))

@app.route("/players/<number>")
def show_players(number):
    try:
        if MVF1API.openWindow(int(escape(number))):
            return "Player opened"
        else:
            return "Problem opening player"
    except Exception as e:
        return str(e)
    
@app.route("/state")
def show_state():
    return MVF1API.getState()

@app.route("/sectors")
def show_sectors():
    return MVF1API.getSectorTimes()

@app.route("/sectors/ordered")
def show_sectors_ordered():
    return MVF1API.getSectorTimesOrdered()

@app.route("/sectors/top6")
@app.route("/sectors/topsix")
def update_drivers():
    return MVF1API.updateDrivers()