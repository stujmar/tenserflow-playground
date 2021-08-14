from __future__ import absolute_import, division, print_function, unicode_literals

# numpy is an important library for scientific computing.
import numpy as np

# matplotlib is a plotting library.
import matplotlib.pyplot as plt

# pandas is a library for data manipulation and analysis.
import pandas as pd

# IPython.display allows us to display images.
from IPython.display import clear_output

# What is six.moves? 
# six.moves is a library that lets us import code from other libraries.
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc
# tensorflow is a machine learning library.
import tensorflow as tf

# Line of best fit. 
# Line through a scatter plot that best predicts future data points.

# Equation for a line is y=mx+b, where b is the y-intercept and m is the slope.
# Slope is the change in y over change in x, or 'rise' over 'run'.

# function to return y value of a line.
def line_y(x, m, b):
    return m*x + b

# function to return x value of a line.
def line_x(y, m, b):
    return (y-b)/m

# Equation to calucate area of a cylinder.
# pi*r^2*h, where r is radius, h is height.

# function to return area of a cylinder.
def cylinder_area(r, h):
    return np.pi*r**2*h

# area of a cylinder from diameter.
def cylinder_area_from_diameter(d, h):
    return np.pi*(d/2)**2*h
