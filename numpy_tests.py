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
print(a[1, 6])

