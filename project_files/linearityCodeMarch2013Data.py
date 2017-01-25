import matplotlib.patches as mpatches
import numpy
import matplotlib.pyplot as plt
from astropy.io import fits

imageAmount = 21
raw_ints = []
raw_counts = []
ints = []
counts = []
true_counts_1 = []
true_counts_2 = []
true_counts_3 = []
true_counts_4 = []
true_counts_5 = []
true_counts_6 = []
error_0 = []
error_1 = []
error_2 = []
error_3 = []
error_4 = []
error_5 = []
error_6 = []
true_counts = []
truer_counts = []
corrected = []

lower = 60
lower_adj = 5
upper = 109
upper_adj = 8
xarr = numpy.linspace(5000,60000,21)

def open_images():
	i = 0
	count = 0
	ds9x1 = 200
	ds9x2 = 350
	ds9y1 = 0
	ds9y2 = 200

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
			raw_ints.append(float(hdu1[0].header["INT"]))
			raw_counts.append(numpy.median(scidata[x,ds9y1:ds9y2,ds9x1:ds9x2]))
			x += 1
			count += 1
			
		x = 0
		while i == 20 and x < 5:
			raw_ints.append(float(hdu1[0].header["INT"]))
			raw_counts.append(numpy.median(scidata[x,ds9y1:ds9y2,ds9x1:ds9x2]))
			x += 1
			count += 1
		i += 1
	return

def avg_ints_counts():
	ten_number = 0
	one_number = 0
	while one_number < 20:
		ints.append(raw_ints[ten_number])
		counts.append((raw_counts[ten_number]+raw_counts[ten_number+1]+raw_counts[ten_number+2]+raw_counts[ten_number+3]+raw_counts[ten_number+4]+raw_counts[ten_number+5]+raw_counts[ten_number+6]+raw_counts[ten_number+7]+raw_counts[ten_number+8]+raw_counts[ten_number+9])/10)
		ten_number += 10
		one_number += 1
		
	while one_number < 21:
		ints.append(raw_ints[ten_number])
		counts.append((raw_counts[ten_number]+raw_counts[ten_number+1]+raw_counts[ten_number+2]+raw_counts[ten_number+3]+raw_counts[ten_number+4])/5)
		ten_number += 10
		one_number += 1
	return
	
def make_true_counts():
	coeffs = numpy.polyfit(ints[lower_adj:upper_adj],counts[lower_adj:upper_adj],1)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts.append(coeffs[0]*ints[number] + coeffs[1])
		number+= 1	
	coefficients1 = numpy.polyfit(true_counts[lower_adj:upper_adj],counts[lower_adj:upper_adj],1)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts_1.append(coefficients1[0]*xarr[number] + coefficients1[1])
		number+= 1

	coefficients2 = numpy.polyfit(true_counts[0:14],counts[0:14],2)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts_2.append(coefficients2[0]*xarr[number]*xarr[number] + coefficients2[1]*xarr[number] + coefficients2[2])
		number+= 1

	coefficients3 = numpy.polyfit(true_counts[0:14],counts[0:14],3)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts_3.append(coefficients3[0]*xarr[number]*xarr[number]*xarr[number] + coefficients3[1]*xarr[number]*xarr[number] + coefficients3[2]*xarr[number] + coefficients3[3])
		number+= 1

	coefficients4 = numpy.polyfit(true_counts[0:14],counts[0:14],4)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts_4.append(coefficients4[0]*xarr[number]*xarr[number]*xarr[number]*xarr[number] + coefficients4[1]*xarr[number]*xarr[number]*xarr[number] + coefficients4[2]*xarr[number]*xarr[number] + coefficients4[3]*xarr[number] + coefficients4[4])
		number+= 1
		
	#================================REPONENING IMAGES================================#
	
	i = 0
	count = 0
	ds9x1 = 200
	ds9x2 = 350
	ds9y1 = 0
	ds9y2 = 200
	
	coefs_inv = numpy.polyfit(counts[0:14],true_counts[0:14],3)	
	print(coefs_inv)

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

def error():
	number = 0
	end_number = 21
	while number < end_number:
		error_0.append((counts[number]-true_counts[number])/true_counts[number])
		number+= 1
		
	number = 0
	end_number = 21
	while number < end_number:
		error_1.append((true_counts_1[number]-true_counts_1[number])/true_counts_1[number])
		number+= 1
	
	number = 0
	end_number = 21
	while number < end_number:
		error_2.append((true_counts_2[number]-true_counts_1[number])/true_counts_1[number])
		number+= 1
	
	number = 0
	end_number = 21
	while number < end_number:
		error_3.append((true_counts_3[number]-true_counts_1[number])/true_counts_1[number])
		number+= 1
	
	number = 0
	end_number = 21
	while number < end_number:
		error_4.append((true_counts_4[number]-true_counts_1[number])/true_counts_1[number])
		number+= 1
	return
	
