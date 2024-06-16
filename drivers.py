drivers = [
    {'driver_number': "1", 'driver_name': 'Max Verstappen', 'driver_tla': 'VER', 'team_name': 'Red Bull Racing', 'team_tla': 'RBR', 'screen_position': '', 'place': ''},
    {'driver_number': "2", 'driver_name': 'Logan Sargeant', 'driver_tla': 'SAR', 'team_name': 'Williams', 'team_tla': 'WIL', 'screen_position': '', 'place': ''},
    {'driver_number': "3", 'driver_name': 'Daniel Ricciardo', 'driver_tla': 'RIC', 'team_name': 'Visa Cash App Racing Bulls', 'team_tla': 'VRB', 'screen_position': '', 'place': ''},
    {'driver_number': "4", 'driver_name': 'Lando Norris', 'driver_tla': 'NOR', 'team_name': 'McLaren', 'team_tla': 'MCL', 'screen_position': '', 'place': ''},
    {'driver_number': "10", 'driver_name': 'Pierre Gasly', 'driver_tla': 'GAS', 'team_name': 'Alpine', 'team_tla': 'ALP', 'screen_position': '', 'place': ''},
    {'driver_number': "11", 'driver_name': 'Sergio Perez', 'driver_tla': 'PER', 'team_name': 'Red Bull Racing', 'team_tla': 'RBR', 'screen_position': '', 'place': ''},
    {'driver_number': "14", 'driver_name': 'Fernando Alonso', 'driver_tla': 'ALO', 'team_name': 'Aston Martin', 'team_tla': 'AMR', 'screen_position': '', 'place': ''},
    {'driver_number': "16", 'driver_name': 'Charles Leclerc', 'driver_tla': 'LEC', 'team_name': 'Ferrari', 'team_tla': 'FER', 'screen_position': '', 'place': ''},
    {'driver_number': "18", 'driver_name': 'Lance Stroll', 'driver_tla': 'STR', 'team_name': 'Aston Martin', 'team_tla': 'AMR', 'screen_position': '', 'place': ''},
    {'driver_number': "20", 'driver_name': 'Kevin Magnussen', 'driver_tla': 'MAG', 'team_name': 'Haas', 'team_tla': 'HAS', 'screen_position': '', 'place': ''},
    {'driver_number': "22", 'driver_name': 'Yuki Tsunoda', 'driver_tla': 'TSU', 'team_name': 'Visa Cash App Racing Bulls', 'team_tla': 'VRB', 'screen_position': '', 'place': ''},
    {'driver_number': "23", 'driver_name': 'Alex Albon', 'driver_tla': 'ALB', 'team_name': 'Williams', 'team_tla': 'WIL', 'screen_position': '', 'place': ''},
    {'driver_number': "24", 'driver_name': 'Zhou Guanyu', 'driver_tla': 'ZHO', 'team_name': 'Kick Sauber', 'team_tla': 'SAU', 'screen_position': '', 'place': ''},
    {'driver_number': "27", 'driver_name': 'Nico Hulkenberg', 'driver_tla': 'HUL', 'team_name': 'Haas', 'team_tla': 'HAS', 'screen_position': '', 'place': ''},
    {'driver_number': "31", 'driver_name': 'Esteban Ocon', 'driver_tla': 'OCO', 'team_name': 'Alpine', 'team_tla': 'ALP', 'screen_position': '', 'place': ''},
    {'driver_number': "44", 'driver_name': 'Lewis Hamilton', 'driver_tla': 'HAM', 'team_name': 'Mercedes', 'team_tla': 'MER', 'screen_position': '', 'place': ''},
    {'driver_number': "55", 'driver_name': 'Carlos Sainz Jr', 'driver_tla': 'SAI', 'team_name': 'Ferrari', 'team_tla': 'FER', 'screen_position': '', 'place': ''},
    {'driver_number': "63", 'driver_name': 'George Russell', 'driver_tla': 'RUS', 'team_name': 'Mercedes', 'team_tla': 'MER', 'screen_position': '', 'place': ''},
    {'driver_number': "77", 'driver_name': 'Valtteri Bottas', 'driver_tla': 'BOT', 'team_name': 'Kick Sauber', 'team_tla': 'SAU', 'screen_position': '', 'place': ''},
    {'driver_number': "81", 'driver_name': 'Oscar Piastri', 'driver_tla': 'PIA', 'team_name': 'McLaren', 'team_tla': 'MCL', 'screen_position': '', 'place': ''}
]



def getDriverNumber(screen_position):
    for driver in drivers:
        if driver['screen_position'] == screen_position:
            return driver['driver_number']
    return None

def formatDriver(driver_number):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            return f"P{str(driver['place']).ljust(2)} - {driver['team_tla']} - {driver['driver_tla']}"
    return None

def setDriverPlace(driver_number, place):
    for driver in drivers:
        if driver['driver_number'] == str(driver_number):
            driver['place'] = place
            return True
    return False

def setDriverScreenPosition(driver_number, screen_position):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            driver['screen_position'] = str(screen_position)
            return True
    return False

def getDriverTLA(driver_number):
    for driver in drivers:
        if driver['driver_number'] == driver_number:
            return driver['driver_tla']
    return None