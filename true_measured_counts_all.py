#This gives a second order error whaaaa

import numpy
import matplotlib.pyplot as plt
from astropy.io import fits

imageAmount = 115
ints = []
counts = []

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
	
	ints.append(float(hdu1[0].header["INT"]))
	
	counts.append(numpy.median(scidata[ds9x1:ds9x2,ds9y1:ds9y2]))
	
	print (str(ints[i])+"\t"+str(counts[i])+"\n")
	
	i += 1

#Best fit line, from 0 ints to 2000 ints

# Use polyfit - 1st order
coefficients1 = numpy.polyfit(ints[0:65],counts[0:65],1)
print (coefficients1)
polynomial1 = numpy.poly1d(coefficients1)

number = 0
end_number = 114
best_counts1 = []

while number < end_number:
	best_counts1.append(coefficients1[0]*ints[number] + coefficients1[1])
	number+= 1
	
number = 0
end_number = 114
error_lin1 = []

while number < end_number:
	error_lin1.append((best_counts1[number] - counts[number])/(best_counts1[number]))
	number += 1

# Use polyfit - 2nd order
coefficients2 = numpy.polyfit(ints[0:65],counts[0:65],2)
print (coefficients2)
polynomial2 = numpy.poly1d(coefficients1)

number = 0
end_number = 114
best_counts2 = []

while number < end_number:
	best_counts2.append(coefficients2[0]*ints[number]*ints[number] + coefficients2[1]*ints[number] + coefficients2[2])
	number+= 1
	
number = 0
end_number = 114
error_lin2 = []

while number < end_number:
	error_lin2.append((best_counts2[number] - counts[number])/(best_counts2[number]))
	number += 1

	
# Use polyfit - 3rd order
coefficients3 = numpy.polyfit(ints[0:65],counts[0:65],3)
print (coefficients3)
polynomial3 = numpy.poly1d(coefficients1)

number = 0
end_number = 114
best_counts3 = []

while number < end_number:
	best_counts3.append(coefficients3[0]*ints[number]*ints[number]*ints[number] + coefficients3[1]*ints[number]*ints[number] + coefficients3[2]*ints[number] + coefficients3[3])
	number+= 1
	
number = 0
end_number = 114
error_lin3 = []

while number < end_number:
	error_lin3.append((best_counts3[number] - counts[number])/(best_counts3[number]))
	number += 1

	
# Use polyfit - 4th order
coefficients4 = numpy.polyfit(ints[0:65],counts[0:65],4)
print (coefficients4)
polynomial4 = numpy.poly1d(coefficients1)

number = 0
end_number = 114
best_counts4 = []

while number < end_number:
	best_counts4.append(coefficients4[0]*ints[number]*ints[number]*ints[number]*ints[number] + coefficients4[1]*ints[number]*ints[number]*ints[number] + coefficients4[2]*ints[number]*ints[number] + coefficients4[3]*ints[number] + coefficients4[4])
	number+= 1

number = 0
end_number = 114
error_lin4 = []

while number < end_number:
	error_lin4.append((best_counts4[number] - counts[number])/(best_counts4[number]))
	number += 1

	
##########################################################################################################################
# Feed data into pyplot.
xpoints = numpy.linspace(0.0,5000.0,2000)
plt.plot(best_counts1[0:114],counts[0:114],'b')
plt.plot(best_counts2[0:114],counts[0:114],'g')
plt.plot(best_counts3[0:114],counts[0:114],'m')
plt.plot(best_counts4[0:114],counts[0:114],'r')
plt.ylabel('measured counts')
plt.xlabel('true counts')
plt.title('Best fit polynomials shaped to original data',fontsize = 40)
plt.text(40000,100,'Desired: Blue, Quadratic: Green, Cubic: Magenta, Quartic: Red', fontsize=20, horizontalalignment='center')

plt.show()