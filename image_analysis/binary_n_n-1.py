#! /usr/bin/python
import os, sys, math, string, Image, ImageOps

# This script combine the functionality of get_intensity.py, convert_bw.py and de_noise_n_n-1.py

###################################################################################################
# Some parameters we will be using
###################################################################################################
start = 0 # first image -or- background image
stop = 100 # last image -or- reference image
interval = 1
error = 10

x_start = 0
x_end = 2152
y_start = 0
y_end = 3000

x_range = x_end - x_start
y_range = y_end - y_start

###################################################################################################
# Load the background image
###################################################################################################
#in_bg_image = "image"+str(start)+".pnm"
in_bg_image = "image00.pnm"
bg_image = Image.open(in_bg_image)
bg = bg_image.load()
#out_bg_image = "gray_crop"+str(start)+".png" # in case I want to save grey scale images
#out_bg_data = "data_"+start # in case I want to save grey scale intensity data

im_bg = Image.open(in_bg_image)

box = (x_start, y_start, x_end, y_end)
# crop the image and convert to grey scale if have not done so yet (do not need this if using image00 as background)
#crop_bg = im_bg.crop(box)
#crop_grey_bg = ImageOps.grayscale(crop_bg)
#crop_grey_bg.save(out_bg_image, 'png')
#bg = crop_grey_bg.load()



###################################################################################################
# Load image999, which is already cropped and in binary format
###################################################################################################
in_999_image = "refined_999.png"
im_999 = Image.open(in_999_image)
pic999 = im_999.load()


###################################################################################################
# Loop through all images and convert to binary without de-noise
###################################################################################################

#for i in range (start, stop+1):
i = start
while i < stop+1:
	in_image = "image"+str(i)+".pnm"
	out_image2 = "error"+str(error)+"_bw_"+str(i)+".png"
	print in_image
	im = Image.open(in_image)
	crop = im.crop(box)
	crop_grey = ImageOps.grayscale(crop)
	#crop_grey.save(out_image1, 'png')
	current = crop_grey.load()
	for y in range(0, y_range):
		for x in range(0, x_range):
       	 		I = current[x, y]
			Ibg = bg[x, y]
			if Ibg > I + error:
				current[x, y] = 255
			else:
				current[x, y] = 0

	crop_grey.save(out_image2, 'png')
	i = i + interval

#####################################################################################################
# Loop through the preliminary binary images (error_.png) and remove noise
#####################################################################################################

# Compare last image with image999 first
image_last = "error"+str(error)+"_bw_"+str(stop)+".png"
print image_last
im_last = Image.open(image_last)
last = im_last.load()
count = 0

for y in range(0, y_range):
                for x in range(0, x_range):
			I_last = last[x,y]
			I_999 = pic999[x, y]
			if I_999 == 0 and I_last == 255:
				last[x,y] = 0
				count = count + 1
			else:
				last[x,y] = last[x,y]	

print "removed "+str(count)+" white pixel on image "+str(stop)

refined_last_name = "refined_"+str(stop)+".png"
im_last.save(refined_last_name, 'png')


# Starting with last image, compare image n with image n-1 and remove all white pixels on image n-1 that is black on image n
j = stop

while j > start:
	ref_file_name = "refined_"+str(j)+".png"
	compare_file_name = "error"+str(error)+"_bw_"+str(j-interval)+".png"
	save_file_name = "refined_"+str(j-interval)+".png"
	print ref_file_name
	print compare_file_name
	im_ref = Image.open(ref_file_name)
	im_compare = Image.open(compare_file_name)
	ref = im_ref.load()
	compare = im_compare.load()
	count2 = 0
	for y in range(0, y_range):
                for x in range(0, x_range):
                        I_ref = ref[x,y]
                        I_compare = compare[x, y]
                        if I_ref == 0 and I_compare == 255:
                                compare[x,y] = 0
				count2 = count2 + 1
                        else:
                                compare[x,y] = compare[x,y]
	im_compare.save(save_file_name, 'png')
	print "removed "+str(count2)+" white pixel on image "+str(j-interval)
	j = j - interval



