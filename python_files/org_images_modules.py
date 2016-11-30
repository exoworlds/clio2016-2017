#This seperates all of the actions into distinct modules and runs the program.
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
error_1 = []
error_2 = []
error_3 = []
error_4 = []
error_5 = []
error_6 = []
true_counts = []
lower = 60
lower_adj = 6
upper = 109
upper_adj = 10

def polyfit2():
	#testing to see if polyfit works using a second order equation
	x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	#y = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]
	y = [1,8,27,64,125,216,343,512,729,1000,1331,1728,2197,2744,3375,4096,4913,5832,6859,8000]
	
	test_coefs = []
	true_exp = []

	test_coefs = numpy.polynomial.polynomial.polyfit(x[0:20],y[0:20],3)
	print(str(test_coefs))
	number = 0
	while number < 20:
		true_exp.append(test_coefs[0]+ test_coefs[1]*x[number] + test_coefs[2]*x[number]*x[number] + test_coefs[3]*x[number]*x[number]*x[number])
		number = number + 1

	number = 0
	while number < 20:
		print(true_exp[number] - y[number])
		number = number + 1
	print(str(true_exp))
	print(str(y))
	
	plt.plot(true_exp,error_exp)
	plt.show()
	
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
			#print (str(count)+"\t"+str(i)+"\t"+str(raw_ints[count])+"\t"+str(raw_counts[count])+"\n")
			count += 1
			
		x = 0
		while i == 20 and x < 5:
			raw_ints.append(float(hdu1[0].header["INT"]))
			raw_counts.append(numpy.median(scidata[x,ds9y1:ds9y2,ds9x1:ds9x2]))
			x += 1
			#print (str(count)+"\t"+str(i)+"\t"+str(raw_ints[count])+"\t"+str(raw_counts[count])+"\n")
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
	#coefficients1 = numpy.polyfit(raw_ints[lower:upper],raw_counts[lower:upper],1)
	coefficients1 = [13.9820, 4892.02]
	print(coefficients1)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts_1.append(coefficients1[0]*ints[number] + coefficients1[1])
		number+= 1

	coefficients2 = numpy.polyfit(raw_ints[lower:upper],raw_counts[lower:upper],2)
	print(coefficients2)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts_2.append(coefficients2[0]*ints[number]*ints[number] + coefficients2[1]*ints[number] + coefficients2[2])
		number+= 1

	coefficients3 = numpy.polyfit(raw_ints[lower:upper],raw_counts[lower:upper],3)
	coefficients3 = [4.6*10 **(-11),-1.41* 10 **(-6),1.00273,112.575]
	print(coefficients3)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts_3.append(coefficients3[0]*ints[number]*ints[number]*ints[number] + coefficients3[1]*ints[number]*ints[number] + coefficients3[2]*ints[number] + coefficients3[3])
		number+= 1

	coefficients4 = numpy.polyfit(raw_ints[lower:upper],raw_counts[lower:upper],4)
	number = 0
	end_number = 21
	while number < end_number:
		true_counts_4.append(coefficients4[0]*ints[number]*ints[number]*ints[number]*ints[number] + coefficients4[1]*ints[number]*ints[number]*ints[number] + coefficients4[2]*ints[number]*ints[number] + coefficients4[3]*ints[number] + coefficients4[4])
		number+= 1
	return

def error_true_counts(true_counts):		
	#Make that sweet, sweet initial error array
	error = []
	number = 0
	end_number = 21
	while number < end_number:
		error.append((true_counts[number]-counts[number])/true_counts[number])
		number+= 1
	return error

def print_graph():

	#Prints out true counts vs. error of linearity for desired, second, third, and fourth order relationship
	"""
	plt.plot(true_counts_1,error_1,'k')
	plt.plot(true_counts_2,error_2,'r')
	plt.plot(true_counts_3,error_3,'b')
	#plt.plot(true_counts_4,error_4,'g')
	plt.vlines(counts[lower_adj], -.1, .4)
	plt.vlines(counts[upper_adj], -.1, .4)
	plt.ylabel('Error of linearity')
	plt.xlabel('true counts')
	plt.title('True counts based on linear fit of data between 500ms and 1500 ms vs. departure from linearity',fontsize = 9)
	plt.text(40000,-.08,'Desired relationship: Black, 2nd order polynomial: Red, 3rd order polynomial: Blue', fontsize=7, horizontalalignment='center')
	"""
	#-------------------------------------#
	
	#Prints out true counts vs counts for desired, second, third, and fourth order relationships
	"""
	
	plt.plot(true_counts_1,counts,'k')
	plt.plot(true_counts_2,counts,'r')
	plt.plot(true_counts_3,counts,'b')
	plt.plot(true_counts_4,counts,'g')
	#plt.vlines(counts[lower_adj], 0, 60000)
	#plt.vlines(counts[upper_adj], 0, 60000)
	plt.ylabel('measured counts')
	plt.xlabel('true counts')
	plt.title('True counts based on linear fit of data between 500ms and 1500 ms vs. measured counts',fontsize = 10)
	plt.text(40000,2000,'Desired relationship: Black, 2nd order polynomial: Red, 3rd order polynomial: Blue', fontsize=9, horizontalalignment='center')
	"""
	#-------------------------------------#
	
	#Prints out raw data vs raw counts
	
	plt.title('Ints vs. measured counts',fontsize = 15)
	#plt.text(2500,2000,'Data: Black, Linearity correction: Red',fontsize=9, horizontalalignment='center')
	plt.plot(ints,counts,'k')
	plt.plot(raw_ints,raw_counts,'r')
	

	#Shows graph
	#ax.grid(color='k', linestyle='-', linewidth=2)
	
	
	red_patch = mpatches.Patch(color='red', label='Actual data')
	black_patch = mpatches.Patch(color='black', label='Mean of data')

	plt.legend(handles=[red_patch,black_patch],bbox_to_anchor=(1, .2))
	plt.show()
	return

open_images()

avg_ints_counts()

make_true_counts()

error_1 = error_true_counts(true_counts_1)
error_2 = error_true_counts(true_counts_2)
error_3 = error_true_counts(true_counts_3)
error_4 = error_true_counts(true_counts_4)

print_graph()	

"""
legend
	legend((line1, line2, line3), ('label1', 'label2', 'label3'))

errorbar
	errorbar(x, y, yerr=None, xerr=None,
         fmt='', ecolor=None, elinewidth=None, capsize=None,
         barsabove=False, lolims=False, uplims=False,
         xlolims=False, xuplims=False, errorevery=1,
         capthick=None)

grid
	ax.grid(color='r', linestyle='-', linewidth=2)
"""

