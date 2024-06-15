# When on a new computer: pip install requests
# If not try Run python -m pip install requests
# If this doesn't work check https://pypi.org/project/requests/
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']} Can use a list of items as a value
# 1	    Max Verstappen
# 2	    Logan Sargeant
# 3	    Daniel Ricciardo
# 4	    Lando Norris
# 10	Pierre Gasly
# 11	Sergio Perez
# 14	Fernando Alonso
# 16	Charles Leclerc
# 18	Lance Stroll
# 20	Kevin Magnussen
# 22	Yuki Tsunoda
# 23	Alex Albon
# 24	Zhou Guanyu
# 27	Nico Hulkenberg
# 31	Esteban Ocon
# 44	Lewis Hamilton
# 55	Carlos Sainz Jr
# 63	George Russell
# 77	Valtteri Bottas
# 81	Oscar Piastri
# Driver numbers for testing
# Multiviewer API link https://mvf1.readthedocs.io/en/latest/MultiViewerForF1.html
# pip install mvf1
# https://github.com/RobSpectre/mvf1/issues/2
# https://github.com/RobSpectre/mvf1
# https://pypi.org/project/mvf1/
# https://github.com/f1multiviewer/issue-tracker/issues/337

import requests
from mvf1 import MultiViewerForF1
mvf1 = MultiViewerForF1()

def openWindow(driverNumber):
    players = mvf1.players
    players[0].content_id
    #Take the driverNumber and open the window for that driver
    try:
        mvf1.player_create(content_id = players[0].content_id, driver_number = driverNumber)
    except:
        return False
    return True

#Get all players and see if the requested driver is in the list
def getAllPlayers(driverNumber):
    players = mvf1.players
    for player in players:
        try:
            if player.driver_data["driverNumber"] == driverNumber:
                return True
        except:
            pass
    return False