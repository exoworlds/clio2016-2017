import matplotlib.patches as mpatches
import numpy
import matplotlib.pyplot as plt
from astropy.io import fits

"""
Plan:
x Open up 4 images
x For each image:
	Open image
	Read in a pixel
	Apply correction to pixel
Subtract image 1 - image 4
Write that to a fits file

"""
def open_images():
	i = 0
	while i < 4:
		fname = "tau_0000"+str(i+1)+".fit"
		correct_image(fname)
		i = i + 1
		
	fname1 = "FIXED_IMG"+str(1)+".fits"
	fname2 = "FIXED_IMG"+str(4)+".fits"

	x = 0
	y = 0
	ds9x2 = 400
	ds9y2 = 200
	coefs_inv = [3.67e-16, -7.58e-11, 2.69e-06, 9.66e-01, 1.39e+02]
	
	hdu1 = fits.open(fname1)
	scidata = hdu1[0].data
	array1 = numpy.ndarray(shape=(ds9y2,ds9x2))
	while x < ds9x2:
		while y < ds9y2:
			str_num = str(scidata[y,x])
			num = float(str_num)
			new_num = num*num*num*num*coefs_inv[0] + num*num*num*coefs_inv[1] + num*num*coefs_inv[2] + num*coefs_inv[3] + coefs_inv[4]
			array1.itemset((y,x),new_num)
			y = y + 1
		y = 0
		x = x + 1
	
	hdu1 = fits.open(fname2)
	scidata = hdu1[0].data
	array2 = numpy.ndarray(shape=(ds9y2,ds9x2))
	while x < ds9x2:
		while y < ds9y2:
			str_num = str(scidata[y,x])
			num = float(str_num)
			new_num = num*num*num*num*coefs_inv[0] + num*num*num*coefs_inv[1] + num*num*coefs_inv[2] + num*coefs_inv[3] + coefs_inv[4]
			array2.itemset((y,x),new_num)
			y = y + 1
		y = 0
		x = x + 1

	array = numpy.subtract(array1,array2)
	
	hdu = fits.PrimaryHDU(array)
	hdu.writeto('FIXED_sub_IMG'+str(1)+'.fits', clobber = True)


def correct_image(fname):
	x = 0
	y = 0
	ds9x2 = 400
	ds9y2 = 200
	coefs_inv = [3.67e-16, -7.58e-11, 2.69e-06, 9.66e-01, 1.39e+02]

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
	hdu.writeto('FIXED_IMG'+fname+'.fits', clobber = True)
	
open_images()