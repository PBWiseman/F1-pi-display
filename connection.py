import serial
import time
import requests
import drivers
import threading

ser = None

def main():
    #Connects to the arduino then starts the data fetching and waiting for a response from the arduino
    connect()
    threading.Thread(target=run_Drivers_on_timer).start()
    threading.Thread(target=waitForInput).start()

#Gets the port that the arduino connects on. It changes with no apparent reason so I have a double try except block to test both options.
def connect():
    global ser
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        print("Connected on port /dev/ttyACM0")
        time.sleep(2)
    except:
        try:
            ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
            print("Connected on port /dev/ttyACM1")
            time.sleep(2)
        except:
            print("Error: No port found")



#Runs repeatedly to get the top 6 drivers and send them to the arduino
def run_Drivers_on_timer():
    while True:
        if not getDrivers():
            print("Web server not online")
        #If the connection to the arduino isn't working it will try to reselect the port
        if not sendToArduino(drivers.getTopSix()):
            print("Arduino not connected")
            connect()
        time.sleep(1)

#Gets the top 6 drivers from the ngrok site the computer is hosting
def getDrivers():
    try:
        response = requests.get("http://fun-sharply-skylark.ngrok-free.app/sectors/topsix", timeout=5)
        drivers.setTopSix(response.json())
        return True
    except Exception as e:
        print(e)
        return False


def sendToArduino(driversToUpdate):
    try:
        for driver in driversToUpdate:
            print(driver)
            ser.write(driver.encode())
            time.sleep(.1)
        ser.write("@".encode())
        return True
    except Exception as e:
        print(e)
        return False

def waitForInput():
    screenPos = ""
    while(True):
        try:
            screenPos = ser.readline().decode('utf-8').strip()
            if screenPos != "":
                driverNum = drivers.getDriverNumber(screenPos)
                if driverNum != None:
                    res = requests.get(f"http://fun-sharply-skylark.ngrok-free.app/players/{driverNum}", timeout=30)
                    print(res)
                ser.readline().decode('utf-8').strip() #I want to clear out the backlog after it opens so the server isnt flooded by requests
                screenPos = ""
                driverNum = ""
        except Exception as e:
            print(e)
            driverNum = ""
            screenPos = ""

main()