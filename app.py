# --Setting up a new computer--
# Install Python and Pip if not installed yet
# Run: py -3 -m venv .venv
# Run: .venv\Scripts\activate
# Run: pip install Flask
# Run: pip install requests
# Run: pip install mvf1

# --Every time you want to run the server--
# Start ngrok and run: ngrok http --domain=fun-sharply-skylark.ngrok-free.app 5000
# Run: flask run
# Open a broadcast stream and a live timing screen in Multiviewer
# If you want to run the server with debug updating run: flask run --debug

# --Documentation--
# Requests: https://pypi.org/project/requests/
# Flask: https://flask.palletsprojects.com/en/3.0.x/
# Multiviewer API: https://mvf1.readthedocs.io/en/latest/MultiViewerForF1.html
# More multiviewer API: https://github.com/RobSpectre/mvf1/
# Yet more multiviewer API: https://pypi.org/project/mvf1/

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