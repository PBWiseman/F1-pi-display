import serial
import time
import requests
import drivers
import threading

sending = False

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

def main():
    threading.Thread(target=run_Drivers_on_timer).start()
    waitForInput()

#Runs every second in the background to get the top 6 drivers
def run_Drivers_on_timer():
    while True:
        getDrivers()
        sendToArduino(drivers.getTopSix())
        time.sleep(5)

def getDrivers():
    try:
        response = requests.get("http://fun-sharply-skylark.ngrok-free.app/sectors/topsix", timeout=5)
        drivers.setTopSix(response.json())
        return True
    except Exception as e:
        print(e)
        return False


def sendToArduino(driversToUpdate):
    global sending
    sending = True
    for driver in driversToUpdate:
        print(driver)
        ser.write(driver.encode())
        time.sleep(.1)
    ser.write("@".encode())
    time.sleep(2)
    response = ""
    while response != "Done":
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            if response:
                print("Response Arduino:", response)
    sending = False

def waitForInput():
    screenPos = ""
    while(True):
        if not sending:
            try:
                screenPos = ser.readline().decode('utf-8').strip()
                if screenPos != "":
                    driverNum = drivers.getDriverNumber(str(screenPos))
                    if driverNum != "":
                        requests.get(f"http://fun-sharply-skylark.ngrok-free.app/players/{driverNum}", timeout=10)
                    screenPos = ""
                    driverNum = ""
                    #wait for 2 seconds to not spam the computer with requests
                    time.sleep(2)
            except Exception as e:
                print(e)
                driverNum = ""
                screenPos = ""

main()