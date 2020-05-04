#############################################################################################
# pi.py python script that allows the pi to interface with the arduino.
# Date : 2nd May 2020
# Written by: Daniel Ackuaku, for CS 300 Final Project
# Institution: Calvin University
# Professor: Dereck Schuurman
#
#
# Reads serial data from the sensors on the arduino and stores them in an google sheets
# uses data from the google sheets to detect if the bathroom is occupied or not.
# intercaes with the google home.   
#############################################################################################
from pprint import pprint
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import serial
import time 
import datetime

##########################################################################
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", SCOPES)
client = gspread.authorize(creds)
sheet = client.open("Occupod").sheet1
sheet2 = client.open("Occupod").worksheet('BathroomState')



##########################################################################

try:
	while True:
		arduino = serial.Serial("/dev/ttyACM0", 9600) # make sure you write correct serial Pi -"/dev/ttyACM0" Mac -/dev/cu.usbmodem14101
		data = arduino.readline().decode()
		pieces = data.split("\t")
		lights = pieces[0]
		temperature = pieces[1]
		humidity = pieces[2]
		motion = pieces[3]
		currentTime = datetime.datetime.now()
		# int realtime = currentTime.strftime("%X")
		# print(currentTime.strftime("%X"), lights, temperature, humidity, motion)
		if (lights >="20" and humidity >= "50" and temperature >= "20"):
			bathroomState = [currentTime.strftime("%X"), "Occupied - Shower"]
			sheet2.append_row(bathroomState)
		elif int(lights) >= 20 and int(humidity) <= 40 and int(motion) > 0:
			bathroomState = [currentTime.strftime("%X"), "Occupied - Toilet"]
			sheet2.append_row(bathroomState)
		else:
			bathroomState = [currentTime.strftime("%X"), "Vaccant"]
			sheet2.append_row(bathroomState)

		appendRow = [currentTime.strftime("%X"),int(lights), float(temperature) , (humidity) ,motion]
		sheet.append_row(appendRow)
except KeyboardInterrupt:
	print ("Done")

