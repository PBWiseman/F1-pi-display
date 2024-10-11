#Current driver data
drivers = [
    {'driver_number': 1, 'driver_tla': 'VER', 'team_tla': 'RBR', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 4, 'driver_tla': 'NOR', 'team_tla': 'MCL', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 10, 'driver_tla': 'GAS', 'team_tla': 'ALP', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 11, 'driver_tla': 'PER', 'team_tla': 'RBR', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 14, 'driver_tla': 'ALO', 'team_tla': 'AMR', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 16, 'driver_tla': 'LEC', 'team_tla': 'FER', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 18, 'driver_tla': 'STR', 'team_tla': 'AMR', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 20, 'driver_tla': 'MAG', 'team_tla': 'HAS', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 22, 'driver_tla': 'TSU', 'team_tla': 'VRB', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 23, 'driver_tla': 'ALB', 'team_tla': 'WIL', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 24, 'driver_tla': 'ZHO', 'team_tla': 'SAU', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 27, 'driver_tla': 'HUL', 'team_tla': 'HAS', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 30, 'driver_tla': 'LAW', 'team_tla': 'VRB', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 31, 'driver_tla': 'OCO', 'team_tla': 'ALP', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 43, 'driver_tla': 'COL', 'team_tla': 'WIL', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 44, 'driver_tla': 'HAM', 'team_tla': 'MER', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 55, 'driver_tla': 'SAI', 'team_tla': 'FER', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 63, 'driver_tla': 'RUS', 'team_tla': 'MER', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 77, 'driver_tla': 'BOT', 'team_tla': 'SAU', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 81, 'driver_tla': 'PIA', 'team_tla': 'MCL', 'screen_position': None, 'place': None, 'minisectors': []}
]

#When given a screen position returns the driver number on that position
def getDriverNumber(screen_position):
    for driver in drivers:
        if driver['screen_position'] is not None:
            if driver['screen_position'] == int(screen_position):
                return driver['driver_number']
    return None

#Formats the driver place, team tla, and driver tla and returns it when given the driver number
def formatDriver(driver_number):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            place_str = str(driver['place']) if driver['place'] is not None else ''
            return f"P{place_str.ljust(2)} - {driver['team_tla']} - {driver['driver_tla']}"
    return None

#Returns the drivers three letter code when given a driver number
def getDriverTLA(driver_number):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            return driver['driver_tla']
    return None
    
def setTopSix(driversToUpdate):
    try:
        # Create a list of available screen positions
        available_positions = [0, 1, 2, 3, 4, 5]
        #Getting a list of the non zero driver number
        driverNumbers = [driver['driver_number'] for driver in driversToUpdate if driver['driver_number'] != 0]

        # Reset screen positions and minisectors for all drivers
        for driverStored in drivers:
            driverStored['place'] = None
            driverStored['minisectors'] = []
            #If the driver isn't in the new data then remove it's screen position
            if driverStored['driver_number'] not in driverNumbers:
                driverStored['screen_position'] = None
            else:
                #If it is then remove it's screen position from the free ones.
                if driverStored['screen_position'] in available_positions:
                    available_positions.remove(driverStored['screen_position'])

        # Update drivers with new data
        for driver in driversToUpdate:
            driver_number = driver['driver_number']
            if driver_number == 0:
                continue  # Skip blank drivers
            for driverStored in drivers:
                if driverStored['driver_number'] == driver_number:
                    driverStored['place'] = driver['position']
                    #Converting the minisector number codes to the correct letters
                    driverStored['minisectors'] = [convertSectorCodes(minis) for minis in driver['sectors']]
                    #If the driver doesnt already have a screen position then give it one from the list of free ones
                    if driverStored['screen_position'] is None:
                        driverStored['screen_position'] = available_positions.pop(0)
        return True
    except Exception as e:
        print(e)
        return False
    
    #This converts the codes to a letter than is easier to send the to the arduino
def convertSectorCodes(minisector):
    match minisector:
        case 2048: #Yellow
            return 'Y'
        case 2049: #Green
            return 'G'
        case 2051: #Purple
            return 'P'
        case 2052 | 2068: #Stopped
            return 'R' 
        case 2064: #Blue
            return 'B'
        case _: #Unknown
            return 'W'
        
#Returns the 6 drivers with screen positions and need to be sent to the arduino
def getTopSix():
    output = ["", "", "", "", "", ""]
    for driver in drivers:
        if driver['screen_position'] is None:
            continue
        output[driver['screen_position']] = formatDriver(driver['driver_number']) + "%"
        output[driver['screen_position']] += "".join(driver['minisectors'])
        output[driver['screen_position']] += "&"
    
    # Remove all empty strings
    output = [item for item in output if item != ""]
    #I am adding empty strings to 6 positions and then removing them after so that the order of screen positions is kept if there aren't blank strings
    return output
