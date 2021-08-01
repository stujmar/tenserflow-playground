import os
import tensorflow as tf
import cProfile

print(tf.version)
tf.executing_eagerly()
print('tesnorflow executed')

# Creating Tensors
string = tf.Variable("this is a string", tf.string)
integer = tf.Variable(123, tf.int16)
float = tf.Variable(3.21, tf.float32)