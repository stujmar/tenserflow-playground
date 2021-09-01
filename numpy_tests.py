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

def change_column(array, column, new_value):
    array[:, column] = new_value
    print(array)
# change_column(a, 1, 99)

def change_row(array, row, new_value):
    array[row, :] = new_value
    print(array)
# change_row(a, 0, 99)

three_dee = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(three_dee)
# print(three_dee[0,1,1])

# function to print an array of zeros.
def print_zeros(x):
    print(np.zeros(x))
# print_zeros(3)

# function to print a two dimensional array of zeroes.
def print_zeros_2d(x, y):
    print(np.zeros((x, y)))
# print_zeros_2d(2, 3)

# function to print a three dimensional array of ones.
def print_ones(x, y, z):
    print(np.ones((x, y, z), dtype='int32'))
# print_ones(3, 2, 1)

# function to print a 2d array of n number.
def print_n(x, y, n):
    print(np.full((x, y), n, dtype='int32'))
# print_n(3, 2, 99)

four_array = np.full_like(a, 4)
# print(four_array)

# a function to print an array of random numbers.
def print_random(x, y):
    print(np.random.random((x, y)))
# print_random(3, 2)

# a function to print an array of random numbers, with a specific range.
def print_random_range(max, value):
    print(np.random.randint(max, size=(value, value)))
# print_random_range(10, 5)

# print an identity matrix.
def print_identity(x):
    print(np.identity(x))
# print_identity(5)

arr = np.array([1, 2, 3])
# function to repeat an array x times.
def print_repeat(x):
    print(np.repeat(arr, x))
# print_repeat(3)

arr_two = np.array([[1, 2, 3]])
def print_repeat_2d(x):
    print(np.repeat(arr_two, x, axis=0))
# print_repeat_2d(3)

# Code challenge
our_array = np.zeros((5, 5))
our_array[:, 0] = 1
our_array[:, 4] = 1
our_array[0, :] = 1
our_array[4, :] = 1
our_array[2, 2] = 9
# print(our_array)

# Suggested solution.
output = np.ones((5, 5))
core = np.zeros((3, 3))
core[1, 1] = 9
output[1:-1, 1:-1] = core
# print(output)

a = np.array([1, 2, 3, 4, 5])
b = a
b[0] = 99
# a is a reference to the same array as b!
# print(a, b)

c = np.array([1, 2, 3, 4, 5])
d = c.copy()
d[0] = 99
# now there is an actual copy of the array.
# print(c, d)


e = np.array([1, 2, 3, 4, 5])
# a function to add to an array.
def adding_to_array(array, n):
    array += n
    print(array)
# adding_to_array(e, 10)

# a function to add two arrays. 
def add_two_arrays(array1, array2):
    array1 += array2
    print(array1)
f = np.array([1, 2, 3, 4, 5])
g = np.array([5, 4, 3, 2, 1])
# add_two_arrays(f, g)
