import matplotlib.patches as mpatches
import numpy
import matplotlib.pyplot as plt
from astropy.io import fits

"""
Plan:
Open up 4 images
For each image:
	Open image
	Read in a pixel
	Apply correction to pixel
Subtract image 1 - image 4
Write that to a fits file

"""
i = 0
while i < 4:
	imageAmount = 21
	raw_ints = []
	raw_counts = []
	ints = []
	counts = []
	
	lower = 60
	lower_adj = 5
	upper = 109
	upper_adj = 8
	x = 0
	y = 0
	count = 0
	ds9x2 = 400
	ds9y2 = 200
	coefs_inv = [3.67e-16, -7.58e-11, 2.69e-06, 9.66e-01, 1.39e+02]
	myList = []

	fname = "tau_0000"+str(i+1)+".fit"
	hdu1 = fits.open(fname)
	scidata = hdu1[0].data
	
	array = numpy.ndarray(shape=(ds9y2,ds9x2))


	while x < ds9x2:
		while y < ds9y2:
			str_num = str(scidata[0,y,x])
			num = float(str_num)
			new_num = num*num*num*num*coefs_inv[0] + num*num*num*coefs_inv[1] + num*num*coefs_inv[2] + num*coefs_inv[3] + coefs_inv[4]
			array.itemset((y,x),new_num)
			y = y + 1
		y = 0
		x = x + 1
		
	
	

	hdu = fits.PrimaryHDU(array)
	hdu.writeto('FIXED_IMG'+str(i+1)+'.fits', clobber = True)
	i = i + 1
	

def open_correct_images():
	i = 0
	count = 0
	ds9x1 = 200
	ds9x2 = 350
	ds9y1 = 0
	ds9y2 = 200
	
	coefs_inv = [3.67e-16, -7.58e-11, 2.69e-06, 9.66e-01, 1.39e+02]

	while i < imageAmount:
		if i < 9:
			fname = "Linearity0000"+str(i+1)+".fit"
		elif i >= 9 and i <99:
			fname = "Linearity000"+str(i+1)+".fit"
		else:
			fname = "Linearity00"+str(i+1)+".fit"
			
		hdu1 = fits.open(fname)
		scidata = hdu1[0].data
		
		x = 0
		
		while i < 20 and x < 10:
			num = numpy.median(scidata[x,ds9y1:ds9y2,ds9x1:ds9x2])
			if num > 20000:
				corrected.append(num*num*num*coefs_inv[0] + num*num*coefs_inv[1] + num*coefs_inv[2] + coefs_inv[3])	
			else:
				corrected.append(num)
			x += 1
			count += 1
			
		x = 0
		while i == 20 and x < 5:
			num = numpy.median(scidata[x,ds9y1:ds9y2,ds9x1:ds9x2])
			if num > 20000:
				corrected.append(num*num*num*coefs_inv[0] + num*num*coefs_inv[1] + num*coefs_inv[2] + coefs_inv[3])		
			else:
				corrected.append(num)
			x += 1
			count += 1
		i += 1
	return
	
def subtract_images():
	return

def write_images():
	return

