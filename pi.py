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

import serial
import time
#import MySQLdb as mdb
try:
	while True:
		arduino = serial.Serial("/dev/ttyACM0", 9600) # make sure you write correct serial
		data = arduino.readline().decode()
		pieces =data.split("\t")
		lights = pieces[0]
		temperature = pieces[1]
		humidity = pieces[2]
		motion = pieces[3]
		print(lights, temperature, humidity, motion)
except KeyboardInterrupt:
	print ("Done")
#con = mdb.connect('localhost','root','password','database_name');
#with con:
 # cursor =con.cursor()
 # cursor.execute("INSERT INTO table_name VALUES('',%s,%s)",(temperature    ,humidity))
 # con.commit()
 # cursor.close()
# Log temperature every 10 seconds
