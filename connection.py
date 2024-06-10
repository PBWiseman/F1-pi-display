import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

time.sleep(2)
ser.write(b"Testing&Hello&Line 3&Line 4&Line 5&Line 6")
time.sleep(2)
response = ""
while response != "Done":
    response = ser.readline().decode('utf-8').strip()
    if response:
        print("Response from Arduino:", response)