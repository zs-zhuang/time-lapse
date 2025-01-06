#! /usr/bin/python
import os, sys, math, string, Image, ImageOps

#out_file = open ('data_I','w')
#im = Image.open("image0.pnm")

in_arg = sys.argv[1]
in_image = "image"+in_arg+".pnm"
out_image1 = "crop"+in_arg+".png"
out_image2 = "gray_crop"+in_arg+".png"
out_data = "data_"+in_arg


im = Image.open(in_image)
out_file = open (out_data, 'w')

im_gray = ImageOps.grayscale(im)
image = im_gray.load()

width_total, height_total = im_gray.size
#print width_total
#print height_total

x_start = 0
x_end = 2152
y_start = 0
y_end = 3000

box = (x_start, y_start, x_end, y_end)
im_crop_org = im.crop(box)
im_crop_org.save(out_image1, "png")
im_cropA = im_gray.crop(box)
im_cropA.save(out_image2, "png")
#width_temp, height_temp = im_cropA.size
#widthA, heightA = x_end - x_start, y_end - y_start
#print widthA
#print heightA


cropA_pixels = []
for y in range(y_start, y_end):
#for x in range(10):
    for x in range(x_start, x_end):
    #for y in range(5):
        Ixy = image[x, y]
        info = str(x)+' '+str(y)+' '+str(Ixy)
	#print info
        cropA_pixels.append(info)


#print cropA_pixels
#print len(cropA_pixels)

for i in range (0, len(cropA_pixels)):
	entry = cropA_pixels[i]
	out_file.write(entry+'\n')


