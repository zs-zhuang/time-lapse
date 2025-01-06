#! /usr/bin/python

import os, math, sys, Image, ImageOps, string



# get the size of the image
ref_image = 'refined_999.png'
in_image = Image.open(ref_image)
im = in_image.load()
width, height = in_image.size
#width, height = 11, 7
print width, height


file = "refined_999.data"
print file
file_open = open(file, 'r')
in_data = file_open.readlines()
	
	
# create a lookup table of pixel value for each file
lookup = [ [0 for i in range(0,width)]
              for j in range(0,height) ]


# Put pixel data into lookup
for y in range (0, height):
        for x in range (0, width):
                I = im[x, y]
                lookup[y][x] = im[x, y]

	
d_white = {}
list = []
	
index = 1
# Go through every pixel and write out location of each white pixel and assign an unique index to each location
for b in range (0, height):
	for a in range (0, width):
		if lookup[b][a] == 255:
                        location = str(a)+' '+str(b)
			list.append(location)    
			#print location
			d_white[(location)] = index		
			index = index + 1
	

#print lookup		
#print d_white					
#print list
	

# Go through all the white pixels, if they are connected, their index value will be updated to the same index
# For now, it is random what index value it ends up with, but all white pixel with the same index value belongs
# to the same colony
# I don't know what's the best way to distinguish which colony is which at the moment
	

delta = -1

while delta != 0:
	
	delta = 0
	for e in range (0, len(list)):
		location_now = list[e]
		x = int(location_now.split()[0])
		y = int(location_now.split()[1])
		index_now = d_white[(location_now)]			


		neighbor1 = str(x-1)+' '+str(y-1)	
		neighbor2 = str(x-1)+' '+str(y)
		neighbor3 = str(x-1)+' '+str(y+1)
		neighbor4 = str(x)+' '+str(y-1)
		neighbor5 = str(x)+' '+str(y+1)
		neighbor6 = str(x+1)+' '+str(y-1)
		neighbor7 = str(x+1)+' '+str(y)
		neighbor8 = str(x+1)+' '+str(y+1)
		
				

		if neighbor1 in d_white:
			if index_now < d_white[neighbor1]:	
				d_white[neighbor1] = index_now
				delta = delta + 1 
			if index_now > d_white[neighbor1]:
				d_white[location_now] =  d_white[neighbor1]
				delta = delta + 1			

		if neighbor2 in d_white:
			if index_now < d_white[neighbor2]:
                        	d_white[neighbor2] = index_now
				delta = delta + 1
                	if index_now > d_white[neighbor2]:
                        	d_white[location_now] =  d_white[neighbor2]
				delta = delta + 1

		if neighbor3 in d_white:
			if index_now < d_white[neighbor3]:
                        	d_white[neighbor3] = index_now
				delta = delta + 1
                	if index_now > d_white[neighbor3]:
                        	d_white[location_now] =  d_white[neighbor3]
				delta = delta + 1

		if neighbor4 in d_white:
			if index_now < d_white[neighbor4]:
                        	d_white[neighbor4] = index_now
				delta = delta + 1
                	if index_now > d_white[neighbor4]:
                        	d_white[location_now] =  d_white[neighbor4]
				delta = delta + 1

		if neighbor5 in d_white:
			if index_now < d_white[neighbor5]:
                        	d_white[neighbor5] = index_now
				delta = delta + 1
                	if index_now > d_white[neighbor5]:
                        	d_white[location_now] =  d_white[neighbor5]
				delta = delta + 1

		if neighbor6 in d_white:
			if index_now < d_white[neighbor6]:
                        	d_white[neighbor6] = index_now
				delta = delta + 1
                	if index_now > d_white[neighbor6]:
                        	d_white[location_now] =  d_white[neighbor6]
				delta = delta + 1

		if neighbor7 in d_white:
			if index_now < d_white[neighbor7]:
                        	d_white[neighbor7] = index_now
				delta = delta + 1
                	if index_now > d_white[neighbor7]:
                        	d_white[location_now] =  d_white[neighbor7]
				delta = delta + 1

		if neighbor8 in d_white:
			if  index_now < d_white[neighbor8]:
                        	d_white[neighbor8] = index_now
				delta = delta + 1
                	if index_now > d_white[neighbor8]:
                        	d_white[location_now] =  d_white[neighbor8]	         
				delta = delta + 1
	print delta

#print d_white


# After final iteration
# convert dictionary white to a list, white_list
# loop through white_list and count how many pixels belong to a given index
# write white_list out as a two column data file: location vs. index
		
white_list = []        
for key, value in d_white.iteritems():
        temp = str(key)+' '+str(value)
	#print temp
        white_list.append(temp)
        
#print white_list
#print len(white_list)


out_data = open('white_pix_location_vs_colony_index', 'w')
for w in range (0, len(white_list)):
	row = white_list[w]
	out_data.write(str(row)+'\n')


d_index = {}
for p in range (0, len(white_list)):
	row = white_list[p]
	index = row.split()[2]
	if index not in d_index:
		d_index[index] = index


#print d_index
print 'total number of colonies detected: '+str(len(d_index))

out_cm = open("cm", 'w')

for key, value in d_index.iteritems():
	key = []
	index = value
	#print key	
	for q in range (0, len(white_list)):
		row2 = white_list[q]
		x = row2.split()[0]
		y = row2.split()[1]
		xy = str(x)+' '+str(y)
		current_index = row2.split()[2]
		if current_index == index:
			key.append(xy)

	#print key
	size = len(key)
	print "colony_size_is "+str(size) 
		
	colony_name = 'colony_index_'+index+'_tag_by_size_'+str(size)
	#colony_name = 'colony_tag_by_size_'+str(size)
	out_file = open(colony_name, 'w')

	sum_x = 0	
	sum_y = 0

	for s in range (0, len(key)):
		entry = key[s]
		out_file.write(entry+'\n')
		x0 = entry.split()[0]
		y0 = entry.split()[1]
		sum_x = sum_x + int(x0)
		sum_y = sum_y + int(y0)

	cm_x = sum_x/len(key)
	cm_y = sum_y/len(key)
	out_cm.write(str(index)+' '+str(cm_x)+' '+str(cm_y)+'\n')

 		
				


		

