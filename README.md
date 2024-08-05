# F1 Pi Display

This is a project for the Embedded Systems paper at Otago Polytechnic in Semester 1 2024.
It uses a computer streaming MultiViewer and running a Flask app hosted on ngrok, a raspberry pi, an arduino, 3 LCD screens, 6 buttons, and 6 LCD strips of 5 length.
It displays 6 selected drivers with their last 5 minisectors and has buttons to select a driver to view.

Most of this readme is reminders for myself. Not really expecting anyone else to see or be interested in this project but if you are and need any more info about setting it up feel free to send me a message!

## Setting up a new computer

- Install Python, Pip and pipenv (pip install pipenv --user) if not installed yet
- Run: pipenv install
- Run: pipenv shell

## Every time you want to run the server

- Start ngrok and run: ngrok http --domain=fun-sharply-skylark.ngrok-free.app 5000
- Run: flask run
- Open a broadcast stream and a live timing screen in Multiviewer
- If you want to run the server with debug updating run: flask run --debug

## Other notes

- To upgrade a package without committing it to pipenv run: pipenv upgrade -package-
- To update the pipenv with the upgrade run: pipenv update -package-
- To install new packages use pipenv install -package-

## Documentation

- Requests: <https://pypi.org/project/requests/>
- Flask: <https://flask.palletsprojects.com/en/3.0.x/>
- Multiviewer API: <https://mvf1.readthedocs.io/en/latest/MultiViewerForF1.html>

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
