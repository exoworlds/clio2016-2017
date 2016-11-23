#disorganized code

import numpy
import matplotlib.pyplot as plt
from astropy.io import fits

imageAmount = 21
raw_ints = []
raw_counts = []
ints = []
counts = []
numpy_ints = []
numpy_counts = []
true_counts_1 = []
true_counts_2 = []
true_counts_3 = []
true_exp = []
error_exp = []
error_1 = []
error_2 = []
error_3 = []
error_4 = []
error_5 = []
error_6 = []
lower = 60
lower_adj = 6
upper = 109
upper_adj = 10
	
i = 0
count = 0
ds9x1 = 200
ds9x2 = 350
ds9y1 = 0
ds9y2 = 200

#testing to see if polyfit works using a second order equation
"""
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#y = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]
y = [1,8,27,64,125,216,343,512,729,1000,1331,1728,2197,2744,3375,4096,4913,5832,6859,8000]


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
	
#plt.plot(true_exp,error_exp)
#plt.show()
"""

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
		#print (str(raw_ints[count])+"\t"+str(raw_counts[count])+"\n")
		count += 1
			
	x = 0
	while i == 20 and x < 5:
		raw_ints.append(float(hdu1[0].header["INT"]))
		raw_counts.append(numpy.median(scidata[x,ds9y1:ds9y2,ds9x1:ds9x2]))
		x += 1
		#print (str(raw_ints[count])+"\t"+str(raw_counts[count])+"\n")
		count += 1
	i += 1

numpy_ints = numpy.array(raw_ints)
numpy_counts = numpy.array(raw_counts)
xvalues = numpy.linspace(0,4000,21)

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

numpy_mean_counts = numpy.array(counts)

coefs = numpy.polynomial.polynomial.polyfit(numpy_ints[lower:upper],numpy_counts[lower:upper],1)
coefs = [ 4892.02, 13.9820]
print(coefs)
ffit = numpy.polynomial.polynomial.polyval(xvalues, coefs)
number = 0
end_number = 21
while number < end_number:
	true_counts_1.append(coefs[0]+ coefs[1]*ints[number] )
	number+= 1
true_counts = numpy.array(true_counts_1)
error = (true_counts - numpy_mean_counts)/true_counts

coefs2 = numpy.polynomial.polynomial.polyfit(numpy_ints[lower:upper],numpy_counts[lower:upper],2)
#print(coefs2)
ffit2 = numpy.polynomial.polynomial.polyval(xvalues, coefs2)
number = 0
end_number = 21
while number < end_number:
	true_counts_2.append(coefs2[0]+ coefs2[1]*ints[number] + coefs2[2]*ints[number]*ints[number])
	number+= 1
true_counts_np = numpy.array(true_counts_2)
error2 = (true_counts_np - numpy_mean_counts)/true_counts_np

coefs3 = numpy.polynomial.polynomial.polyfit(numpy_ints[lower:upper],numpy_counts[lower:upper],3)
#print(coefs3)
ffit3 = numpy.polynomial.polynomial.polyval(xvalues, coefs3)
number = 0
end_number = 21
while number < end_number:
	true_counts_3.append(coefs3[0]+ coefs3[1]*ints[number] + coefs3[2]*ints[number]*ints[number] + coefs3[3]*ints[number]*ints[number]*ints[number])
	number+= 1
true_counts_np_2 = numpy.array(true_counts_3)
error3 = (true_counts_np_2 - numpy_mean_counts)/true_counts_np_2

#printing out linear relationship of true counts vs just the measured counts

plt.plot(true_counts,counts,'b')
plt.plot(true_counts,true_counts,'g')

plt.ylabel('true counts')
plt.xlabel('measured counts')
plt.title('True Counts vs. Counts',fontsize = 10)

plt.show()






