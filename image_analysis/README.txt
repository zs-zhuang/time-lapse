###################################################################################################
# Image processing can be automated using the bash_auto script
# See bash_auto for additional comments on the requirements
#
#
# short version (scripts inside prep_reference directory):
# run ./bash_auto to process time lapse images (need refined_999.png)
# To prepare the reference image (refined_999.png)
# run ./get_intensity on background and reference image
# run ./convert_bw 5 70 (if image 5 is the background and image70 is the reference, use error20) 
# cp error20_bw_70.png to edit_999.png
# manually revise edit_999.png with gimp, save under the same name
# ./prep_999.py
# ./morph_bw.py (this will produce refined_999.png)
# ./count_colony.py (this is not necessary, it's for checking the quality of refined_999.png)
# copy refined_999.png to the directory where the rest of the images are located, run bash_auto
###################################################################################################


###################################################################################################
# Additional information on how to process images if you want to know what bash_auto does
###################################################################################################
# This only works on relatively low density petri dish where merged colonies are easily identified and very limited in number
# Merged colonies are manually edited by drawing a black line in-between to indicate them as separate colonies during image processing
# usage example:
# ./get intensity.py 45 (this will get intensity data for each pixel from image45)
# ./convert_bw.py 0 45 (this will convert image45 from greyscale to binary using greyscale image0 as background
# the output file name will indicate how much buffer/error/intensity difference between current vs. background pixel is required
# for example, error20 means current intensity needs to be at least 20 values darker than background to be considered as a colony
# Due to memory issues, crop the original image into three sub-images for the top, middle and bottom plate
For efficiency, get_intensity.py, convert_bw.py and de_noise_n_final.py have been combined into a single script binary.py

# For functionality of the individual scripts, read the following:

./get_intensity.py (crop, convert original RGB to greyscale) # run this on every images
./convert_bw.py (generate binary bw image from greyscale based on background intensity) # run this on every image


# Create a refined version of last image
copy selected reference image (such as the very last image from experiment) as edit_999.png
# manually select and edit this image
# manually reduce noise, also get rid of outlines of petri dish, draw a thin black line between two merged colony
# erase noise with black circle blush width 1 or bigger
# separate merged colony with black square pencil 0.3 width
# ONLY CONVERT WHITE PIXEL INTO BLACK WHEN REMOVING NOISE
# NEVER CONVERY BLACK PIXEL INTO WHITE EVEN IF IT'S A SINGLE BLACK PIXEL IN THE MIDDLE OF A WHITE COLONY!!!
edit with gimp and re-save as edit_999.png

# when done with edit_999.png
./prep_999.py # generate data table and refined image for manually corrected last image, only applies to reference image
save as temp_999.data
save as temp_999.png

# further refine temp_999 by running morph_bw.py, save it as refined_999.data and refined_999.png (it should not be necessary to run this on every image based on the way I process them, see next part)
# Do NOT convert orphaned black pixel to white
# 000        000
# 010 ---->  000
# 000        000
# only run the following on temp_999

./morph_bw.py # convert orphaned white pixel to black
save as refined_999.data and refined_999.png
copy refined_999.data as error20_bw_999.data
copy refined_999.png as error20_bw_999.png

# For total N images, where N is the last image (which got manually corrected to image999)
# This removes all white dots that is present in image N-1, but not present in N
# i.e. if the pixel is black in the final image, then it should not be white in the previous image

# compare imageN to refined_image999, write out refined imageN
# compare imageN-1 to refined imageN, write out refined imageN-1
# ...
# ...
# compare image1 to refined image2, write out refined image1
# compare image0 to refined image1, write out refined image0


./de_noise_n_n-1.py # might be too invasive, not using this for now, run this on every image

# Alternatively, just compared every image to 999 and remove all white dots in earlier images that turned out to be black in the final image
./de_noise_n_final.py # use this for now, run this on every image


# Track colony appearance and growth over time (need an input list containing all image ID numbers; i.e., 61, 60, 59, 58...3, 2, 1, 0)
# At the moment, I do not need to write out the pixel location of each colony on each image
# I just have that information for the last reference image using get_final_colony.py
# I could modify this script and obtain the information if I ever need that
# output multiple two-column file, one file for each unique colony, contain colony size over time information
# time, size

./fast_track.py

# To get detection time
# output a single two-column file
# colony index, time first appeared
./q_vs_time.py


# If I need detailed location of every colony on the last reference image
# this script will work on all images
# but it will generate inconsistent tag/index when individual images are processed 
# it will not keep track of which tag/index goes to which colony when it's run on image n vs. image n-1
# it will not consistently assign the same tag/index to the same colony on two different images
# tracking.py will keep track of colony on difference images and assign them the same tag/index
./count_colony.py


