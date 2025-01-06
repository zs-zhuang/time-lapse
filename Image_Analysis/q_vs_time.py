#! /usr/bin/python

import os, sys, string, math, Image, ImageOps

###################################################################################################
# Some parameters and files  we will be using
###################################################################################################
start = 0 # first image -or- background image
stop = 100 # last image -or- reference image
interval = 1

initial_delay = 135 # time before first image is taken (in minutes)
time_lapse = 30 # how often the scanner scans petri dish (in minutes)
detection_threshold = 20


###################################################################################################
# get a list of all the colonies that need to be tracked
###################################################################################################

in_colony_list = open('ref_log_image999', 'r')
log = in_colony_list.readlines()

colony_list = []

for i in range (0, len(log)):
        information = log[i]
        index = information.split()[0]
        colony_list.append(index)

#print colony_list

###################################################################################################
# loop through every colony in the colony list over every image being processed
# output a two-column file for each colony
# time(a function of image number depending on how often images are taken during exp), colony size (in pixel)
# output a two-columnfile for detection time for each colony
# colony_index, detection_time
###################################################################################################

d_detected = {}
detection_file_name = "detection_time_"+str(detection_threshold)+"pix"
detection_file_name2 = "time_only_"+str(detection_threshold)+"pix"
out_detection = open(detection_file_name, 'w')
out_detection2 = open(detection_file_name2, 'w')

for a in range (0, len(colony_list)):
	colony = colony_list[a]
	out_file_name = 'colony_'+str(colony)+'_vs_time'
	out_file = open(out_file_name, 'w')	
	#print colony
	
	b = start
	while b < stop-5:
		filename = 'log_image_'+str(b)
		in_size_file = open(filename, 'r')
		in_size = in_size_file.readlines()
		time = initial_delay + b*time_lapse	
		print filename

		for c in range (0, len(in_size)):
			row = in_size[c].rstrip()
			tag = row.split()[0]
			size = row.split()[1]
			
			if tag == colony:
				out_file.write(str(time)+' '+str(size)+'\n')

				if int(size) > detection_threshold and tag not in d_detected:
					detection_size = size
		 			d_detected[colony] = time
		 			out_detection.write(str(colony)+' '+str(time)+'\n')
					out_detection2.write(str(time)+'\n')
			
		b = b + interval
 
		
