#! /usr/bin/python

import sys, string, math, os, Image, ImageOps

im = Image.open("edit_999.png")
width, height = im.size

print width, height
print im.format, im.size, im.mode



image = im.load()

binary = []

for y in range(height):
    for x in range(width):
        Ixy = image[x, y]
        pixels = Ixy
        binary.append(pixels)


binary2 = []
for z in range (0, len(binary)):
	current = binary[z]
	if current > 0:
		current = 255
	binary2.append(current)



out_file = open('temp_999.data', 'w')

for j in range (0, len(binary2)):
	entry = binary2[j]
	out_file.write(str(entry)+'\n')


refined_pic = "temp_999.png"
im = Image.new('1', (width, height))
im.putdata(binary2)
im.save(refined_pic, "png")
