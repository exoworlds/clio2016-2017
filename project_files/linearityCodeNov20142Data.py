import matplotlib.patches as mpatches
import numpy
import matplotlib.pyplot as plt
from astropy.io import fits

"""
main function: provide names of files to open, passes name to correct_image
correct_image: opens the image, applies the correction, writes new file
subtract_images: takes two new image names,opens them, subtracts them from each other, writes new file
horiz_slice: gets a horizontal line of pixels and graphs the counts in each pixel
vert_slice: gets a horizontal line of pixels and graphs the counts in each pixel
"""

def main():
	#opens each image, applies the correction, writes new file.
	
	#for tau
	
	i = 1
	x = 1
	flip = 0
	
	while i <= 54:
	
		if i > 9:
			fname1 = "tau_000"+str(i)+".fit"
		else:
			fname1 = "tau_0000"+str(i)+".fit"
		
		if i + 3 > 9:
			fname2 = "tau_000"+str(i+3)+".fit"
		else:
			fname2 = "tau_0000"+str(i+3)+".fit"
			
		correct_image(fname1)
		correct_image(fname2)
		
		if (flip == 0):
			subtract_images(fname1,fname2,x,4)
		else:
			subtract_images(fname2,fname1,x,4)
		
		if(i == 15):
			i = i + 7
		elif(x%3 == 0):
			i = i + 4
			if (flip == 0):
				flip = 1
			else:
				flip = 0
		else:
			i = i + 1
		
		x = x + 1
	
	i = 1
	x = 1
	flip = 0
	
	while i <= 54:
	
		if i > 9:
			fname1 = "FIXED_tau_000"+str(i)+".fit"
		else:
			fname1 = "FIXED_tau_0000"+str(i)+".fit"
		
		if i + 3 > 9:
			fname2 = "FIXED_tau_000"+str(i+3)+".fit"
		else:
			fname2 = "FIXED_tau_0000"+str(i+3)+".fit"
		
		if (flip == 0):
			subtract_images(fname1,fname2,x,1)
		else:
			subtract_images(fname2,fname1,x,1)
				
		if(i == 15):
			i = i + 7
		elif(x%3 == 0):
			i = i + 4
			if (flip == 0):
				flip = 1
			else:
				flip = 0
		else:
			i = i + 1
		
		x = x + 1
		
	
	#for tau_sat
	
	i = 1
	x = 1
	flip = 0
	
	while i <= 57:
	
		if i > 9:
			fname1 = "tau_sat_000"+str(i)+".fit"
		else:
			fname1 = "tau_sat_0000"+str(i)+".fit"
		
		if i + 3 > 9:
			fname2 = "tau_sat_000"+str(i+3)+".fit"
		else:
			fname2 = "tau_sat_0000"+str(i+3)+".fit"
			
		correct_image(fname1)
		correct_image(fname2)
		
		if (flip == 0):
			subtract_images(fname1,fname2,x,5)
		else:
			subtract_images(fname2,fname1,x,5)
		
		if(x%3 == 0):
			i = i + 4
			if (flip == 0):
				flip = 1
			else:
				flip = 0
		else:
			i = i + 1
		
		x = x + 1
	
	i = 1
	x = 1
	flip = 0
	
	while i <= 57:
	
		if i > 9:
			fname1 = "FIXED_tau_sat_000"+str(i)+".fit"
		else:
			fname1 = "FIXED_tau_sat_0000"+str(i)+".fit"
		
		if i + 3 > 9:
			fname2 = "FIXED_tau_sat_000"+str(i+3)+".fit"
		else:
			fname2 = "FIXED_tau_sat_0000"+str(i+3)+".fit"
		
		if (flip == 0):
			subtract_images(fname1,fname2,x,2)
		else:
			subtract_images(fname2,fname1,x,2)
				
		if(x%3 == 0):
			i = i + 4
			if (flip == 0):
				flip = 1
			else:
				flip = 0
		else:
			i = i + 1
		
		x = x + 1
		
	#for tau_unsat
	
	i = 1
	x = 1
	flip = 0
	
	while i <= 9:
	
		if i > 9:
			fname1 = "tau_unsat000"+str(i)+".fit"
		else:
			fname1 = "tau_unsat0000"+str(i)+".fit"
		
		if i + 3 > 9:
			fname2 = "tau_unsat000"+str(i+3)+".fit"
		else:
			fname2 = "tau_unsat0000"+str(i+3)+".fit"
			
		correct_image(fname1)
		correct_image(fname2)
					
		if (flip == 0):
			subtract_images(fname1,fname2,x,6)
		else:
			subtract_images(fname2,fname1,x,6)
				
		if(x%3 == 0):
			i = i + 4
			if (flip == 0):
				flip = 1
			else:
				flip = 0
		else:
			i = i + 1
		
		x = x + 1
	
	i = 1
	x = 1
	flip = 0
	
	while i <= 9:
	
		if i > 9:
			fname1 = "FIXED_tau_unsat000"+str(i)+".fit"
		else:
			fname1 = "FIXED_tau_unsat0000"+str(i)+".fit"
		
		if i + 3 > 9:
			fname2 = "FIXED_tau_unsat000"+str(i+3)+".fit"
		else:
			fname2 = "FIXED_tau_unsat0000"+str(i+3)+".fit"
					
		if (flip == 0):
			subtract_images(fname1,fname2,x,3)
		else:
			subtract_images(fname2,fname1,x,3)
				
		if(x%3 == 0):
			i = i + 4
			if (flip == 0):
				flip = 1
			else:
				flip = 0
		else:
			i = i + 1
		
		x = x + 1
		
	horiz_slice()
	vert_slice()

