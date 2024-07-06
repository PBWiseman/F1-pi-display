# For setup instructions see README.md

from flask import Flask
from markupsafe import escape
import MVF1API;

app = Flask(__name__)

#Opening a driver cam
@app.route("/players/<number>")
def show_players(number):
    try:
        if MVF1API.openWindow(int(escape(number))):
            return "Player opened"
        else:
            return "Problem opening player"
    except Exception as e:
        return str(e)

#Getting the full live timing
@app.route("/state")
def show_state():
    return MVF1API.getState()

#Current sector times
@app.route("/sectors")
def show_sectors():
    return MVF1API.getSectorTimes()

#Current sector times ordered by time
@app.route("/sectors/ordered")
def show_sectors_ordered():
    return MVF1API.getSectorTimesOrdered()

#Get the top 6 drivers
@app.route("/sectors/top6")
@app.route("/sectors/topsix")
def update_drivers():
    return MVF1API.updateDrivers()