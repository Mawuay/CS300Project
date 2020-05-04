#############################################################################################
# pi.py python script that allows the pi to interface with the arduino.
# Date : 2nd May 2020
# Written by: Daniel Ackuaku, for CS 300 Final Project
# Institution: Calvin University
# Professor: Dereck Schuurman
#
#
# Reads serial data from the sensors on the arduino and stores them in an sql data base
# uses data from the SQL database to detect if the bathroom is occupied or not.
# intercaes with the google home.   
#############################################################################################
from pprint import pprint
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
# import serial
# import time 
# import datetime

##########################################################################
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", SCOPES)
client = gspread.authorize(creds)
sheet = client.open("Occupod").sheet1
data = sheet.get_all_records()
pprint(data)


##########################################################################


# try:
# 	while True:
# 		arduino = serial.Serial("/dev/ttyACM0", 9600) # make sure you write correct serial
# 		data = arduino.readline().decode()
# 		pieces =data.split("\t")
# 		lights = pieces[0]
# 		temperature = pieces[1]
# 		humidity = pieces[2]
# 		motion = pieces[3]
# 		print(lights, temperature, humidity, motion)
# except KeyboardInterrupt:
# 	print ("Done")

