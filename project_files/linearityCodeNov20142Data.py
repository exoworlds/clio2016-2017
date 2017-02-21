import matplotlib.patches as mpatches
import numpy
import matplotlib.pyplot as plt
from astropy.io import fits

"""
main function: provide names of files to open, passes name to correct_image
correct_image: opens the image, applies the correction, writes new file
subtract_images: takes two new image names,opens them, subtracts them from each other, writes new file
"""

def main():
	#opens each image, applies the correction, writes new file.
	i = 1
	while i <= 56:
	
		if i > 9:
			fname = "tau_000"+str(i)+".fit"
		else:
			fname = "tau_0000"+str(i)+".fit"
		
		correct_image(fname)
		i = i + 1
	
	i = 1
	x = 1
	
	while i <= 56:
	
		if i > 9:
			fname1 = "FIXED_tau_000"+str(i)+".fit"
		else:
			fname1 = "FIXED_tau_0000"+str(i)+".fit"
		
		if i + 3 > 9:
			fname2 = "FIXED_tau_000"+str(i+3)+".fit"
		else:
			fname2 = "FIXED_tau_0000"+str(i+3)+".fit"
			
		if i + 1 > 9:
			fname3 = "FIXED_tau_000"+str(i+1)+".fit"
		else:
			fname3 = "FIXED_tau_0000"+str(i+1)+".fit"
			
		if i + 2 > 9:
			fname4 = "FIXED_tau_000"+str(i+2)+".fit"
		else:
			fname4 = "FIXED_tau_0000"+str(i+2)+".fit"
		
	
		subtract_images(fname1,fname2,x)
		
		subtract_images(fname3,fname4,x+1)
		
		x = x + 2
		i = i + 4
	


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
	hdu.writeto('FIXED_'+fname, clobber = True)
	

def subtract_images(fname1,fname2,val):
	x = 0
	y = 0
	ds9x2 = 400
	ds9y2 = 200
	coefs_inv = [3.67e-16, -7.58e-11, 2.69e-06, 9.66e-01, 1.39e+02]
	
	hdu1 = fits.open(fname1)
	scidata1 = hdu1[0].data
	array1 = numpy.ndarray(shape=(ds9y2,ds9x2))
	hdu2 = fits.open(fname2)
	scidata2 = hdu2[0].data
	array2 = numpy.ndarray(shape=(ds9y2,ds9x2))
	
	while x < ds9x2:
		while y < ds9y2:
			#For first image
			str_num = str(scidata1[y,x])
			num = float(str_num)
			new_num = num*num*num*num*coefs_inv[0] + num*num*num*coefs_inv[1] + num*num*coefs_inv[2] + num*coefs_inv[3] + coefs_inv[4]
			array1.itemset((y,x),new_num)
			
			#and the other
			str_num = str(scidata2[y,x])
			num = float(str_num)
			new_num = num*num*num*num*coefs_inv[0] + num*num*num*coefs_inv[1] + num*num*coefs_inv[2] + num*coefs_inv[3] + coefs_inv[4]
			array2.itemset((y,x),new_num)
			y = y + 1
		y = 0
		x = x + 1

	array = numpy.subtract(array1,array2)
		
	hdu = fits.PrimaryHDU(array)
	hdu.writeto('FIXED_sub_IMG'+str(val)+'.fit', clobber = True)

main()