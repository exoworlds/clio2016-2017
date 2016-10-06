#This compares a linear line from 0 to 2000 ints and extrapolates that to encompass all of the data set to show the regression

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
		
	i += 1

# Use polyfit - 1st order - on original data
coefficients1 = numpy.polyfit(ints[15:55],counts[15:55],1)

number = 0
end_number = 115
true_counts = []

while number < end_number:
	true_counts.append(coefficients1[0]*ints[number] + coefficients1[1])
	number+= 1
	
#Use a polyfit on the original true counts/measured counts graph
coefficients2 = numpy.polyfit(true_counts[15:80],counts[15:80],2)
polynomial_lin = numpy.poly1d(coefficients2)
xpoints = numpy.linspace(0,60000,500)

# Feed data into pyplot.
plt.plot(true_counts,counts,'k')
plt.plot(xpoints,polynomial_lin(xpoints),'r')
plt.ylabel('measured counts')
plt.xlabel('true counts')

plt.show()