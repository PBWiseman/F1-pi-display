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

#For if I add a remaining time display: data > liveTimingState > ExtrapolatedClock > Remaining

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
    

def getState():
    return mvf1.live_timing_state

def updateDrivers():
    sectorTimes = getSectorTimesOrdered()
    if sectorTimes == "Error":
        return sectorTimes
    #Just need the top 6 since I only have 6 slots
    top_6_drivers = sectorTimes[:6]
    
    top_6_info = []
    for driver in top_6_drivers:
        driver_info = {
            'position': driver['position'],
            'driver_number': int(driver['driver_number']),
            'sectors': driver['sectors']
        }
        top_6_info.append(driver_info)

    return top_6_info



#The sorting method wasn't working well so I asked chatGPT to help. It took many back and forward attempts to get it working so it would take too long to list the exact prompts
#The original request was to order it in the following priority
# Greater than 1 sector
# Least blue sectors
# Most purple sectors
# Most green sectors
# Most sectors overall
def getSectorTimesOrdered():
    times = getSectorTimes()
    if times == "Error":
        return times
    
    driver_sector_info = []

    for driver_number, driver_data in times.items():
        minisector_codes = driver_data['Sectors']
        # Filter out zero sectors
        non_zero_sectors = [code for code in minisector_codes if code != 0]

        # Count purple (2051), green (2049), blue (2064) sectors
        purple_count = non_zero_sectors.count(2051)
        green_count = non_zero_sectors.count(2049)
        blue_count = non_zero_sectors.count(2064)
        total_count = len(non_zero_sectors)

        position = driver_data['Position']

        driver_sector_info.append({
            'driver_number': driver_number,
            'position': position,
            'driver_name': drivers.getDriverTLA(driver_number),
            'purple_count': purple_count,
            'green_count': green_count,
            'blue_count': blue_count,
            'total_count': total_count,
            'sectors': non_zero_sectors
        })

    # Sort driver_sector_info list based on the specified priorities
    sorted_driver_sector_info = sorted(driver_sector_info, key=lambda x: (x['total_count'] == 0, x['blue_count'], -x['purple_count'], -x['green_count'], -x['total_count']))    #Remove all but the 5 most recent sectors
    for driver in sorted_driver_sector_info:
        driver['sectors'] = driver['sectors'][-5:]
    return sorted_driver_sector_info

def getSectorTimes():
    try:
        data = mvf1.live_timing_state
        if data is None:
            return "Error: No timing data available."
        minisector_codes = {}
        for driver_line in data['data']['liveTimingState']['TimingData']['Lines'].values():
            driver_number = driver_line['RacingNumber'] 
            sectors = driver_line['Sectors']
            position = driver_line['Line']
            minisector_codes[driver_number] = {
                'Sectors': [],
                'Position': position
            }
            for sector in sectors:
                segments = sector['Segments']
                for segment in segments:
                    minisector_code = segment['Status']
                    minisector_codes[driver_number]['Sectors'].append(minisector_code)
        return minisector_codes
    except Exception as e:
        print(f"Error fetching sector times: {str(e)}")
        return "Error"