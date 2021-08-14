from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc
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
