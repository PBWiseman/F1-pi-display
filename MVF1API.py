#See app.py for instructions on how to run the server
#For if I add a remaining time display: data > liveTimingState > ExtrapolatedClock > Remaining

import requests
import time
import drivers
from mvf1 import MultiViewerForF1
mvf1 = MultiViewerForF1()
createdPlayerID = None
createdPlayer = None

#Opens the window for the inputted driver
def openWindow(driverNumber):
    players = mvf1.players
    #Get the content id that is needed to open a new player
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
                # If accessing the property failed, the window was probably closed manually
                createdPlayer = None
                createdPlayerID = None
            else:
                # If the player is still open, check if it's the correct driver. If not delete it
                if createdPlayer.driver_data["driverNumber"] == driverNumber:
                    return True
                else:
                    createdPlayer.delete()
                    createdPlayer = None
                    createdPlayerID = None
        #Create the player
        #TODO: Make the player inherit the size and position of the last createdPlayer window if one was open
        #TODO: Is it possible to set the window to the top but not always on top?
        response = mvf1.player_create(content_id = contentId, driver_number = driverNumber, fullscreen = True, always_on_top = True)
        createdPlayerID = response['data']['playerCreate']
        #The player takes a variable amount of time to be selectable. This ensures it will be grabbed asap
        retries = 10
        interval = .5
        for _ in range(retries):
            createdPlayer = mvf1.player(createdPlayerID)
            if createdPlayer:
                break
            time.sleep(interval)
        if not createdPlayer:
            raise Exception("Player creation failed after retries.")
        #If you are watching a replay this syncs the player to the commentary window
        mvf1.player_sync_to_commentary()
        return True
    except Exception as e:
        print(str(e))
        return False
    
#Returns the current state of the live timing
def getState():
    return mvf1.live_timing_state

#Updates the top 6 drivers
#TODO: Store data for all drivers?
def updateDrivers():
    sectorTimes = getSectorTimesOrdered()
    if sectorTimes == "Error":
        return sectorTimes
    #Just need the top 6 since I only have 6 slots
    top_6_drivers = sectorTimes[:6]

    #If there is less than 6 drivers then fill the rest with empty data
    while len(top_6_drivers) < 6:
        top_6_drivers.append({
            'driver_number': 0,
            'position': 0,
            'sectors': []
        })
    
    #Just gets the needed information and ignores the rest
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
# Most purple sectors
# Most green sectors
# Most sectors overall
# Since then I have added least blue sectors to the top as well as removing drivers with no sectors or ones that are currently in the pits
# It also only returns the last 5 sectors
def getSectorTimesOrdered():
    times = getSectorTimes()
    if times == "Error":
        return times
    
    driver_sector_info = []

    for driver_number, driver_data in times.items():
        minisector_codes = driver_data['Sectors']
        # Filter out zero sectors
        non_zero_sectors = [code for code in minisector_codes if code != 0]

        #If the driver is not in this stage of the qualifying session or is dnf then skip them
        if not non_zero_sectors:
            continue

        # If the driver is currently in the pits then remove them
        if non_zero_sectors[-1] == 2064:
            continue

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
    sorted_driver_sector_info = sorted(driver_sector_info, key=lambda x: (x['blue_count'], -x['purple_count'], -x['green_count'], -x['total_count']))
    #Removing all but the last 5 sectors
    for driver in sorted_driver_sector_info:
        driver['sectors'] = driver['sectors'][-5:]
    return sorted_driver_sector_info

#Returns the current sector times for all drivers
def getSectorTimes():
    try:
        data = mvf1.live_timing_state
        if data is None:
            return "Error: No timing data available."
        minisector_codes = {}
        #Digs through the data to get the needed data
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