def print_graph():
	
	#-------------------------------------#
	
	#Prints out raw data

	plt.title('Integration Time vs. Measured Counts',fontsize = 15)
	plt.plot(ints,counts,'k')
	plt.plot(raw_ints,raw_counts,'r')
	
	red_patch = mpatches.Patch(color='red', label='Actual data')
	black_patch = mpatches.Patch(color='black', label='Mean of Data')

	plt.legend(handles=[red_patch,black_patch],bbox_to_anchor=(1, .18))
	plt.ylabel('counts')
	plt.xlabel('integration time (ms)')
	plt.show()
	
	#-------------------------------------#
	
	#Prints out raw data and linear fit to data
	
	plt.title('Ints vs. Measured Counts with Linear Fit',fontsize = 15)
	plt.plot(ints,counts,'k')
	plt.plot(ints,true_counts,'g')

	black_patch = mpatches.Patch(color='black', label='Data')
	green_patch = mpatches.Patch(color='green', label='Linear Fit')

	plt.legend(handles=[black_patch,green_patch],bbox_to_anchor=(1, .18))
	plt.ylabel('counts')
	plt.xlabel('integration time (ms)')
	
	plt.vlines(ints[lower_adj], 0, 60000)
	plt.vlines(ints[upper_adj], 0, 60000)
	plt.axis([0,4000,0,60000]) #This fixes the axes to go from 0-60,000.
	plt.show()
	
	#-------------------------------------#
	
	#Prints out true counts vs counts for desired, second, third, and fourth order relationships
	xarr = numpy.linspace(5000,60000,21)

	plt.plot(xarr,true_counts_1,'k')
	plt.plot(xarr,true_counts_2,'r')
	plt.plot(xarr,true_counts_3,'b')
	plt.scatter(true_counts,counts)
	plt.plot(xarr,true_counts_4,'g')
	plt.vlines(counts[lower_adj], 0, 60000)
	plt.vlines(counts[upper_adj], 0, 60000)
	plt.ylabel('measured counts')
	plt.xlabel('true counts')
	plt.axis([0,60000,0,60000]) #This fixes the axes to go from 0-60,000.
	
	black_patch = mpatches.Patch(color='black', label='Linear Fit')
	red_patch = mpatches.Patch(color='red', label='2nd Order')
	blue_patch = mpatches.Patch(color='blue', label='3rd Order')
	green_patch = mpatches.Patch(color='green', label='4th Order')
	blue_circ_patch = mpatches.Patch(edgecolor='black',facecolor = 'blue', label = 'Original Data')

	plt.legend(handles=[black_patch,red_patch,blue_patch,green_patch,blue_circ_patch],bbox_to_anchor=(1, .36))
	plt.title('True counts vs. measured counts, based on polynomial fit',fontsize = 15)
	plt.show()
		
	#------------------------------------#

	#Prints out true counts vs. error of linearity for desired, second, third, and fourth order relationship
	
	plt.scatter(true_counts,error_0)
	plt.plot(true_counts_1,error_1,'k')
	plt.plot(true_counts_2,error_2,'r')
	plt.plot(true_counts_3,error_3,'b')
	plt.plot(true_counts_4,error_4,'g')
	plt.ylabel('Error of linearity')
	plt.xlabel('true counts')
	plt.vlines(true_counts[lower_adj], -.1, .02)
	plt.vlines(true_counts[upper_adj], -.1, .02)
	plt.title('True counts vs. departure from linearity, based on polynomial fit',fontsize = 13)
	
	black_patch = mpatches.Patch(color='black', label='Linear Fit')
	red_patch = mpatches.Patch(color='red', label='2nd Order')
	blue_patch = mpatches.Patch(color='blue', label='3rd Order')
	green_patch = mpatches.Patch(color='green', label='4th Order')
	blue_circ_patch = mpatches.Patch(edgecolor='black',facecolor = 'blue', label = 'Original Data')


	plt.legend(handles=[black_patch,red_patch,blue_patch,green_patch, blue_circ_patch],bbox_to_anchor=(1, 1))
	plt.axis([0,60000,-.1,.02])

	plt.show()
	
	#------------------------------------#
	
	plt.title('Integration Time vs. Corrected Counts',fontsize = 15)
	plt.scatter(raw_ints,corrected,color = 'black')
	
	xarr = numpy.linspace(0,4000,21)
	yarr = numpy.linspace(4800,61000,21)
	plt.plot(xarr,yarr,'r')
	plt.plot(ints,counts)
	
	black_patch = mpatches.Patch(color='black', label='Corrected data')
	blue_patch = mpatches.Patch(color='blue', label='Original data')


	plt.legend(handles=[black_patch,blue_patch],bbox_to_anchor=(1, .178))
	plt.ylabel('counts')
	plt.xlabel('integration time (ms)')
	plt.axis([0,4000,0,60000])
	plt.show()
	
	#-------------------------------------#
	
	return

open_images()

avg_ints_counts()

make_true_counts()

error()

print_graph()
