# ------------------------------------------------- #
# Title: Assignment 07, Pickling
# Description: Create an example code that uses Pickling
# ChangeLog: (Who, When, What)
# Ethan Morgan,08/24/2021,Created Script
# ------------------------------------------------- #

import pickle # import the 'pickle' code to be used in this script

# Dictionary of Floats/Integers, Stringers, and Booleans
dictionary_data = {
    'Floats_or_Integers': [1, 2.0],
    'Strings': ("Activities", "Actions"),
    'Booleans': (True, False)}

# Print the dictionary define previously
print()
print("This is a Dictionary Prior to Being Pickled...")
print(dictionary_data)

# Creates a file or rewrites a file named 'dictionary_data.dat'
# The 'wb' writes the data to a file in binary
with open('dictionary_data.dat', 'wb') as row:
    pickle.dump(dictionary_data, row)

# Opens the binary file and inputs the data in a different dictionary
# The 'load' command pulls the data from the binary file
with open('dictionary_data.dat', 'rb') as row:
    dictionary_data_unbinary = pickle.load(row)

# Print the dictionary to show that the data hasn't changed
print()
print("This is the same Dictionary Post Being Pickled...")
print(dictionary_data_unbinary)
