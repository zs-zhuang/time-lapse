#! /usr/bin/python

# This script will capture the serial monitor output in Arduino and save it to a text file along with time stamp

########################################################################################
#
# MAKE SURE YOUR ARDUINO SERIAL MONITOR IS OFF
# OTHERWISE THE ARDUINO SERIAL MONITOR WILL EAT YOUR CHARACTERS AND PYTHON WILL PRINT INCOMPLETE INFO TO FILE
# DO NOT START THIS SCRIPT AT THE EXACT MOMENT WHEN SERIAL PORT IS RECEIVING INFO, IT ALSO CAUSE PYTHON TO PRINT INCOMPLETE INFO 
#
########################################################################################

import sys
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600) # specify USB port

logfile = open('temp.log', 'w') # specify name of output file, 'a' for append, 'w' for overwrite
buffer = "" 


# keep adding everying read from serial monitor into a a single message until a new line sign ('\n') is encountered
while 1:
	buffer += ser.read(ser.inWaiting())
      	if (buffer != "") and '\n' in buffer:
		now = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())  # get time stamp from computer
		last_received, buffer = buffer.split('\n')[-2:]
		print str(now)+'  '+str(last_received)
		logfile.write(str(now)+'  '+str(last_received)+'\n')
        	logfile.flush() #write to hard drive


