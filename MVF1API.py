# When on a new computer: pip install requests
# If not try Run python -m pip install requests
# If this doesn't work check https://pypi.org/project/requests/
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']} Can use a list of items as a value
# Multiviewer API link https://mvf1.readthedocs.io/en/latest/MultiViewerForF1.html
# pip install mvf1
# https://github.com/RobSpectre/mvf1/issues/2
# https://github.com/RobSpectre/mvf1
# https://pypi.org/project/mvf1/
# https://github.com/f1multiviewer/issue-tracker/issues/337

import requests
import time
import drivers
from mvf1 import MultiViewerForF1
mvf1 = MultiViewerForF1()
createdPlayerID = None
createdPlayer = None

def openWindow(driverNumber):
    players = mvf1.players
    contentId = players[0].content_id
    global createdPlayer
    global createdPlayerID
    #Take the driverNumber and open the window for that driver
    try:
        if createdPlayer is not None:
            try:
                # Try to access a property of the player to see if it's still open
                _ = createdPlayer.driver_data
            except Exception:
                # If accessing the property failed, the window was probably closed
                createdPlayer = None
                createdPlayerID = None
            else:
                if createdPlayer.driver_data["driverNumber"] == driverNumber:
                    return True
                else:
                    createdPlayer.delete()
                    createdPlayer = None
                    createdPlayerID = None
        response = mvf1.player_create(content_id = contentId, driver_number = driverNumber, fullscreen = True, always_on_top = True)
        createdPlayerID = response['data']['playerCreate']
        retries = 10
        interval = .5
        for _ in range(retries):
            createdPlayer = mvf1.player(createdPlayerID)
            if createdPlayer:
                break
            time.sleep(interval)
        if not createdPlayer:
            raise Exception("Player creation failed after retries.")
        createdPlayer.set_fullscreen(True)
        mvf1.player_sync_to_commentary()
        return True
    except Exception as e:
        print(str(e))
        return False
    