# F1 Pi Display

This is a project for the Embedded Systems paper at Otago Polytechnic in Semester 2 2024.
It uses a computer streaming MultiViewer and running a Flask app hosted on ngrok, a raspberry pi, an arduino, 3 LCD screens, 6 buttons, and 6 LCD strips of 5 length.
It displays 6 selected drivers with their last 5 minisectors and has buttons to select a driver to view.

## Setting up a new computer

- Install Python and Pip if not installed yet
- Run: py -3 -m venv .venv
- Run: .venv\Scripts\activate
- Run: pip install Flask
- Run: pip install requests
- Run: pip install mvf1

## Every time you want to run the server

- Start ngrok and run: ngrok http --domain=fun-sharply-skylark.ngrok-free.app 5000
- Run: flask run
- Open a broadcast stream and a live timing screen in Multiviewer
- If you want to run the server with debug updating run: flask run --debug

## Documentation

Requests: <https://pypi.org/project/requests/>
Flask: <https://flask.palletsprojects.com/en/3.0.x/>
Multiviewer API: <https://mvf1.readthedocs.io/en/latest/MultiViewerForF1.html>

## Future updates

- 3D printed case
- Soldered circuit board
- Improved code
  - Customize where windows open
  - Different driver selection logic for races
  - Loading drivers to account for new drivers or FP1 changes
- More displays
  - Session time
  - LED Matrix display for racing condition flags
  - Laps remaining
- Removing Arduino
