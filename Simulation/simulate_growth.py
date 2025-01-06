#! /usr/bin/python

# This script calculate crowding factor based on the detection image, i.e. image on which the colony of interest is first detected

import os, string, sys, math, Image, ImageOps, numpy
from numpy  import *

##############################################################################
# This script simulates the distribution of time to reach a population size N
# bacteria divide according to certain distribution
# for example, if they divide with exponential distribution, most cells can divide and then divide again immediately
# this might be true for starved cells going through cell size reduction
# or they might divide with various growth rate that falls into a gamma or gaussian distribution
#############################################################################

n = 1000 # total number of individual cells inoculated on plates; i.e., total number of colony to be followed
L0 = 10 # arbitrary unit for the length of a newly created cell
L1 = 20 #arbitraty unit for the length of a cell ready for cell division 
size0 = 1 # every colony start with 1 bacterium
#size_d = 16384 # number of cells in a detectable colony, roughly 14 generations starting from a single cell
size_d = 1000

list_td = []
for x in range(0, n):


	size_now = size0
	time_now = 0
	list = []
	grower = size0
	offspring = size0

	while size_now < size_d:
		for i in range (0, offspring):
			g = numpy.random.exponential(3, 1) #for exponential, first variable is 1/lambda, this is 1/growth rate
			#g = numpy.random.normal(3, 0.3, 1) #for normal, first variable is mu, second is sigma, third is roll x times
        		#print g
			new_division_time = float((L1 - L0)*g)
			list.append(new_division_time)
			s_list = sorted(list, key=float)
                        next_division_time = s_list[0]			

	        
                grower = 1
		offspring = 2
		time_now = time_now + next_division_time
		size_now = size_now + grower
		#print list
		#print next_division_time
		#print size_now, time_now


		list2 = []
		for j in range(0, len(list)):
			remain = float(list[j])
			if remain != next_division_time:
				remain = remain - next_division_time
				list2.append(remain)


		#print list2
		list = list2
	

	#print time_now
	list_td.append(time_now)
	print x, time_now	

out_file = open("colony_detectime_time_list_normal", 'w')
for y in range(0, len(list_td)):
	detection_time = list_td[y]
	out_file.write(str(detection_time)+'\n')

