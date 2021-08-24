# Intro to Programming (Python), Assignment 07

Ethan Morgan, 08/24/2021

## Introduction

Assignment 07 provided an opportunity to working error handling and ‘pickling’ in Python.
I chose to split up the error handling and ‘pickling’ examples into two different scripts.
This was done to explain clearly how each aspect is used in Python.

## Error Handling Script

Error handling is important in scripting because it provides the user a better way understand
errors that may arise in the code.  The example I chose to use was a script that would not
error out if the user’s input was not what was expected.  Figure 1 shows the 
‘Assignment07_ErrorHandling.py’ script.  The script includes multiple comments that provides
guidance through the code and how it it runs.

```
# ------------------------------------------------- #
# Title: Assignment 07, Error Handling
# Description: Create an example code with error handling
# ChangeLog: (Who, When, What)
# Ethan Morgan,08/24/2021,Created Script
# ------------------------------------------------- #

# This script provides an example of error handling in Python.
# It takes user input, but the script requires a numeric input.
# The script uses a try/except error handling to deal with wrong inputs.
# If a string is input, the code will request a new input until a number input.

while True: # 'while' statement used to continue to ask for user input
    print() # print blank line for output clarity
    print("Input a Float Value Below!")
    user_input = input("Input Value: ") # user input requested
    try:
        user_input_float = float(user_input) # converts user input into float type data
        # note, if a string is input for 'user_input' the code skips to the 'except' below
        print() # print blank line for output clarity
        print("The Float Value You Entered Was: ",user_input_float) # print out user float input
        print("Congrats you Entered a Float Value and Not a String!") # print feedback user did it correct
        break # 'break' used to stop code once user input was correct
    except:
        print() # print blank line for output clarity
        # the user's input was not a float or integer
        print("Your Input of",user_input,"is a String!") # print feedback user didn't input correctly
        print("Please Input a Number, Not a String!") # print feedback user didn't input correctly
```
Figure 1 'Assignment07_ErrorHandling.py' Script

A ‘while’ loop is used continually ask the user to input a numeric value.  Then a ‘try/except’
error handling capability is used to prevent the script from erroring out if the user inputs
something other than a numeric value.  If the user inputs a string, the first line of code in
the ‘try’ clause will push the user into the ‘except’ clause and inform the user input a number,
not a string.

## Pickling Script


## Summary

Assignment 07 provided us to work with ‘try/except’ statements and using Pickle as a way of
working with binary files.
