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
