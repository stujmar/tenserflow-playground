# numpy is an important library for scientific computing.
import numpy as np
import re

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
# get_pokemon_with_lowest_total()

# drop a column from the dataframe.
def drop_column(column, dataframe):
    dataframe = dataframe.drop(columns=[column], axis=1, inplace=True)

# Create and delete 'Grand Total' column.
poke_df['Grand Total'] = poke_df.iloc[:, 4:10].sum(axis=1)
drop_column('Grand Total', poke_df)

# rearrange columns.
def rearrange_columns(dataframe):
    cols = list(dataframe.columns)
    # careful hard coding, this is not a good way to do this.
    return dataframe[cols[0:4] + [cols[-1]]+cols[4:12]]
# poke_df = rearrange_columns(poke_df)

# save the dataframe to a csv file.
def save_dataframe_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)
# save_dataframe_to_csv(poke_df, './data/pokemon_data_sorted.csv')

# save dataframe to excel file.
def save_dataframe_to_excel(dataframe, filename):
    dataframe.to_excel(filename, index=False)
# save_dataframe_to_excel(poke_df, './data/pokemon_data_sorted.xlsx')

# save as a txt file.
def save_dataframe_to_txt(dataframe, filename):
    dataframe.to_csv(filename, index=False, sep='\t')
# save_dataframe_to_txt(poke_df, './data/pokemon_data_sorted.txt')

# print all pokemon of a given type.
def print_pokemon_by_type(type, dataframe):
    print(dataframe[dataframe['Type 1'] == type])
# print_pokemon_by_type('Grass', poke_df)

# print all pokemon of a given Type 1 and Type 2.
def print_pokemon_by_type_and_type2(type1, type2, dataframe):
    # & = and, | = or.
    print(dataframe[(dataframe['Type 1'] == type1) & (dataframe['Type 2'] == type2)])
# print_pokemon_by_type_and_type2('Grass', 'Flying', poke_df)

# print pokemon with a HP greater than 100 sorted by HP.
def print_pokemon_by_hp_greater_than_100(dataframe):
    print(dataframe[dataframe['HP'] > 100].sort_values('HP', ascending=False))
# print_pokemon_by_hp_greater_than_100(poke_df)

# reset the index of the dataframe.
def reset_index(dataframe):
    # look up drop and inplace in the documentation.
    return dataframe.reset_index(drop=True, inplace=True)
# poke_df = reset_index(poke_df)

# Filter out pokemon with 'Mega' in their name.
def filter_pokemon_by_mega(dataframe):
    return dataframe[dataframe['Name'].str.contains('Mega') == False]
# poke_df = filter_pokemon_by_mega(poke_df)

# Use regex to checks types
def filter_pokemon_by_type_regex(dataframe):
    return dataframe.loc[dataframe['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
# print(filter_pokemon_by_type_regex(poke_df))

# Get all pokemon names that contains with 'pi'.
def get_pokemon_name_contains(dataframe, string):
    return dataframe.loc[dataframe['Name'].str.contains(string + '[a-z]*', flags=re.I, regex=True)]
# print(get_pokemon_name_contains(poke_df, 'pi'))

# Get all pokemon names that starts with 'pi'.
def get_pokemon_names_starting_with(dataframe, string):
    return dataframe.loc[dataframe['Name'].str.contains('^' + string + '[a-z]*', flags=re.I, regex=True)]
# print(get_pokemon_names_starting_with(poke_df, 'pi'))

# Find and replace types. 
def find_and_replace(dataframe, old, new):
    dataframe.loc[dataframe['Type 1'] == old, 'Type 1'] = new
    return dataframe
# print(find_and_replace(poke_df, 'Fire', 'Lava'))

# Make pokemon of a given name Legendary. 
def find_and_replace(dataframe, name):
    dataframe.loc[dataframe['Name'] == name, 'Legendary'] = True
    return dataframe
# find_and_replace(poke_df, 'Magikarp')

# print all pokemon where Name = 'Magicarp'
def print_pokemon_by_name(dataframe, name):
    print(dataframe[dataframe['Name'] == name])
# print_pokemon_by_name(poke_df, 'Magikarp')

# return original dataframe.
def return_original_dataframe():
    return pd.read_csv('./data/pokemon_data.csv')
poke_df = return_original_dataframe()

poke_df.loc[poke_df['Speed'] == 100, ['Generation', 'Legendary']] = "Wow Speedy!"
poke_df = return_original_dataframe()

add_stats()
poke_df = rearrange_columns(poke_df)
print(poke_df)

print(poke_df.groupby(['Type 1']).mean())