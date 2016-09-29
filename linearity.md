- Find the part of the image that is illuminated
- Find the coordinates of the illuminated region
- Get the median counts in each image within that illuminated region
- Plot against the integration time
- [PyPlot Plotting Tutorial](http://matplotlib.org/users/pyplot_tutorial.html)
- Find a polynomial fit to the integration time vs. counts plot [Example](https://sites.google.com/site/scienceuprising/tools/useful-python-scripts/matplotlib/using-numpy-s-polyfit-in-combination-with-matplotlib-to-fit-data-points)
- How to make an array of integers: [Numpy Arrays](http://www.scipy-lectures.org/intro/numpy/operations.html)

import numpy as np

x = np.arange(100)

y = 12.6 * x + 54.

