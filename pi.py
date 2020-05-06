#############################################################################################
# pi.py python script that allows the pi to interface with the arduino.
# Date : 2nd May 2020
# Written by: Daniel Ackuaku, for CS 300 Final Project
# Institution: Calvin University
# Professor: Derek Schuurman
#
# Reads serial data from the sensors on the arduino and stores them in an google sheets
# uses data from the google sheets to detect if the bathroom is occupied or not
# deletes data from teh google sheet after 1 hour
#############################################################################################
from pprint import pprint
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import serial
import time 
import datetime

##########################################################################
# Configuring credentials for the google sheet API
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", SCOPES)
client = gspread.authorize(creds)

# Opening the specific sheets in the google sheets workbook
sheet = client.open("Occupod").sheet1
sheet2 = client.open("Occupod").worksheet('BathroomState')
##########################################################################
# Variable definitions 

countTimer = 0



# Function definition
# Function that reads in serial data, parses it into strings and publishes it to google sheets
def sense_and_record():
	global countTimer
	arduino = serial.Serial("/dev/ttyACM0", 9600) # Reads in the sensor data
	data = arduino.readline().decode() # Decodes that data into a string
	pieces = data.split("\t") # splits the string into the parts of infromation required
	lights = pieces[0]
	temperature = pieces[1]
	humidity = pieces[2]
	motion = pieces[3]
	currentTime = datetime.datetime.now() # sets the currentTime variable to local time
	# Algorithm that detemines if someone is in the bath room and what activity they might be doing based on sensor data & updates the sheet
	if (lights >="20" and humidity >= "50" and temperature >= "20"):
		bathroomState = [currentTime.strftime("%X"), "Occupied - Shower"]
		sheet2.append_row(bathroomState)
	elif int(lights) >= 20 and int(humidity) <= 40 and int(motion) > 0:
		bathroomState = [currentTime.strftime("%X"), "Occupied - Toilet"]
		sheet2.append_row(bathroomState)
	else:
		bathroomState = [currentTime.strftime("%X"), "Vacant"]
		sheet2.append_row(bathroomState)

	appendRow = [currentTime.strftime("%X"), int(lights), float(temperature) , int(humidity) ,int(motion)]
	sheet.append_row(appendRow)
	countTimer = countTimer + 1


# Function that deletes from the sheet after 1 hour of sensing
def delete_and_update():
	global countTimer
	if (countTimer == 360):
		for x in range (2,360):
			sheet.delete_row(x)
			sheet2.delete_row(x)
		countTimer = 0

# Continus loop that reads data from the Arduino sensors 
try:
	print("Welcome you are updating the google sheet.")
	while True:
		sense_and_record()
		delete_and_update()

except KeyboardInterrupt:
	print ("Done")

