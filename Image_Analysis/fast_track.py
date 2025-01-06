#! /usr/bin/python

import os, sys, string, math, Image, ImageOps, numpy as np

###################################################################################################
# Some parameters and files  we will be using
###################################################################################################
start = 0 # first image -or- background image
stop = 100 # last image -or- reference image
interval = 1

x_start = 0
x_end = 2152
y_start = 0
y_end = 3000

x_range = x_end - x_start
y_range = y_end - y_start

###################################################################################################
# Load the reference image
# This part gets colony information from the very last image
# Information include size, list of pixel locations, unique tag ID (index) for each individual colony
# Data will be saved in a dictionary where key = tuple = (x, y), and value = index
# This data will be used as reference to track colonies in all the previous images over time
###################################################################################################
in_ref_image = "refined_999.png"
im_ref = Image.open(in_ref_image)
ref = im_ref.load()
ref_white_location = []
ref_d_white = {}

# Go through every pixel and write out location of each white pixel and assign an unique index to each location
ref_index = 1
for y in range(0, y_range):
#for y in range(0, 450):
		for x in range(0, x_range):
		#for x in range(0, 450):
       	 		Iref = ref[x, y]
			if Iref == 255:
				ref_location = (x, y)
				ref_white_location.append(ref_location)
				ref_d_white[ref_location] = ref_index
                        	ref_index = ref_index + 1


# Go through all the white pixels, if they are connected, their index value will be updated to the same index
delta = -1

while delta != 0:
	
	delta = 0


	for j in range (0, len(ref_white_location)):
        	location_now = ref_white_location[j]
        	x = location_now[0]
        	y = location_now[1]
        	index_now = ref_d_white[location_now]

        	neighbor1 = (x-1, y-1)
        	neighbor2 = (x-1, y)
        	neighbor3 = (x-1, y+1)
        	neighbor4 = (x, y-1)
        	neighbor5 = (x, y+1)
        	neighbor6 = (x+1, y-1)
        	neighbor7 = (x+1, y)
        	neighbor8 = (x+1, y+1)


		if neighbor1 in ref_d_white:
			if index_now < ref_d_white[neighbor1]:	
				ref_d_white[neighbor1] = index_now
				delta = delta + 1 
			if index_now > ref_d_white[neighbor1]:
				ref_d_white[location_now] =  ref_d_white[neighbor1]
				delta = delta + 1			

		if neighbor2 in ref_d_white:
			if index_now < ref_d_white[neighbor2]:
                        	ref_d_white[neighbor2] = index_now
				delta = delta + 1
                	if index_now > ref_d_white[neighbor2]:
                        	ref_d_white[location_now] =  ref_d_white[neighbor2]
				delta = delta + 1

		if neighbor3 in ref_d_white:
			if index_now < ref_d_white[neighbor3]:
                        	ref_d_white[neighbor3] = index_now
				delta = delta + 1
                	if index_now > ref_d_white[neighbor3]:
                        	ref_d_white[location_now] =  ref_d_white[neighbor3]
				delta = delta + 1

		if neighbor4 in ref_d_white:
			if index_now < ref_d_white[neighbor4]:
                        	ref_d_white[neighbor4] = index_now
				delta = delta + 1
                	if index_now > ref_d_white[neighbor4]:
                        	ref_d_white[location_now] =  ref_d_white[neighbor4]
				delta = delta + 1

		if neighbor5 in ref_d_white:
			if index_now < ref_d_white[neighbor5]:
                        	ref_d_white[neighbor5] = index_now
				delta = delta + 1
                	if index_now > ref_d_white[neighbor5]:
                        	ref_d_white[location_now] =  ref_d_white[neighbor5]
				delta = delta + 1

		if neighbor6 in ref_d_white:
			if index_now < ref_d_white[neighbor6]:
                        	ref_d_white[neighbor6] = index_now
				delta = delta + 1
                	if index_now > ref_d_white[neighbor6]:
                        	ref_d_white[location_now] =  ref_d_white[neighbor6]
				delta = delta + 1

		if neighbor7 in ref_d_white:
			if index_now < ref_d_white[neighbor7]:
                        	ref_d_white[neighbor7] = index_now
				delta = delta + 1
                	if index_now > ref_d_white[neighbor7]:
                        	ref_d_white[location_now] =  ref_d_white[neighbor7]
				delta = delta + 1

		if neighbor8 in ref_d_white:
			if  index_now < ref_d_white[neighbor8]:
                        	ref_d_white[neighbor8] = index_now
				delta = delta + 1
                	if index_now > ref_d_white[neighbor8]:
                        	ref_d_white[location_now] =  ref_d_white[neighbor8]	         
				delta = delta + 1
	print delta


# Figure out how many unique colonies we got and their corresponding size
ref_d_index = {} # each unique index value corresponds to a unique colony
for key, value in ref_d_white.iteritems():
	if value not in ref_d_index:
		ref_d_index[value] = []		
	ref_d_index[value].append(key)

print 'total number of reference colony is '+str(len(ref_d_index))
#print ref_d_index

log_file_name = 'ref_log_image999'
out_log = open(log_file_name, 'w')
for key in ref_d_index:
	#print len(ref_d_index[key])
	out_log.write(str(key)+' '+str(len(ref_d_index[key]))+'\n')



#########################################################################################
#########################################################################################
# This part loops through all the images collected over time and track colony growth
#########################################################################################
#########################################################################################

i = start
while i < stop+1:
	in_current_image = "refined_"+str(i)+".png"
	print in_current_image
	im_current = Image.open(in_current_image)
	current = im_current.load()
	current_white_location = []
	current_d_white = {}
	
	tag = 1
	for y in range(0, y_range):
                for x in range(0, x_range):
                        I = current[x, y]
                        if I == 255:
                                location = (x, y)
                                current_white_location.append(location)
                                current_d_white[location] = tag
                                tag = tag + 1	

	
				
	# Go through all the white pixels in current image, and reassign their temporary index  value to the correct index value
	# "correct" means index value compatible with the index assigned to the last reference image
	for t in range (0, len(current_white_location)):
        	location_now = current_white_location[t]
        	if location_now in ref_d_white:
			current_d_white[location_now] = ref_d_white[location_now]

		else:
			print 'unknown pixel'
			print location_now
			current_d_white[location_now] = 'XXX'
		
	
	#print current_d_white

	# Now I have a current_d_white dictionary with the correct index value for each pixel
	# To measure colony size, I just have to count number of pixel with the same index value
	
	current_d_index = {} # each unique index value corresponds to a unique colony
	for key, value in current_d_white.iteritems():
        	if value not in current_d_index:
                	current_d_index[value] = []
        	current_d_index[value].append(key)

	print 'total number of colony on image'+str(i)+' is '+str(len(current_d_index))

	log2_file_name = 'log_image_'+str(i)
        out_log2 = open(log2_file_name, 'w')
	for key in current_d_index:
        	out_log2.write(str(key)+' '+str(len(current_d_index[key]))+'\n')	

	i = i + interval
