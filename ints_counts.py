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
	
	print (str(ints[i])+"\t"+str(counts[i])+"\n")
	
	i += 1

#Best fit line, from 0 ints to 2000 ints

# Use polyfit - 1st order
coefficients1 = numpy.polyfit(ints[0:65],counts[0:65],1)
print (coefficients1)
polynomial1 = numpy.poly1d(coefficients1)

# Feed data into pyplot.
xpoints = numpy.linspace(0.0,5000.0,10000)
plt.plot(ints[0:114],counts[0:114],xpoints,polynomial1(xpoints))
plt.ylabel('counts')
plt.xlabel('ints')

plt.show()