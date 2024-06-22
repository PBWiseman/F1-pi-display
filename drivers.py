drivers = [
    {'driver_number': 1, 'driver_tla': 'VER', 'team_tla': 'RBR', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 2, 'driver_tla': 'SAR', 'team_tla': 'WIL', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 3, 'driver_tla': 'RIC', 'team_tla': 'VRB', 'screen_position': None, 'place': None, 'minisectors': []},
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
    {'driver_number': 31, 'driver_tla': 'OCO', 'team_tla': 'ALP', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 44, 'driver_tla': 'HAM', 'team_tla': 'MER', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 55, 'driver_tla': 'SAI', 'team_tla': 'FER', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 63, 'driver_tla': 'RUS', 'team_tla': 'MER', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 77, 'driver_tla': 'BOT', 'team_tla': 'SAU', 'screen_position': None, 'place': None, 'minisectors': []},
    {'driver_number': 81, 'driver_tla': 'PIA', 'team_tla': 'MCL', 'screen_position': None, 'place': None, 'minisectors': []}
]

def getDriverNumber(screen_position):
    for driver in drivers:
        if driver['screen_position'] == screen_position:
            return driver['driver_number']
    return None

def formatDriver(driver_number):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            place_str = str(driver['place']) if driver['place'] is not None else ''
            return f"P{place_str.ljust(2)} - {driver['team_tla']} - {driver['driver_tla']}"
    return None

def getDriverTLA(driver_number):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            return driver['driver_tla']
    return None
    
def setTopSix(driversToUpdate):
    try:
        # Create a list of available screen positions
        available_positions = [0, 1, 2, 3, 4, 5]
        driverNumbers = [driver['driver_number'] for driver in driversToUpdate]
        
        # Reset screen positions and minisectors for all drivers
        for driverStored in drivers:
            driverStored['place'] = None
            driverStored['minisectors'] = []
            if driverStored['driver_number'] not in driverNumbers:
                driverStored['screen_position'] = None
            else:
                if driverStored['screen_position'] in available_positions:
                    available_positions.remove(driverStored['screen_position'])

        # Update drivers with new data
        for driver in driversToUpdate:
            driver_number = driver['driver_number']
            for driverStored in drivers:
                if driverStored['driver_number'] == driver_number:
                    driverStored['place'] = driver['position']
                    driverStored['minisectors'] = [convertSectorCodes(minis) for minis in driver['sectors']]
                    if driverStored['screen_position'] is None:
                        driverStored['screen_position'] = available_positions.pop(0)
        return True
    except Exception as e:
        print(e)
        return False
    
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
        
def getTopSix():
    output = ["", "", "", "", "", ""]
    for driver in drivers:
        if driver['screen_position'] is not None:
            output[driver['screen_position']] = formatDriver(driver['driver_number']) + "%"
            output[driver['screen_position']] += "".join(driver['minisectors'])
            output[driver['screen_position']] += "&"
    return output
