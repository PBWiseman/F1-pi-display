#pip install Flask
#py -3 -m venv .venv
#.venv\Scripts\activate
#for debugging
#flask run --debug
#for connection to pi
#Open ngrok and run: ngrok http --domain=fun-sharply-skylark.ngrok-free.app 5000
from flask import Flask
from markupsafe import escape
import MVF1API;
import OpenF1Api;

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