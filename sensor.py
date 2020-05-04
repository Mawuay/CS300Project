import RPi.GPIO as GPIO
import time
from time import sleep
import Adafruit_MCP3008
# import Adafruit_DHT
import dht11

# dhtDevice = adafruit_dht.DHT11(pin = D18)
# initialize GPIO
CLK = 25
MISO = 24
MOSI = 23
CS = 18
PIR = 18
LED = 4
DELAY = 1.0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # Use BCM numbers
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)

a2d = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
print('Press Ctrl-C to quit...')

# # read data using pin 14
# instance = Adafruit_DHT.DHT11(board.D14)
# result = instance.read()

# if result.is_valid():
#     print("Temperature: %-3.1f C" % result.temperature)
#     print("Humidity: %-3.1f %%" % result.humidity)
# else:
#     print("Error: %d" % result.error_code)

motion_state = 0
try:
    while True:
        value = a2d.read_adc(0)
        print('A/D input channel 0 = ', value)
        sleep(0.1)
        if GPIO.input(PIR) != motion_state:
            motion_state = GPIO.input(PIR)
            print("motion =", motion_state)
        time.sleep(DELAY)
        	

except KeyboardInterrupt:
	print("Done")
	GPIO.cleanup()
