import numpy as np
import sys

# NumPy is a multi-dimensional array object, similar to a list.
# NumPy is much faster than Python lists.

# Int32 holds 4 bytes, or 32 bits. 00000000 00000000 00000000 00000000
# Int8 holds 1 byte, or 8 bits. 00000000

# Python list hold Size, Reference, Value, Object Type. While Numpy only hold values.
# Python list is mutable, while Numpy is not? Fact check this is it from github copilot.

# Numpy is contiguous (all values in one place). Python list is not.
# a Python list is a bunch of pointers to where the data is stored.

# Numpy can to additions deletions etc as can Python lists, but Numpy can do much more.
# Mathlab Pandas and Scipy are other packages that use Numpy? double check this.

one_dimensional_array = np.array([1, 2, 3, 4]) # one dimensional array.
def print_one_dimensional_array():
    print(one_dimensional_array)
    print("dimension(s):", one_dimensional_array.ndim)
    print("shape:", one_dimensional_array.shape)
    print("type:", one_dimensional_array.dtype)
    print("size:", one_dimensional_array.size)
# print_one_dimensional_array()

two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6]]) # two dimensional array.
def print_two_dimensional_array():
    print(two_dimensional_array)
    print("dimension(s):", two_dimensional_array.ndim)
    print("type:", two_dimensional_array.dtype)
    print("size:", two_dimensional_array.size)
# print_two_dimensional_array()

three_dimensional_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # three dimensional array.
def print_three_dimensional_array():
    print(three_dimensional_array)
    print("dimension(s):", three_dimensional_array.ndim)
    print("type:", three_dimensional_array.dtype)
    print("size:", three_dimensional_array.size)
# print_three_dimensional_array()

# .itemsize x .size = .nbytes

# establish a 2d array with a shape of (2, 7)
a = np.array([[1, 2, 3, 4, 5 ,6 ,7], [ 8, 9, 10, 11, 12, 13, 14]])

# check the shape
print(a.shape)

# get a specific element/entry array[row, column]
# prints the last element
print(a[1, 6])
# prints 14

# print an element with negative index
# prints the last element
print(a[-1, -1])
# prints 14

# print a whole row
print(a[0, :])
# prints [1 2 3 4 5 6 7]

# print a whole column
print(a[:, 2])
# print [3, 10]

# Getting a little more advanced. [start:stop:step]
print(a[0, 1:6:2])
# prints [2, 4, 6]

# made a function to change an element in the 2 dimensional array
def change_element(array, row, column, new_value):
    array[row, column] = new_value
    print(array)
# change_element(a, 0, 0, 99)
