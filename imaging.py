#Author:  Tsewang Stanzin

import os
import sys
import time
from datetime import datetime, timedelta
import shutil
# import pyfits
from astropy.io import fits
import astropy.io.fits as pyfits
from PIL import Image, ImageDraw, ImageFont 
import numpy as np
from numpy import *
from stat import S_ISREG, ST_CTIME, ST_MODE
import cv2
import argparse
import os
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)


previous_date=datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')
now = datetime.now()
newDirName='/opt/lampp/htdocs/IAO/sky/allskycamera/'+now.strftime("%Y%m%d")
# Create target Directory if don't exist
if not os.path.exists(newDirName):
	os.mkdir(newDirName)
	os.mkdir(newDirName+'/0_fits/')
	print("New Date Directory Created...Creating a movie of previous date........Wait")

	save_path = '/opt/lampp/htdocs/IAO/sky/allskycamera/Movies/'+previous_date+'.mp4'
	ap = argparse.ArgumentParser()
	ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
	ap.add_argument("-o", "--output", required=False, default=save_path, help="output video file")
	args = vars(ap.parse_args())
	movieimage_path = '/opt/lampp/htdocs/IAO/sky/allskycamera/'+previous_date
	ext = args['extension']
	output = args['output']
	images = []
	for f in os.listdir(movieimage_path):
    		if f.endswith(ext):
       		 images.append(f)
	image_path = os.path.join(movieimage_path, images[0])
	frame = cv2.imread(image_path)
	cv2.imshow('video',frame)
	height, width, channels = frame.shape
	fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
	out = cv2.VideoWriter(output, fourcc, 10.0, (width, height))
	for image in images:
		image_path = os.path.join(movieimage_path, image)
		frame = cv2.imread(image_path)    
		out.write(frame) # Write out frame to video
		cv2.imshow('video',frame)
		if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
			break
	out.release()
	cv2.destroyAllWindows()
	print("The output video is {}".format(output))
      		
else:    
	print("Date has not changed...Continuing in todays folder")

stamped_dst = newDirName;

src = '/home/iiap/Desktop/stellacam/Temp/';
dst = '/opt/lampp/htdocs/IAO/sky/allskycamera/latest.png';



fnt = ImageFont.truetype('/var/lib/defoma/gs.d/dirs/fonts/DejaVuSerif.ttf', 12);# check availability of font fiel on the system path

arr = os.listdir(src);
#print (arr);
for fname in arr:
	#print(fname);
	bname, ext = fname.split('.');
	#print(ext);
	dat, tim = bname.split('_');
	# Can check for extention
	srcpath = src + fname;
	#print(srcpath);

	# Code for stamping the image
	image = Image.open(srcpath);
	draw = ImageDraw.Draw(image);
	#draw.text((15, 5), "Gain: ", font=fnt, fill=(255, 255, 255));
	#draw.text((15, 25), "FrameRate: ", font=fnt, fill=(255, 255, 255));

	draw.text((560, 5), tim+" IST", font=fnt, fill=(255, 255, 255));
	draw.text((560, 25), dat, font=fnt, fill=(255, 255, 255));

	draw.text((15, 465), "All Sky Camera", font=fnt, fill=(255, 255, 255));
	draw.text((560, 465), "©IAO Hanle", font=fnt, fill=(255, 255, 255));

	draw.text((314, 5), "N", font=fnt, fill=(0,255,0));
	draw.text((314, 465), "S", font=fnt, fill=(0,255,0));
	draw.text((70, 236), "E", font=fnt, fill=(0,255,0));
	draw.text((550, 236), "W", font=fnt, fill=(0,255,0));
	image.save(srcpath);
	
	#temp_path = stamped_dst + fname;
	shutil.move(srcpath,stamped_dst);
       	#Take the image form stamped_dst ,  convert  to fits and edit the header.. correct the image and replace back the png      
	png_file=stamped_dst + '/' + fname
	fits_file=stamped_dst+'/0_fits/'+ bname + '.fits';	
	
	image = Image.open(png_file)
	xsize, ysize = image.size
	plt.imshow(image)
	#plt.show()
	image = image.transpose(Image.FLIP_TOP_BOTTOM)
	I = np.asarray(image)
	I.shape
	I = transpose(I, (2, 0, 1))
	I = I[:3]
	test= pyfits.PrimaryHDU(data=I)
	test.header['Time'] =  time.strftime("%H:%M:%S") # add spurious header info
	test.header['Date'] =  time.strftime("%d-%m-%Y")
	test.header['Place'] =  'IAO Hanle'
	test.header['Dev_Info'] =  'Stella_Cam'
	#test.header['Mean'] =  str(mean)
	#test.header['Std_dev'] =  str(stdv)
	
	hdulist = fits.HDUList([test,test])
	#print(hdulist)
	test.writeto(fits_file)
	time.sleep(1)

	#correction_file = pyfits.open(fits_file);
	#correction_data = correction_file[0].data + correction_file[0].data;	#Subtracting dark frame 
	#print(inp_data)
        #flat fielding not done
	#flat_data = flat_file[0].data/255.0;
	#i=0; 
	#while(i< inp_data.shape[0]): 
	#	inp_file[0].data[i,:] = abs(inp_data[i,:]*flat_data[i,:]);# to manage bit width of the image n color depth in grayscale
	#	i = i + 1;
	#End of code
	sys_call= "vips im_copy " + fits_file + " " + png_file;   #Back to PNG
	os.system(sys_call);

	#inp_file = pyfits.open(fits_file, mode='update');
	#inp_data = inp_file[0].data + inp_file[0].data;
	#fil_header = inp_file[0].header;			#storing header info in fil_header
	#fil_data = inp_file[0].data;	
        	
	#inp_data = inp_file[0].data + dark_file[0].data;	#Subtracting dark frame 
	#png_file = ImageOps.mirror(png_file)
	#png_file.save('lena_mirror.jpg', quality=95)
	#sys_call = "vips im_copy " + png_file + " " + fits_file;
	#os.system(sys_call);
        # Do the corrections # Convert Back to png
	      
		        
time.sleep(1);

#Relative or absolute path to the directory
dir_path = stamped_dst

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
   	 os.path.basename(path)

arr2 = os.path.basename(path)

temp2_path = path;

#shutil.move(srcpath,temp_path);
#temp_path = stamped_dst + fname;
shutil.copy(temp2_path,dst);

time.sleep(2);







