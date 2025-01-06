#! /usr/bin/python

import os, string, math, sys, Image, ImageOps

# This script will average the intensity of the first few images to obtain the background intensity

###################################################################################################
# Some parameters we will be using
###################################################################################################
start = 0 # first image used for averaging background intensity
stop = 5 # last image used for averaging background intensity
interval = 1

x_start = 0
x_end = 2152
y_start = 0
y_end = 3000

x_range = x_end - x_start
y_range = y_end - y_start


####################################################################################################
# Loop over the images, average their intensity and write out as a new gray_scale background image 00
####################################################################################################


d = {}
for y in range(0, y_range):
	for x in range(0, x_range):
		d[x,y] = 0


i = start
while i < stop + 1:
	file_name = "image"+str(i)+".pnm"
	im = Image.open(file_name)
	print file_name
	box = (x_start, y_start, x_end, y_end)
	crop = im.crop(box)
	crop_grey = ImageOps.grayscale(crop)
	current = crop_grey.load()
	for y in range(0, y_range):
		for x in range(0, x_range):
       	 		I = current[x, y]
			#print I
			d[x,y] = d[x,y] + I
			#print d
		
	i = i + interval	

background = Image.new('L', (x_range, y_range))
bg = background.load()

n = int(stop - start)/interval + 1
print n

for key, value in d.iteritems():
	location = key
	I = value/n
	bg[location] = I

background.save('image00.pnm', 'png')  # saving this as a png file, but use pnm extension in file name