def correct_image(fname):
	x = 0
	y = 0
	ds9x2 = 400
	ds9y2 = 200
	coefs_inv = [ -6.32644177e-17,5.55450534e-11,-2.19977738e-06,1.02869293e+00,-1.21422072e+02]

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
	
def subtract_images(fname1,fname2,val,val2):
	x = 0
	y = 0
	ds9x2 = 400
	ds9y2 = 200
	
	hdu1 = fits.open(fname1)
	scidata1 = hdu1[0].data
	array1 = numpy.ndarray(shape=(ds9y2,ds9x2))
	hdu2 = fits.open(fname2)
	scidata2 = hdu2[0].data
	array2 = numpy.ndarray(shape=(ds9y2,ds9x2))
	
	while x < ds9x2:
		while y < ds9y2:
			#For first image
			if(val2 == 4 or val2 == 5 or val2 == 6):
				str_num = str(scidata1[0,y,x])
			else:
				str_num = str(scidata1[y,x])
			num = float(str_num)
			array1.itemset((y,x),num)
			
			#and the other
			if(val2 == 4 or val2 == 5 or val2 == 6):
				str_num = str(scidata2[0,y,x])
			else:
				str_num = str(scidata2[y,x])
			num = float(str_num)
			array2.itemset((y,x),num)
			y = y + 1
		y = 0
		x = x + 1

	array = numpy.subtract(array1,array2)
		
	hdu = fits.PrimaryHDU(array)
	
	if val2 == 1:
		hdu.writeto('FIXED_sub_IMG'+str(val)+'.fit', clobber = True)
	
	if val2 == 2:
		hdu.writeto('FIXED_sub_sat_IMG'+str(val)+'.fit', clobber = True)
	
	if val2 == 3:
		hdu.writeto('FIXED_sub_unsat_IMG'+str(val)+'.fit', clobber = True)
		
	if val2 == 4:
		hdu.writeto('sub_IMG'+str(val)+'.fit', clobber = True)
		
	if val2 == 5:
		hdu.writeto('sub_sat_IMG'+str(val)+'.fit', clobber = True)
		
	if val2 == 6:
		hdu.writeto('sub_unsat_IMG'+str(val)+'.fit', clobber = True)
		
def horiz_slice():
	x1 = 0
	x2 = 400
	y = 99
	fname1 = "sub_IMG1.fit"
	fname2 = "FIXED_sub_IMG1.fit"
	hdu1 = fits.open(fname1)
	hdu2 = fits.open(fname2)
	scidata1 = hdu1[0].data
	scidata2 = hdu2[0].data

	array1 = numpy.ndarray(x2)
	array2 = numpy.ndarray(x2)

	while x1 < x2:
		str_num = str(scidata1[y,x1])
		num = float(str_num)
		array1.itemset(x1,num)
		str_num = str(scidata2[y,x1])
		num = float(str_num)
		array2.itemset(x1,num)
		x1 = x1 + 1
	
	xarr = numpy.arange(0,400,1)

	plt.scatter(xarr,array1,c = 'r')
	plt.scatter(xarr,array2,c = 'b')
	plt.ylabel('counts')
	plt.xlabel('pixel')
	plt.title('Counts for subtracted initial and fixed image: horizontal',fontsize = 15)
	red_patch = mpatches.Patch(color='red', label='Original counts')
	blue_patch = mpatches.Patch(color='blue', label='Adjusted counts')
	
	plt.legend(handles=[red_patch,blue_patch],bbox_to_anchor=(1, .18))
	plt.axis([0,400,0,20000])
	plt.show()

def vert_slice():
	y1 = 0
	y2 = 200
	x = 99
	fname1 = "sub_IMG1.fit"
	fname2 = "FIXED_sub_IMG1.fit"
	hdu1 = fits.open(fname1)
	hdu2 = fits.open(fname2)
	scidata1 = hdu1[0].data
	scidata2 = hdu2[0].data
	
	array1 = numpy.ndarray(y2)
	array2 = numpy.ndarray(y2)
	
	while y1 < y2:
		str_num = str(scidata1[y1,x])
		num = float(str_num)
		array1.itemset(y1,num)
		str_num = str(scidata2[y1,x])
		num = float(str_num)
		array2.itemset(y1,num)
		y1 = y1 + 1
	
	yarr = numpy.arange(0,200,1)
	
	plt.scatter(yarr,array1,c = 'r')
	plt.scatter(yarr,array2,c = 'b')
	plt.ylabel('counts')
	plt.xlabel('pixel')
	plt.title('Counts for subtracted initial and fixed image: vertical',fontsize = 15)
	red_patch = mpatches.Patch(color='red', label='Original counts')
	blue_patch = mpatches.Patch(color='blue', label='Adjusted counts')
	
	plt.legend(handles=[red_patch,blue_patch],bbox_to_anchor=(1, .18))
	plt.axis([0,400,0,20000])
	plt.show()

main()