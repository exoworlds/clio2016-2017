1. Read in the cubed files: use previous programming to do this

2. apply linearity correction to all images them while I read them in: apply to every single pixel in the pictur (within a new function in a loop)
  http://stackoverflow.com/questions/37863967/pil-apply-the-same-operation-to-every-pixel

3. Subtract images from each other
  group 1:   1    2   3
  group 2:   4    5   6
  So 1-4, 2-5, 3-6 and so on and so forth

4. Write a fits file to disk, save to computer, open ds9 to look at them, and depending on how far I get, we will either get the peak pixel (which is kind of a shortcut) or we do a different phptometry method to determine how bright the star is.

General help:
  look under Example of working with 3-d FITS cube link on the front page
