#! /usr/bin/python

import os, sys, math, string, Image, ImageOps

# This program removes orphaned white pixel surrounded by 7 or 8 black pixels
# This is a one time procedue and does not iterate to self consistency to avoid removing signals by accident, especially the colony edges
# only run this on the last reference image (999)


final_image = 'temp_999.png'
in_image = Image.open(final_image)
im = in_image.load()
width, height = in_image.size
print width, height


lookup = [ [0 for i in range(0,width)]
              for j in range(0,height) ]


#file = 'temp_999.data'
#file_open = open(file, 'r')
#data = file_open.readlines()
	
#count = 0

#for y in range (0, height):
#	for x in range (0, width):
#		I = im[x, y]
#		lookup[y][x] = im[x, y]
#        	if I == 255:
#			count = count + 1		

#print count


for y in range (0, height):
        for x in range (0, width):
                I = im[x, y]
                lookup[y][x] = im[x, y]


data_new = [ [0 for m in range(0,width)]
                      for n in range(0,height) ]


count_orphan_black = 0
count_orphan_white = 0


for b in range (1, height-1):		
	for a in range (1, width-1):
		neighbor_b = 0
		neighbor_w = 0

#		if lookup[b][a] == 0: #black
#			#print b
#			#print a
#			if lookup[b][a-1] == 255:
#                        	neighbor_w = neighbor_w + 1
#                        if lookup[b][a+1] == 255:
#                        	neighbor_w = neighbor_w + 1
#
#                        if lookup[b+1][a-1] == 255:
#                        	neighbor_w = neighbor_w + 1
#                        if lookup[b+1][a+1] == 255:
#                        	neighbor_w = neighbor_w + 1
#                        if lookup[b+1][a] == 255:
#                        	neighbor_w = neighbor_w + 1
#
#                        if lookup[b-1][a-1] == 255:
#                        	neighbor_w = neighbor_w + 1
#                        if lookup[b-1][a+1] == 255:
#                        	neighbor_w = neighbor_w + 1
#                        if lookup[b-1][a] == 255:
#                        	neighbor_w = neighbor_w + 1				
#		if neighbor_w > 5:
#                	count_orphan_black = count_orphan_black + 1
#                	data_new[b][a] = 255
#               else:
#                	data_new[b][a] = lookup[b][a]

		if lookup[b][a] == 255: #white
			if lookup[b][a-1] == 0:
				neighbor_b = neighbor_b + 1
			if lookup[b][a+1] == 0:
				neighbor_b = neighbor_b + 1

			if lookup[b+1][a-1] == 0:
               			neighbor_b = neighbor_b + 1
       			if lookup[b+1][a+1] == 0:
                		neighbor_b = neighbor_b + 1
			if lookup[b+1][a] == 0:
                		neighbor_b = neighbor_b + 1

			if lookup[b-1][a-1] == 0:
                		neighbor_b = neighbor_b + 1
        		if lookup[b-1][a+1] == 0:
               			neighbor_b = neighbor_b + 1
			if lookup[b-1][a] == 0:
                		neighbor_b = neighbor_b + 1
		
		if neighbor_b > 5:
			count_orphan_white = count_orphan_white + 1
			data_new[b][a] = 0
		else:
			data_new[b][a] = lookup[b][a]

	

print 'removed '+ str(count_orphan_black) +' black pixels'
print 'removed '+ str(count_orphan_white) +' white pixels'

list_new = []

for b in range (0, height):
        for a in range (0, width):
	
		intensity = data_new[b][a]
		list_new.append(intensity)


refined_pic = "refined_999.png"
im_morph = Image.new('1', (width, height))
im_morph.putdata(list_new)
im_morph.save(refined_pic, "png")


refined_data = "refined_999.data"
out_file = open(refined_data, 'w')
for q in range (0, len(list_new)):
	entry = list_new[q]
	out_file.write(str(entry)+'\n')

