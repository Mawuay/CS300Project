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
import sqlite3
import datetime
import sys
import signal

# constants
FILENAME = 'bathroom.db'
TABLE = 'BathroomData'
PERIOD = 10.0



def sigint_handler(signum, frame):
    ''' SIGINT handler
    '''
    global db
    db.close()
    sys.exit(0)

def timer_handler(signum, frame):
    ''' Periodic timer signal handler
    '''
    global bus
    global db
    global cursor

    # connection = sqlite3.connect(FILENAME)
    arduino = serial.Serial("/dev/ttyACM0", 9600) # make sure you write correct serial
    bathroomStateVar = arduino.readline().decode()
    sqlcmd = "INSERT INTO " + TABLE + \
    " VALUES (datetime('now','localtime'), bathroomState ( + bathroomStateVar + )"
    # cursor = connection.cursor()
    sqlcmd = "INSERT INTO " + TABLE + "(datetime, bathroomState) VALUES (?, ?),('23', "+ bathroomStateVar + ")" # put the data in the database
    
    
    # sqlcmd = "INSERT INTO " + TABLE + \
    # " VALUES (datetime('now','localtime'),"+str(temp)+")"
    cursor.execute(sqlcmd)

    sqlcmd = "DELETE FROM " + TABLE + \
    " WHERE datetime < datetime('now','localtime','-1 hour')"
    cursor.execute(sqlcmd)
    db.commit()

# # Connect to I2C bus
# bus = smbus.SMBus(BUS)

# Connect to the database
db = sqlite3.connect(FILENAME)
cursor = db.cursor()

# setup a sigint handler
signal.signal(signal.SIGINT, sigint_handler)

# Setup signal to call handler every PERIOD seconds
signal.signal(signal.SIGALRM, timer_handler)
signal.setitimer(signal.ITIMER_REAL, 1, PERIOD)

# Continuously loop blocking on signals
try:
    while True:
        signal.pause() # block on signal, handler is called automatically

# try:
    # while True:
    #     arduino = serial.Serial("/dev/ttyACM0", 9600) # make sure you write correct serial
    #     bathroomStateVar = arduino.readline().decode()
    #     sqlcmd = "INSERT INTO " + TABLE + \
    #     " VALUES (datetime('now','localtime'),bathroomState("+ str(bathroomStateVar) +"))"
    #     cursor = connection.cursor()
    #     cursor.execute("INSERT INTO " + TABLE + "(datetime, bathroomState) VALUES (?, ?)",
    #     ('23', bathroomStateVar)) # put the data in the database

         
except KeyboardInterrupt:
    results = cursor.fetchall()
    for r in results:
        print(results)
    cursor.close()
    db.close()
    print("Done")



