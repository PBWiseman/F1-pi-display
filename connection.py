import serial
import time
#If the arduino is plugged into a new port the /tty needs to change. Can check it when selecting ports on the arduino ide
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)


def main():
    input = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5", "Line 6"]
    sendToArduino(input)
    driverNum = ""
    while(True):
            driverNum = ser.readline().decode('utf-8').strip()
            if driverNum:
                print("Response from Arduino:", driverNum)
                driverNum = ""


def sendToArduino(input):
    for line in input:
        output = line + "&"
        #print(output)
        #For some reason if I do this there is an decoding error on the response but not if I do b"test".
        ser.write(output.encode())
    time.sleep(2)
    response = ""
    while response != "Done":
        if ser.in_waiting > 0:
            print(ser.readline())
            response = ser.readline().decode('utf-8').strip()
            if response:
                print("Response from Arduino:", response)


main()