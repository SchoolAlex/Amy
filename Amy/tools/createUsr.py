# Owner: TryAmyAI

# Imports from other files
from createUrs import newUser
import usrNum

# Imports from python
import os
import sys
import tempfile
import time

def newUser():
    # Get the prefix
    pre = "Amy >> "
    # Welcome message
    print(pre + "Welcome! You are here to create a new user.")
    # Get inputs for user creation
    usrN = input(print(pre + "Please enter a username for the new user: "))
    usrP = input(print(pre + "Please enter a password for the new user: "))
    usrC = input(print(pre + "Please enter an all-digit passcode for the new user: "))
    # Get the file with the number of users in it
    txt = open(usrNum.txt)
    uN = txt.read()
    # If there aren't any other users...
    if(uN == 0):
        # Get the confirmation that this will be the admin
        conf = input(print(pre + "This is the first user. They will become the admin user. Is that ok?"))
        # If they disagree...
        if(conf.lower() == "no"):
            # Send them back to the creating of the user.
            print(pre+"Ok. Bringing you back to the creating a user page.")
            # Wait a bit to give them time to read the message
            time.wait(3)
            # Send them to the function of creating the user again
            newUser()
        # If there are other users...
        else:
            # Continue
            print(pre + "Great! Continuing on...")
    else:
        # Create the user anyways...
        print("User created!")

newUser()
