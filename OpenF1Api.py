import requests
BASE_URL = 'https://api.openf1.org/v1/'
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']} Can use a list of items as a value
# https://openf1.org/ for more information on the API
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
    payload = {'meeting_key' : 'latest', 'session_type': 'Qualifying'}
    r = get_request(dict['se'], payload)
    session_key = r[-1]['session_key']
    payload = {'meeting_key' : 'latest', 'session_key': session_key, 'driver_number' : 1, 'is_pit_out_lap' : 'false'}
    r = get_request(dict['la'], payload)
    latest_lap = r[-5] #to -2 for testing as -1 is giving me crap
    print(latest_lap)
    sector_print(latest_lap['segments_sector_1'], 1)
    sector_print(latest_lap['segments_sector_2'], 2)
    sector_print(latest_lap['segments_sector_3'], 3)

#Function to loop through a sector
def sector_print(sector, sector_number):
    print ('Sector', sector_number, ':')
    for i in sector:
        print(section_code(i))



#Function to convert section codes to colours
def section_code(code):
    match code:
        case 2048:
            return 'Yellow'
        case 2049:
            return 'Green'
        case 2051:
            return 'Purple'
        case 0:
            return 'Not Available'
        case _:
            return 'Unknown: ' + str(code)

# Function to get request from the API
def get_request(endpoint, payload, time = 10):
    try:
        r = requests.get(BASE_URL + endpoint, params=payload, timeout = time)
        if r:
            return r.json()
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