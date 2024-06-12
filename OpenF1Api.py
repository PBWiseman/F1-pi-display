# When on a new computer: pip install requests
# If not try Run python -m pip install requests
# If this doesn't work check https://pypi.org/project/requests/
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']} Can use a list of items as a value
# https://openf1.org/ for more information on the API
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
import requests
BASE_URL = 'https://api.openf1.org/v1/'

dict = {}
dict['ca'] = 'car_data'
dict['dr'] = 'drivers'
dict['la'] = 'laps'
dict['lo'] = 'location'
dict['me'] = 'meetings'
dict['pi'] = 'pit'
dict['po'] = 'position'
dict['ra'] = 'race_control'
dict['se'] = 'sessions'
dict['st'] = 'stints'
dict['te'] = 'team_radio'
dict['we'] = 'weather'


def main():
    print('Hello World')
    # payload = {'session_name': 'Qualifying'}
    # quals = get_request(dict['se'], payload)
    # for qual in quals:
    #     payload = {'session_key' : qual, 'lap_number': 2, 'driver_number': 1}
    #     lap = get_request(dict['la'], payload)
    #     print(qual['circuit_short_name'])
    #     print(lap)
        # sector_print(lap['segments_sector_1'], 1)
        # sector_print(lap['segments_sector_2'], 2)
        # sector_print(lap['segments_sector_3'], 3)
    # payload = {'meeting_key' : 'latest', 'session_type': 'Qualifying'} #Getting the latest qualifying
    # try:
    #     quals = get_request(dict['se'], payload)
    #     print('Qualifying:', quals)
    #     session_key = quals[0]['session_key']
    #     payload = {'meeting_key' : 'latest', 'session_key': session_key, 'driver_number' : 1}
    #     r = get_request(dict['la'], payload)
    #     for lap in r:
    #         if lap['is_pit_out_lap'] == 1:
    #             print('Pit out lap')
    #         else:
    #             lap_purples = lap['segments_sector_1'].count(2051) + lap['segments_sector_2'].count(2051) + lap['segments_sector_3'].count(2051)
    #             lap_purples = "Lap Purples: " + str(lap_purples)
    #             print(lap_purples)
    #             #print(lap['segments_sector_1'].count(2051))
    #             #print(lap['segments_sector_2'].count(2051))
    #             #print(lap['segments_sector_3'].count(2051))
    #             # sector_print(lap['segments_sector_1'], 1)
    #             # print('Time:', lap['duration_sector_1'])
    #             # sector_print(lap['segments_sector_2'], 2)
    #             # print('Time:', lap['duration_sector_2'])
    #             # sector_print(lap['segments_sector_3'], 3)
    #             # print('Time:', lap['duration_sector_3'])
    #             # print('Lap time:', lap['lap_duration'])
    # except:
    #     print('Error')

def get_driver(number):
    payload = {'driver_number' : number}
    driver = get_request(dict['dr'], payload)
    return driver

#Function to loop through a sector
def sector_print(sector, sector_number):
    print ('Sector', sector_number, ':')
    s = ''
    for i in sector:
        s += section_code(i) + ', '
    s = s.rstrip(', ')
    print(s)



#Function to convert section codes to colours
def section_code(code):
    match code:
        case 2048:
            return 'Y'
        case 2049:
            return 'G'
        case 2051:
            return 'P'
        case 0:
            return 'N/A'
        case _:
            return 'N/A'

# Function to get request from the API
def get_request(endpoint, payload, time = 10):
    try:
        r = requests.get(BASE_URL + endpoint, params=payload, timeout = time)
        if r:
            if r.json():
                return r.json()
            else:
                print('Empty JSON')
        else :
            print('Empty Response')
    except requests.exceptions.Timeout:
        print('Timeout error')
    except requests.exceptions.TooManyRedirects:
        print('Too many redirects')
    except requests.exceptions.RequestException as e:
        print('Request exception:', e)
    except:
        print('Unknown error: ', r.status_code)

main()