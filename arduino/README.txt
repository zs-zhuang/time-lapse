This script needs to be uploaded onto the micro controller (arduino):
doublePowerSwitch_multiTempSensor_manual_set_time.ino

It does the following: 

1. reads time from a clock in order to decide what to do
2. controls the power switch of the scanner (turns it on at certain time and turns it off at certain time)
3. reads from 6 temperature sensors periodically and save the temperature on hard drive

This script is specific to the hardware used (please check library requirements):

1. Powerswitch (1 per scanner)
https://www.sparkfun.com/products/10747

2. Temperature sensor
https://www.sparkfun.com/products/245

3. Microcontroller
https://www.sparkfun.com/products/11061

4. Clock
http://www.adafruit.com/products/255?gclid=CIKkpJWPvr4CFatj7AodlSMAUQ
