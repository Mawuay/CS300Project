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
from __future__ import print_function 
from googleapiclient.discovery import build  
from httplib2 import Http  
from oauth2client import file, client, tools  
from oauth2client.service_account import ServiceAccountCredentials
import serial
import time 
 
import datetime

# My Spreadsheet ID ... See google documentation on how to derive this
MY_SPREADSHEET_ID = '11As1O9ctTB7n1GkPzlEfH1AsVQ2-BiseoPWAjge6BIg' # needs to be changed to mine 


def update_sheet(sheetname, lights, temperature, humidity, motion):  
    """update_sheet method:
       appends a row of a sheet in the spreadsheet with the 
       the latest temperature, pressure and humidity sensor data
    """
    # authentication, authorization step #needs to be double checked to ensure it works with mine
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    creds = ServiceAccountCredentials.from_json_keyfile_name( 
            'creds.json', SCOPES)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API, append the next row of sensor data
    # values is the array of rows we are updating, its a single row
    values = [ [ str(datetime.datetime.now()), 
        'Light Intensity', lights, 'Temperature', temperature, 'Humidity', humidity, 'Motion', motion ] ]
    body = { 'values': values }
    # call the append API to perform the operation
    result = service.spreadsheets().values().append(
                spreadsheetId=MY_SPREADSHEET_ID, 
                range=sheetname + '!A1:G1',
                valueInputOption='USER_ENTERED', 
                insertDataOption='INSERT_ROWS',
                body=body).execute()                     


def main():  
    """main method:
       reads the serial input from teh aruino hopefully with the three sensors, then
       call update_sheets method to add that sensor data to the spreadsheet
    """
    arduino = serial.Serial("/dev/ttyACM0", 9600)
    data = arduino.readline().decode()
    pieces =data.split("\t")
    lights = pieces[0]
    temperature = pieces[1]
    humidity = pieces[2]
    motion = pieces[3]
    print ('Light Intensity: %f hPa' % lights)
    print ('Temperature: %f °C' % 	temperature)
    print ('Humidity: %f %%rH' % humidity)
    print ('Motion: %f hPa' % motion)

    update_sheet("Occupod", lights, temperature, humidity, motion)

try:
	while True:
		if __name__ == '__main__':
			main()

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
except KeyboardInterrupt:
	print ("Done")

