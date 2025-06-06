# F1 Pi Display

This is a project that was for originally for the Embedded Systems paper at Otago Polytechnic in Semester 1 2024. The hardware was dissasembled during my recent move and I currently don't have the money to buy the parts I want to upgrade it. I still intend to resume development on it but at the moment it is not functioning.

The changes to F1TV subscriptions also likely break the driver POV feature if you only have a pro instead of a premium subscription.

The original device used a computer streaming MultiViewer and running a Flask app hosted on ngrok, a raspberry pi, an arduino, 3 LCD screens, 6 buttons, and 6 LCD strips of 5 length.
It displays 6 selected drivers with their last 5 minisectors and has buttons to select a driver to view. I have a list of intended changes below for when I am able to buy new parts and resume development.

Most of this readme is reminders on setup and development for myself. If you are interested in this and want any more info feel free to send me a message!

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
- To update pipenv with new updates run: pipenv update
- To install new packages use pipenv install -package-

## Documentation

- Requests: <https://pypi.org/project/requests/>
- Flask: <https://flask.palletsprojects.com/en/3.0.x/>
- Multiviewer API: <https://mvf1.readthedocs.io/en/latest/MultiViewerForF1.html>

## Breadboard layout

This is the layout of the breadboards, without the Pi, for Arduino section of the project. The Arduino is connected to the Pi by a USB cable
![Breadboard-Layout](https://github.com/user-attachments/assets/43ecf02f-76b0-43be-b8bd-1d156154dab9)

## Future updates

- Remove Arduino and making the device Pi only
- Hardware:
  - 3D printed case
  - Soldered circuit board instead of breadboard
  - Session time display for qualifying
  - Laps remaining display for race
  - LED Matrix display for racing condition flags
  - Better wiring, likely with shift registers
- Software
  - Customize where windows open
  - Windows open with the same dimensions as closed ones
  - Loading drivers dynamically for each session instead of hardcoding them
  - Better driver selection logic, make it more dynamic based on actually meaningful and interesting POVs
  - Seperation of race and qualifying selection logic
  - General optimizations to the code to improve run speed
  - Make it easier to open and run, ideally moving more of the logic from the computer to the Pi
