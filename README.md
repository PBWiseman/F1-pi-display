# F1-pi-display
F1 qualifying times display for Raspberry Pi

--Setting up a new computer--
Install Python and Pip if not installed yet
Run: py -3 -m venv .venv
Run: .venv\Scripts\activate
Run: pip install Flask
Run: pip install requests
Run: pip install mvf1

--Every time you want to run the server--
Start ngrok and run: ngrok http --domain=fun-sharply-skylark.ngrok-free.app 5000
Run: flask run
Open a broadcast stream and a live timing screen in Multiviewer
If you want to run the server with debug updating run: flask run --debug

--Documentation--
Requests: https://pypi.org/project/requests/
Flask: https://flask.palletsprojects.com/en/3.0.x/
Multiviewer API: https://mvf1.readthedocs.io/en/latest/MultiViewerForF1.html
More multiviewer API: https://github.com/RobSpectre/mvf1/
Yet more multiviewer API: https://pypi.org/project/mvf1/