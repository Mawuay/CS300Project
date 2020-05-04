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
# Program to continuously read A/D converter
# Instantiate a new A/D object
import serial
import time
#import MySQLdb as mdb
# Software SPI pin configuration


try:
	while True:
		arduino = serial.Serial("/dev/ttyACM0", 9600) # make sure you write correct serial
		data = arduino.readline().decode()
		print(data)

except KeyboardInterrupt:
	print ("Done")

