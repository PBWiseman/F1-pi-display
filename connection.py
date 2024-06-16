import serial
import time
import requests

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
    input = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5", "Line 6"]
    sendToArduino(input)
    driverNum = ""
    while(True):
        try:
            driverNum = ser.readline().decode('utf-8').strip()
            if driverNum:
                requests.get("http://fun-sharply-skylark.ngrok-free.app/players/" + driverNum, timeout=3)
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