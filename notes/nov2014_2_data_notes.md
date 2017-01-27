1. Read in the cubed files: use previous programming to do this

2. apply linearity correction to all images them while I read them in: apply to every single pixel in the picture (within a new function, maybe  in a loop)
http://stackoverflow.com/questions/37863967/pil-apply-the-same-operation-to-every-pixel

3. Subtract images from each other
group 1:   1    2   3
group 2:   4    5   6
So 1-4, 2-5, 3-6 and so on and so forth
Maybe numpy can be used to do this, as what you want is a postive star on one side and a negative star on the other side (left and right respectively, I believe?)

4. Write a fits file to disk, save to computer, open ds9 to look at them, and depending on how far I get, we will either get the peak pixel (which is kind of a shortcut) or we do a different phptometry method to determine how bright the star is.

General help:
  look under Example of working with 3-d FITS cube link on the front page

Probably won't get that far due to the need to reprogram many things from scratch, but if I can at least write images that have been subtracted, then that will be a good place to be in my the 22nd. Maybe if I work Monday mornings/afternoons, Wednesday mornings/afternoons, and Friday mornings/afternoons, I can get to 10 hours a week while Katie is gone.

Skype Katie on Fridays
