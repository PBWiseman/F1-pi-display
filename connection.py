import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

time.sleep(2)
ser.write(b'Hello from Raspberry Pi\n')
time.sleep(2)
response = ser.readline().decode('utf-8').strip()
if response:
    print("Response from Arduino:", response)