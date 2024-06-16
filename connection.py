import serial
import time
import requests
import drivers

try:
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    print("Connected on port /dev/ttyACM1")
    time.sleep(2)
except:
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        print("Connected on port /dev/ttyACM0")
        time.sleep(2)
    except:
        print("Error: No port found")

def main():
    driversToUpdate = ["1", "4", "16", "14", "44", "81"]
    positions = [1, 2, 3, 4, 5, 6]
    getDrivers()
    driversToUpdate = prepDrivers(driversToUpdate, positions)
    sendToArduino(driversToUpdate)
    waitForInput()

def getDrivers():
    response = requests.get("http://fun-sharply-skylark.ngrok-free.app/sectors/topsix", timeout=5)
    print(response.json())
    return response.json()

def prepDrivers(driversToUpdate, positions):
    output = ["", "", "", "", "", ""]
    pos = 0
    for driver in driversToUpdate:
        drivers.setDriverPlace(driver, positions[pos])
        drivers.setDriverScreenPosition(driver, pos)
        drivers.formatDriver(driver)
        output[pos] = drivers.formatDriver(driver)
        pos += 1
    return output

def sendToArduino(driversToUpdate):
    for driver in driversToUpdate:
        output = driver + "&"
        print(output)
        ser.write(output.encode())
        time.sleep(.1)
    ser.write("@".encode())
    time.sleep(2)
    response = ""
    while response != "Done":
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            if response:
                print("Response Arduino:", response)

def waitForInput():
    screenPos = ""
    while(True):
        try:
            screenPos = ser.readline().decode('utf-8').strip()
            if screenPos != "":
                driverNum = drivers.getDriverNumber(str(screenPos))
                if driverNum != "":
                    requests.get("http://fun-sharply-skylark.ngrok-free.app/players/" + driverNum, timeout=10)
                screenPos = ""
                driverNum = ""
                #wait for 2 seconds to not spam the computer with requests
                time.sleep(2)
        except Exception as e:
            print(e)
            driverNum = ""
            screenPos = ""

main()