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
BASE_URL = 'https://api.openf1.org/v1/'

def main():
    remote = MultiViewerForF1()
    for player in remote.players:
        print(player.state)


# def main():
#     payload = {'meeting_key' : 'latest', 'session_type': 'Qualifying'} #Getting the latest qualifying
#     meeting = get_request(dict['me'], {'year' : '2024'})
#     print(meeting)
#     try:
#         quals = get_request(dict['se'], payload)
#         print('Qualifying:', quals)
#         session_key = quals[0]['session_key']
#         payload = {'meeting_key' : 'latest', 'session_key': session_key, 'driver_number' : 16}
#         r = get_request(dict['la'], payload)
#         for lap in r:
#             print('\n')
#             if lap['is_pit_out_lap'] == 1:
#                 print('Pit out lap')
#             elif not lap['segments_sector_3']: #If the last sector is empty it is a pit in lap
#                 print('Pit in lap')
#             else:
#                 sector_print(lap['segments_sector_1'], 1)
#                 print('Time:', lap['duration_sector_1'])
#                 sector_print(lap['segments_sector_2'], 2)
#                 print('Time:', lap['duration_sector_2'])
#                 sector_print(lap['segments_sector_3'], 3)
#                 print('Time:', lap['duration_sector_3'])
#                 print('Lap time:', lap['lap_duration'])
#     except:
#         print('Error')

# #Function to loop through a sector
# def sector_print(sector, sector_number):
#     print ('Sector', sector_number, ':')
#     s = ''
#     for i in sector:
#         s += section_code(i) + ', '
#     s = s.rstrip(', ')
#     print(s)



# #Function to convert section codes to colours
# def section_code(code):
#     match code:
#         case 2048:
#             return 'Y'
#         case 2049:
#             return 'G'
#         case 2051:
#             return 'P'
#         case 0:
#             return 'N/A'
#         case _:
#             return 'N/A'

# # Function to get request from the API
# def get_request(endpoint, payload, time = 10):
#     try:
#         r = requests.get(BASE_URL + endpoint, params=payload, timeout = time)
#         if r:
#             return r.json()
#         else :
#             print('Empty Response')
#     except requests.exceptions.Timeout:
#         print('Timeout error')
#     except requests.exceptions.TooManyRedirects:
#         print('Too many redirects')
#     except requests.exceptions.RequestException as e:
#         print('Request exception:', e)
#     except:
#         print('Unknown error: ', r.status_code)

main()