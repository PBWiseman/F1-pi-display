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
    input = []
    driversToUpdate = [1, 4, 16, 14, 44, 81]
    pos = 0
    for driver in driversToUpdate:
        drivers.setDriverPlace(driver, pos + 1)
        drivers.setDriverScreenPosition(driver, pos)
        drivers.formatDriver(driver)
        input[pos] = drivers.formatDriver(driver)
        pos += 1
    sendToArduino(input)
    screenPos = ""
    while(True):
        try:
            screenPos = ser.readline().decode('utf-8').strip()
            if screenPos:
                driverNum = drivers.getDriverNumber(screenPos)
                if driverNum:
                    requests.get("http://fun-sharply-skylark.ngrok-free.app/players/" + driverNum, timeout=3)
                screenPos = ""
                driverNum = ""
                #wait for 2 seconds to not spam the computer with requests
                time.sleep(2)
        except:
            driverNum = ""


def sendToArduino(input):
    for line in input:
        output = line + "&"
        ser.write(output.encode())
    time.sleep(2)
    response = ""
    while response != "Done":
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            if response:
                print("Response from Arduino:", response)


main()