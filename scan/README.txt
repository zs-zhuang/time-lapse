The followings are for the Ubuntu Linux computer that's connected to the scanners

1. Open a terminal on the computer
type:
crontab -e (this will open a file that will tell your computer to run some process at certain time)

You need to copy/paste the following into the file that you just opened. They will look like this when you want to run these process:
56,26 * * * * /home/USERNAME/scan/bash_scan  /home/USERNAME/scan/scanner1
00,30 * * * * /home/USERNAME/scan/bash_scan  /home/USERNAME/scan/scanner2
04,34 * * * * /home/USERNAME/scan/bash_scan  /home/USERNAME/scan/scanner3

You need to replace username with the name of your own login. What this does is to run a script called bash_scan1 every hour at exact 26 min and 56 min. (it will tell the first scanner to scan at 1:26 PM, then 1:56 PM, then 2:26 PM, then 2:56 PM, etc.). Same idea for scanner 2 and scanner3.

Now you only want your computer to do this when you are running experiment, otherwise it will keep scanning empty scanners and fill your hard drive. So when you are not running experiment, you need to open the file again by typing

crontab -e

add # symbol in front of all the command to make it look like:
#56,26 * * * * /home/USERNAME/scan/bash_scan  /home/USERNAME/scan/scanner1
#00,30 * * * * /home/USERNAME/scan/bash_scan  /home/USERNAME/scan/scanner2
#04,34 * * * * /home/USERNAME/scan/bash_scan  /home/USERNAME/scan/scanner3

This effectively comment out the command and tell your computer not to run them.

Then you need to make some directories on your computer, one for each scanner.
The scanner will save all the images inside these folder. Type the following:

cd ~/
mkdir scan
cd scan/
mkdir scanner1
mkdir scanner2
mkdir scanner3
(you can keep going on if you have more than 3 scanners)
After your experiment, you will take all the image files out of this folder and move to a different computer where you will analyze them.

Now the command inside scan.py highly depend on the scanner you are using. If you are using scanners similar to the one I have, these scripts will contain a command that looks like this:

cmd = "scanimage --source=Transparency -t 55 --resolution=800 > " + filename

The number 55 inside this command controls the area being scanned on your scanner. If you are not sure, you can change the command to this:

cmd = "scanimage --source=Transparency --resolution=800 > " + filename

The above command will scan the entire available area on the scanner.