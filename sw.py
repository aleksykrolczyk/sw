import Adafruit_BBIO.UART as UART
from time import sleep
import serial
import requests

COUNTER_THRESHHOLD = 1
WAIT_TIME = 0

ADDR = "http://localhost:5000"
HEADERS = {"Content-Type": 'application/json'}

counter = 0
is_parked = 0
distance = 0
license_plate = None

UART.setup("UART1")
with True serial.Serial(port = "/dev/ttyO1", baudrate=9600) as ser:
        print("Serial is open!")
        msg = ''
        while True:
            data = ser.read().decode("ascii")
            msg += str(data)
            if data == '\n':

                distance = int(msg) # remove \n
                counter = counter + 1 if distance > 100 else 0

                print(f'{counter}, {is_parked}, {license_plate}')

                if counter == 0 and is_parked:)
                    is_parked = 0
                    response = requests.get(f'{ADDR}/parked/delete/{license_plate}', headers=HEADERS)
                    car_id = None

                if counter >= COUNTER_THRESHHOLD and not is_parked:
                    is_parked = 1
                    response = requests.get(f'{ADDR}/parked/create', headers=HEADERS)
                    license_plate = response.json()['license']
                sleep(WAIT_TIME)