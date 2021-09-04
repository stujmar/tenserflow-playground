import numpy as np

# Starting a TensorFlow Tutorial from
# https://www.youtube.com/watch?v=tpCFfeUEGs8

# What is deep learning?
# Multiple layers of processing to extract information from data.
# Machine learning is data into numbers and pulling out patterns.

# (AI(ML(NN))) (AI(ML(DL))) Neural Nets, Deep Learning, within Machine Learning.
# Provide Data and Outcome and ML/DL will provide the rules/path to get there.

# Example with a self driving car all the rules would be too much to type.
# If you can build a simple rule based system don't use ML.
# Google's ML guide https://developers.google.com/machine-learning/guides

# Lots of data and room for error, then ML is good for you.

# ML likes structured data. Columns = Features.
common_ml_algorithms = ["random forest", "naive bayes", "nearest neighbour", "support vector machine", "many more"]
shallow_algorithms = common_ml_algorithms
common_dl_algorithms = ["neural networks", "fully connected neural network", "convolution nn", "recurrent nn", "transformer"]
# DL works well on unstructured data, loose text, video, audio.

# What are Neural Networks.

# Numerical encoding aka a tensor.
 
inputs = np.array([[116, 78, 15], [117, 43, 96], [125, 87, 23]])

# Anatomy of a Neural Network.
# 1 inputs
# 2 something in the middle.
# 3 outputs

# Types of Learning
# 1 Supervised Learning
# 2 Semi-supervised Learning
# 3 Tranfer Learning