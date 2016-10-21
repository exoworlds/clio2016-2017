#This seperates all of the actions into distinct modules and runs the program.

import numpy
import matplotlib.pyplot as plt
from astropy.io import fits

imageAmount = 115
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
error_1 = []
error_2 = []
error_3 = []
error_4 = []
error_5 = []
error_6 = []
true_counts = []
lower = 30
lower_adj = 6
upper = 54
upper_adj = 10
	
def open_images():
	i = 0
	ds9x1 = 33
	ds9x2 = 180
	ds9y1 = 20
	ds9y2 = 180

	while i < imageAmount:
		if i < 9:
			fname = "Linearity0000"+str(i+1)+".fit"
		elif i >= 9 and i <99:
			fname = "Linearity000"+str(i+1)+".fit"
		else:
			fname = "Linearity00"+str(i+1)+".fit"
			
		hdu1 = fits.open(fname)
		scidata = hdu1[0].data
		
		raw_ints.append(float(hdu1[0].header["INT"]))
		raw_counts.append(numpy.median(scidata[ds9x1:ds9x2,ds9y1:ds9y2]))
		
		#print (str(raw_ints[i])+"\t"+str(raw_counts[i])+"\n")
			
		i += 1
	return

def avg_ints_counts():
	five_number = 0
	one_number = 0
	while one_number < 23:
		ints.append(raw_ints[five_number])
		counts.append((raw_counts[five_number]+raw_counts[five_number+1]+raw_counts[five_number+2]+raw_counts[five_number+3]+raw_counts[five_number+4])/5)
		five_number += 5
		one_number += 1
	return
	
def make_true_counts():
	coefficients1 = numpy.polyfit(raw_ints[lower:upper],raw_counts[lower:upper],1)
	number = 0
	end_number = 23
	while number < end_number:
		true_counts_1.append(coefficients1[0]*ints[number] + coefficients1[1])
		number+= 1

	coefficients2 = numpy.polyfit(raw_ints[lower:upper],raw_counts[lower:upper],2)
	number = 0
	end_number = 23
	while number < end_number:
		true_counts_2.append(coefficients2[0]*ints[number]*ints[number] + coefficients2[1]*ints[number]+coefficients2[2])
		number+= 1

	coefficients3 = numpy.polyfit(raw_ints[lower:upper],raw_counts[lower:upper],3)
	number = 0
	end_number = 23
	while number < end_number:
		true_counts_3.append(coefficients3[0]*ints[number]*ints[number]*ints[number] + coefficients3[1]*ints[number]*ints[number]+coefficients3[2]*ints[number] + coefficients3[3])
		number+= 1

	coefficients4 = numpy.polyfit(raw_ints[lower:upper],raw_counts[lower:upper],4)
	number = 0
	end_number = 23
	while number < end_number:
		true_counts_4.append(coefficients4[0]*ints[number]*ints[number]*ints[number]*ints[number] + coefficients4[1]*ints[number]*ints[number]*ints[number] + coefficients4[2]*ints[number]*ints[number] + coefficients4[3]*ints[number] + coefficients4[4])
		number+= 1
	return

def error_true_counts(true_counts):		
	#Make that sweet, sweet initial error array
	error = []
	number = 0
	end_number = 23
	while number < end_number:
		error.append((true_counts[number]-counts[number])/true_counts[number])
		number+= 1
	return error

def print_graph():
	# Feed data into pyplot.
	#plt.plot(true_counts_1,error_1,'k')
	#plt.plot(true_counts_2,error_2,'r')
	#plt.plot(true_counts_3,error_3,'b')
	#plt.plot(true_counts_4,error_4,'g')
	#plt.plot(true_counts_5,error_5,'m')
	#plt.plot(true_counts_6,error_6,'c')
	#plt.vlines(counts[lower], -.2, .4)
	#plt.vlines(counts[upper], -.2, .4)
	#plt.ylabel('Error of linearity')
	#plt.xlabel('true counts')
	#-------------------------------------#
	plt.plot(true_counts_1,counts,'k')
	plt.plot(true_counts_2,counts,'r')
	plt.plot(true_counts_3,counts,'b')
	plt.plot(true_counts_4,counts,'g')
	#plt.plot(true_counts_5,counts,'m')
	#plt.plot(true_counts_6,counts,'c')
	plt.vlines(counts[lower_adj], 0, 60000)
	plt.vlines(counts[upper_adj], 0, 60000)
	plt.ylabel('measured counts')
	plt.xlabel('true counts')

	plt.show()
	return

open_images()
avg_ints_counts()

i = 0
while i < 23:
	print(str(ints[i])+"\t"+str(counts[i])+"\n")
	i += 1
	
make_true_counts()

error_1 = error_true_counts(true_counts_1)
error_2 = error_true_counts(true_counts_2)
error_3 = error_true_counts(true_counts_3)
error_4 = error_true_counts(true_counts_4)


print_graph()	