import serial, time

ser = serial.Serial('/dev/ttyACM7', 9600)


def requestDistance():
    request = '1'
    ser.write(request)
    while True:
        try:
            time.sleep(0.025)
            distance = ser.readline()
            return distance
        except:
            pass
    time.sleep(0.025)

while True:
    distance = requestDistance()
    print distance
