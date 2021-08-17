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

# print(poke_df.head(3))
# print(poke_df.tail(3))

# Adding a delimiter, but it breaks the print formatting.
poke_delimited = pd.read_csv('./data/pokemon_data.csv', delimiter='\t')
# print(poke_delimited.head(5))

# Print the column headers of the dataframe.
def print_column_headers():
    print(poke_df.columns)

# Read individual column of the dataframe.
def print_names():
    print(poke_df['Name'])

# print name and id of each pokemon. in poke_df.
def print_name_and_id():
    for row in poke_df.iterrows():
        print(row['Name'], 'is number', row['#'])

# print a range of rows, inclusive of start and end numbers.
def print_range(start, end):
    print(poke_df.iloc[start:(end + 1)])

# compare two attributes of each pokemon.
def print_two_attributes(attribute1, attribute2):
    print(poke_df[[attribute1, attribute2]])    

# print a list of attributes of each pokemon.
def print_n_attributes(n, list_of_attributes):
    print(poke_df[list_of_attributes].iloc[0:n])

# print_n_attributes(5, ['Name', 'Attack', 'Defense', 'Legendary'])

# get any data out of each row of the dataframe.
def print_any_data(): 
    for index, row in poke_df.iterrows():
        print(row['Name'], 'is number', row['#'], 'and has', row['Type 1'], 'type')

# print_any_data()

# print a pokemon of a given Name.
def print_pokemon_by_name(name):
    # I don't 100% understand this, but it works.
    print(poke_df[poke_df['Name'] == name])

# print_pokemon_by_name('Bulbasaur')

# finding information about a pokemon.
def access_rows_by_attribute(attribute, value):
    print(poke_df.loc[poke_df[attribute] == value])

# access_rows_by_attribute('Type 1', 'Grass')

# Describe the data.
def describe_data():
    print(poke_df.describe())   
# describe_data()

# sort values by HP and print the dataframe.
def sort_by_attribute(attribute):
    print(poke_df.sort_values(attribute, ascending=False))
# sort_by_attribute('HP')

# sort by two values and print the dataframe.
def sort_by_two_attributes(attribute1, attribute2):
    print(poke_df.sort_values([attribute1, attribute2], ascending=[True, False]))
# sort_by_two_attributes('Type 1', 'Attack')

# add_stats() adds a new column to the dataframe.
def add_stats():
    poke_df['Total'] = poke_df['HP'] + poke_df['Attack'] + poke_df['Defense'] + poke_df['Sp. Atk'] + poke_df['Sp. Def'] + poke_df['Speed']
add_stats()

# get pokemon with the highest total.
def get_pokemon_with_highest_total():
    print(poke_df.sort_values('Total', ascending=False).head(10))
# get_pokemon_with_highest_total()

# get pokemon with the lowest total.
def get_pokemon_with_lowest_total():
    print(poke_df.sort_values('Total', ascending=True).head(10))
get_pokemon_with_lowest_total()