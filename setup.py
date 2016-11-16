# Owner: TryAmyAI

# Imports from other files
from createUsr import newUser
import usrNum

# Imports from python
import os
import sys
import tempfile
import time

def setup():
    # Get the prefix
    pre = "Amy >> "

    # Get the text that has the number of users
    txt = open(usrNum.txt)
    num = txt.read()
    # If there isn't any other users...
    if(num == 0):
        # There isn't any other user, go to create another one.
        print(pre + "I show that no user exists. Please create a user.")
        # Give the user time to read
        time.sleep(3)
        # Create a user
        createUsr.newUser()
    # If there is...
    else:
        # There is another user, go to the next step
        print(pre + "We show that at least one user already exists. Moving to next step.")
        # Give the user time to read
        time.sleep(4)

setup()
