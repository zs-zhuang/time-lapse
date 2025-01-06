This script will capture the information sending into the USB/serial port by the arduino and save it to a file. Currently it will save temperature once per minute along with the time stamp on the computer. Double check which serial port you are using and change the script accordingly:

In the script there will be a command that looks like:
ser = serial.Serial('/dev/ttyACM0', 9600) # specify USB port

You might have to change the ttyACMO to whatever serial port you have

To run this script, just open a terminal and type

./serial_to_file_new_line.py

It will start to print temperature onto the screen and saving it to a file at the same time. The saved file is called temp.log. Start this script when you start the experiment and kill the script when you stop the experiment.

This script works with the Arduino script in the Arduino directory.