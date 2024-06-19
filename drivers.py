drivers = [
    {'driver_number': "1", 'driver_name': 'Max Verstappen', 'driver_tla': 'VER', 'team_name': 'Red Bull Racing', 'team_tla': 'RBR', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "2", 'driver_name': 'Logan Sargeant', 'driver_tla': 'SAR', 'team_name': 'Williams', 'team_tla': 'WIL', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "3", 'driver_name': 'Daniel Ricciardo', 'driver_tla': 'RIC', 'team_name': 'Visa Cash App Racing Bulls', 'team_tla': 'VRB', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "4", 'driver_name': 'Lando Norris', 'driver_tla': 'NOR', 'team_name': 'McLaren', 'team_tla': 'MCL', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "10", 'driver_name': 'Pierre Gasly', 'driver_tla': 'GAS', 'team_name': 'Alpine', 'team_tla': 'ALP', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "11", 'driver_name': 'Sergio Perez', 'driver_tla': 'PER', 'team_name': 'Red Bull Racing', 'team_tla': 'RBR', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "14", 'driver_name': 'Fernando Alonso', 'driver_tla': 'ALO', 'team_name': 'Aston Martin', 'team_tla': 'AMR', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "16", 'driver_name': 'Charles Leclerc', 'driver_tla': 'LEC', 'team_name': 'Ferrari', 'team_tla': 'FER', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "18", 'driver_name': 'Lance Stroll', 'driver_tla': 'STR', 'team_name': 'Aston Martin', 'team_tla': 'AMR', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "20", 'driver_name': 'Kevin Magnussen', 'driver_tla': 'MAG', 'team_name': 'Haas', 'team_tla': 'HAS', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "22", 'driver_name': 'Yuki Tsunoda', 'driver_tla': 'TSU', 'team_name': 'Visa Cash App Racing Bulls', 'team_tla': 'VRB', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "23", 'driver_name': 'Alex Albon', 'driver_tla': 'ALB', 'team_name': 'Williams', 'team_tla': 'WIL', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "24", 'driver_name': 'Zhou Guanyu', 'driver_tla': 'ZHO', 'team_name': 'Kick Sauber', 'team_tla': 'SAU', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "27", 'driver_name': 'Nico Hulkenberg', 'driver_tla': 'HUL', 'team_name': 'Haas', 'team_tla': 'HAS', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "31", 'driver_name': 'Esteban Ocon', 'driver_tla': 'OCO', 'team_name': 'Alpine', 'team_tla': 'ALP', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "44", 'driver_name': 'Lewis Hamilton', 'driver_tla': 'HAM', 'team_name': 'Mercedes', 'team_tla': 'MER', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "55", 'driver_name': 'Carlos Sainz Jr', 'driver_tla': 'SAI', 'team_name': 'Ferrari', 'team_tla': 'FER', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "63", 'driver_name': 'George Russell', 'driver_tla': 'RUS', 'team_name': 'Mercedes', 'team_tla': 'MER', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "77", 'driver_name': 'Valtteri Bottas', 'driver_tla': 'BOT', 'team_name': 'Kick Sauber', 'team_tla': 'SAU', 'screen_position': '', 'place': '', 'minisectors': []},
    {'driver_number': "81", 'driver_name': 'Oscar Piastri', 'driver_tla': 'PIA', 'team_name': 'McLaren', 'team_tla': 'MCL', 'screen_position': '', 'place': '', 'minisectors': []}
]



def getDriverNumber(screen_position):
    for driver in drivers:
        if driver['screen_position'] == screen_position:
            return driver['driver_number']
    return None

def formatDriver(driver_number):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            return {'driver': f"P{str(driver['place']).ljust(2)} - {driver['team_tla']} - {driver['driver_tla']}", 'minisectors': driver['minisectors']}
    return None

def getDriverTLA(driver_number):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            return driver['driver_tla']
    return None
    
def setTopSix(driversToUpdate):
    try:
        # Create a list of available screen positions
        available_positions = {0,1,2,3,4,5}

        # Iterate over the drivers list
        for driverStored in drivers:
            driverStored['place'] = ''
            driverStored['minisectors'] = []
            if driverStored['driver_number'] not in driversToUpdate['driver_number']:
                driverStored['screen_position'] = ''
            else:
                if driverStored['screen_position'] in available_positions:
                    available_positions.remove(driverStored['screen_position'])

        # Iterate over the driversToUpdate list
        for driver in driversToUpdate:
            for driverStored in drivers:
                if driverStored['driver_number'] == driver['driver_number']:
                    driverStored['place'] = driver['position']
                    driverStored['minisectors'] = convertSectorCodes(driver['sectors'])
                    # If a driver doesn't have a screen position or its screen position is not in the available positions, assign it the first available screen position
                    if driverStored['screen_position'] == '' or driverStored['screen_position'] not in available_positions:
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
        case 2052: #Stopped
            return 'R' 
        case 2068: #Stopped
            return 'R' 
        case 2064: #Blue
            return 'B'
        case _: #Unknown
            return 'W'
        
def getTopSix():
    output = [{}, {}, {}, {}, {}, {}]
    i = 0
    for driver in drivers:
        if driver['screen_position'] == '':
            continue
        drivers.formatDriver(driver)
        output[driver['screen_position']] = drivers.formatDriver(driver)
        #needs to add sectors
    return output