# numpy is an important library for scientific computing.
import numpy as np

# matplotlib is a plotting library.
import matplotlib.pyplot as plt

# pandas is a library for data manipulation and analysis.
import pandas as pd

# Load dataset.
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

# The quick brown fox jumps over the lazy dog.

# Import Pokemon data into a dataframe.
poke_df = pd.read_csv('./data/pokemon_data.csv')
poke_df_xlsx = pd.read_excel('./data/pokemon_data.xlsx')

print(poke_df.head(3))
print(poke_df.tail(3))

# print(poke_df_xlsx)