#! /usr/bin/python

import sys, string, math, os, Image, ImageOps

in_arg = sys.argv[1]
in_arg2 = sys.argv[2]

background = "data_"+in_arg
current = "data_"+in_arg2

#print background
#print current

in_file1 = open(background, 'r')
in_file2 = open(current, 'r')
in_image = "crop"+in_arg+".png"

file1 = in_file1.readlines()
file2 = in_file2.readlines()

im = Image.open(in_image)
width, height = im.size
#print width, height

binary = []

for i in range (0, len(file1)):
#for i in range (0, 100):
	entry_bg = file1[i].rstrip()
	entry_c = file2[i].rstrip()
	x = entry_bg.split()[0]
	y = entry_bg.split()[1]
	Ibg = float(entry_bg.split()[2])
	Ic = float(entry_c.split()[2])
	#print Ibg, Ic
	error = 10
	high_Ic = Ic + error
	#low_Ic = Ic - error	

	if Ibg > high_Ic :
		new_Ic = 255
		binary.append(new_Ic)

	else:
		new_Ic = 0
		binary.append(new_Ic)

#print binary
print len(binary)

new_pic = "error"+str(error)+"_bw_"+in_arg2+".png"

bw = Image.new('1', (width, height))
#bw.save("test.png", "png")
bw.putdata(binary)
bw.save(new_pic, "png")


new_data = "error"+str(error)+"_bw_"+in_arg2+".data"

out_file = open(new_data, 'w')

for j in range (0, len(binary)):
	entry = binary[j]
	out_file.write(str(entry)+'\n')
	
