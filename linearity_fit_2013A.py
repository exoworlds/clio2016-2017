# This program was originally called org_images_modules.py by Chris Bohlman.
# I am modifying it to try running it myself - Katie Morzinski, 2016/11/29.
import matplotlib.patches as mpatches
import numpy
import matplotlib.pyplot as plt
from astropy.io import fits


## Values from IDL
ints_uniq = numpy.array([43.0000,100.000,150.000,200.000,300.000,400.000,500.000,750.000,1000.00,1250.00,1500.00,1750.00,2000.00,2250.00,2500.00,2750.00,3000.00,3250.00,3500.00,3750.00,4000.00])
counts_mean = numpy.array([5470.80,6239.40,6931.00,7630.10,9034.70,10446.9,11858.9,15388.0,18899.9,22385.8,25837.5,29225.3,32558.6,35832.9,39044.7,42172.1,45193.2,48096.0,50914.0,52842.4,53251.4])
## IDL
#idx = [4,5,6,7]
#counts_true = 4799.487488d0+ints_uniq*14.1182108d0
#coeff1 = linfit(counts_true[idx], counts_mean[idx])
#print,coeff1,abs(1-coeff1[1])
#   1.1378324e-07       1.0000009
#   8.5524125e-07
counts_true = numpy.array([5406.5706,6211.3086,6917.2191,7623.1296,9034.9507,10446.772,11858.593,15388.146,18917.698,22447.251,25976.804,29506.356,33035.909,36565.462,40095.014,43624.567,47154.120,50683.673,54213.225,57742.778,61272.331])


## Find fits
idx0 = numpy.where((counts_true > 9e3) & (counts_true < 1.6e4))
coeff1 = numpy.polyfit(counts_true[idx0], counts_mean[idx0], 1)
num = 0
end = 60000
xarr = range(num,end,1) #range([start], stop[, step])
yarr1 = []
for i in xarr:
	yarr1.append(coeff1[0]*xarr[i] + coeff1[1])


idx = numpy.where((counts_true > 1e3) & (counts_true < 5e4))
coeff2 = numpy.polyfit(counts_true[idx], counts_mean[idx], 2)
yarr2 = []
for i in xarr:
	yarr2.append(coeff2[0]*xarr[i]*xarr[i] + coeff2[1]*xarr[i] + coeff2[2])


coeff3 = numpy.polyfit(counts_true[idx], counts_mean[idx], 3)
yarr3 = []
for i in xarr:
	yarr3.append(coeff3[0]*xarr[i]*xarr[i]*xarr[i] + coeff3[1]*xarr[i]*xarr[i] + coeff3[2]*xarr[i] + coeff3[3])


coeff4 = numpy.polyfit(counts_true[idx], counts_mean[idx], 4)
yarr4 = []
for i in xarr:
	yarr4.append(coeff4[0]*xarr[i]*xarr[i]*xarr[i]*xarr[i] + coeff4[1]*xarr[i]*xarr[i]*xarr[i] + coeff4[2]*xarr[i]*xarr[i] + coeff4[3]*xarr[i] + coeff4[4])

coeff5 = numpy.polyfit(counts_true[idx], counts_mean[idx], 5)
yarr5 = []
for i in xarr:
	yarr5.append(coeff5[0]*xarr[i]*xarr[i]*xarr[i]*xarr[i]*xarr[i] + coeff5[1]*xarr[i]*xarr[i]*xarr[i]*xarr[i] + coeff5[2]*xarr[i]*xarr[i]*xarr[i] + coeff5[3]*xarr[i]*xarr[i] + coeff5[4]*xarr[i] + coeff5[5])


## Plot it
plt.scatter(counts_true,counts_mean)
plt.plot(xarr,yarr1)
plt.plot(xarr,yarr2,'r')
plt.plot(xarr,yarr3,'g')
plt.plot(xarr,yarr4,'m')
plt.plot(xarr,yarr5,'y')
plt.xlabel('True counts')
plt.ylabel('Measured counts')
#plt.title('True counts based on linear fit of data between 500ms and 1500 ms vs. departure from linearity',fontsize = 9)
#plt.text(40000,-.08,'Desired relationship: Black, 2nd order polynomial: Red, 3rd order polynomial: Blue', fontsize=7, horizontalalignment='center')
plt.axis([0,60000,0,60000]) #This fixes the axes to go from 0-60,000.
blue_patch = mpatches.Patch(color='blue', label='Data; Linear fit')
red_patch = mpatches.Patch(color='red', label='2nd-order Poly fit')
green_patch = mpatches.Patch(color='green', label='3rd-order Poly fit')
purple_patch = mpatches.Patch(color='magenta', label='4th-order Poly fit')
yellow_patch = mpatches.Patch(color='yellow', label='5th-order Poly fit')
plt.legend(handles=[blue_patch,red_patch,green_patch,purple_patch,yellow_patch],bbox_to_anchor=(1, .2))
plt.show()


## Now the departure from linearity (to zoom in and see which polynomial fits the best)
yarr1err = []
for i in xarr:
	yarr1err.append((yarr1[i]-yarr1[i])/yarr1[i])

yarr2err = []
for i in xarr:
	yarr2err.append((yarr2[i]-yarr1[i])/yarr1[i])

yarr3err = []
for i in xarr:
	yarr3err.append((yarr3[i]-yarr1[i])/yarr1[i])

yarr4err = []
for i in xarr:
	yarr4err.append((yarr4[i]-yarr1[i])/yarr1[i])

yarr5err = []
for i in xarr:
	yarr5err.append((yarr5[i]-yarr1[i])/yarr1[i])


## Plot it
plt.plot(xarr,yarr1err)
plt.plot(xarr,yarr2err,'r')
plt.plot(xarr,yarr3err,'g')
plt.plot(xarr,yarr4err,'m')
plt.plot(xarr,yarr5err,'y')
plt.xlabel('True counts')
plt.ylabel('Departure from linearity')
#plt.title('True counts based on linear fit of data between 500ms and 1500 ms vs. departure from linearity',fontsize = 9)
#plt.text(40000,-.08,'Desired relationship: Black, 2nd order polynomial: Red, 3rd order polynomial: Blue', fontsize=7, horizontalalignment='center')
plt.axis([0,60000,-0.1,0.1])
blue_patch = mpatches.Patch(color='blue', label='Data; Linear fit')
red_patch = mpatches.Patch(color='red', label='2nd-order Poly fit')
green_patch = mpatches.Patch(color='green', label='3rd-order Poly fit')
purple_patch = mpatches.Patch(color='magenta', label='4th-order Poly fit')
yellow_patch = mpatches.Patch(color='yellow', label='5th-order Poly fit')
plt.legend(handles=[blue_patch,red_patch,green_patch,purple_patch,yellow_patch],bbox_to_anchor=(1, .2))
plt.show()
