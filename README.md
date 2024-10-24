# F1 Pi Display

This is a project that was for originally for the Embedded Systems paper at Otago Polytechnic in Semester 1 2024. I have decided to contunue working on it. Due to life being so busy at the moment I've had very little time to work on it but after my graduation I intend to fully overhaul the code and the design.
It uses a computer streaming MultiViewer and running a Flask app hosted on ngrok, a raspberry pi, an arduino, 3 LCD screens, 6 buttons, and 6 LCD strips of 5 length.
It displays 6 selected drivers with their last 5 minisectors and has buttons to select a driver to view.

Most of this readme is reminders on setup and development for myself. If you are interested in this and need any more info about setting it up, or wish to suggest changes, feel free to send me a message!

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

## Breadboard layout

This is the layout of the breadboards, without the Pi, for Arduino section of the project. The Arduino is connected to the Pi by a USB cable
![Breadboard-Layout](https://github.com/user-attachments/assets/43ecf02f-76b0-43be-b8bd-1d156154dab9)


## Future updates

- 3D printed case
- Soldered circuit board instead of breadboard
- Improved code
  - Customize where windows open
  - Different driver selection logic for races
  - Loading drivers dynamically for each session instead of hardcoding them
  - General optimizations to the code to improve run speed
- More displays
  - Session time
  - LED Matrix display for racing condition flags
  - Laps remaining
- Removing Arduino and making the device Pi only
