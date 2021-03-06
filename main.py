import os
import tensorflow as tf
import cProfile

print(__name__)

# Print version of tensor.
def print_tensor_version():
    print(tf.version)
# print_tensor_version

# Checks whether the current thread has eager execution enabled.
# This reduces features and boiler plate to make it easy to get started and debug OTF
def check_if_eager():
    tf.executing_eagerly()
# check_if_eager()

# Creating Tensors (Rank 0)
string = tf.Variable("this is a string", tf.string)
integer = tf.Variable(123, tf.int16)
float = tf.Variable(3.21, tf.float32)

# Rank/Degree of Tensors
rank1_tensor = tf.Variable(["Test", "Data", "Here"], tf.string)
rank2_tensor = tf.Variable([["rank", "one"],["rank", "two"]], tf.string)

print("checking rank")
print(tf.rank(rank2_tensor))

print("checking shape")
print(tf.shape(rank2_tensor))

t = tf.zeros([5,5,5,5])
print(tf.shape(t))
# print(t)

my_tensor = tf.ones([5,5,5,5])
# print(my_tensor)
reshaped = tf.reshape(t, [625])
print(reshaped)
print(tf.reshape(reshaped, [125, -1]))