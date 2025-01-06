#! /usr/bin/python

import os, sys, math, string


in_file = open ("count",'r')
content = in_file.readlines()
parameters = content[0].rstrip()
file_number = parameters.split()[0]

i = int(file_number)  #not counting the bashscript and the count file it just generated, so counting start at 0 for the image files 
filename = "image" + str(i) + ".pnm"


#print filename


#cmd = "scanimage --mode=color --resolution=300 > " + filename 
# If scanner has a transparency unit in the lid with light source, use --source=Transparency to turn on illumination 
# scanimage -A will show all options available to the device
#cmd = "scanimage --source=Transparency --resolution=800 > " + filename
#cmd = "scanimage --resolution=400 > " + filename

#cmd = "scanimage --device-name=epkowa:interpreter:001:018 --source=Transparency -t 55 --resolution=800 > " + filename
#cmd = "scanimage --device-name=epkowa:interpreter:001:018 --source=Transparency -t 140 --resolution=800 > " + filename
cmd = "scanimage --source=Transparency -t 55 --resolution=800 > " + filename

#cmd = "scanimage --device-name=epkowa:interpreter:001:003 --source=Transparency --resolution=800 > " + filename

# the order at which the options are given to scanimage matters, so double check it's working

#print cmd

os.popen(cmd)

