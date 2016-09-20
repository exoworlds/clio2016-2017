# FITS files for astronomy

FITS = Flexible Image Transport System
One FITS file consists of a Header (info about the exposure, etc = Metadata) and the Data (the image part)

## ds9
ds9 is an application for displaying and working with FITS files.

- Download and install ds9:
    - http://ds9.si.edu/site/Home.html
- Python ds9 -- For working with FITS files from python to ds9: http://hea-www.harvard.edu/RD/pyds9/

    - It is included in the Anaconda distribution
    - How to install at Terminal:
        - sudo python -m pip install --no-deps pyds9
        - See here for more info: https://github.com/ericmandel/pyds9

## Astropy
- Python 2.7, 3.3, 3.4 or 3.5
- Numpy 1.7.0 or later

How to install:
- conda install astropy

## In Python: How to open a FITS file and display it in ds9:

- Set up your data directory as follows:
    - Make a new folder in your home directory called "mypy"
    - Make 2 folders in there, one called "code" and one called "data"
- Set up the paths (point to the "mypy" directory)
- Download the images - Place them in the directory "data"
- How to read in the FITS file:

    - import astropy.io.fits
    - fname = 'data/Linearity00001.fit'
    - hdu1 = astropy.io.fits.open(fname)
    - hdu1.info()
- How to display the FITS file in ds9:

    - from pyds9 import *
    - print(ds9_targets())
        - If says "None" this means you do not have a ds9 session running -- Start up ds9 -- or Quit and re-start ds9
        - If it says something like " ['DS9:ds9 c0a8000f:50436']" then you are good to go
    - d = DS9()
    - d.set_pyfits(hdu1)  #This will display the image in ds9, and it will print "1" to indicate success
- How to look at the header:

    - print(hdu1[0].header)   #The header is easier to look at in ds9 -- Go to File -> Header
    - print(hdu1[0].header["PASSBAND"])   #Prints the passband filter name
    - print(float(hdu1[0].header["INT"]))   #Prints the exposure integration time
- How to get the image into a data array:

    - scidata = hdu1[0].data
- How to print the countrate at a pixel:

    - ds9x = 590
    - ds9y = 144
    - print(scidata[ds9y-1,ds9x-1])
- Open a 2nd image:
    - fname2 = 'data/Linearity00002.fit'
    - hdu2 = astropy.io.fits.open(fname2)
    - hdu2.info()
    - scidata2 = hdu2[0].data

# Photutils
[Using Photutils](http://photutils.readthedocs.org/en/latest/)

How to install:
pip install --upgrade pip
pip install --no-deps photutils

[Overview of its functionality](http://photutils.readthedocs.org/en/latest/photutils/overview.html)

