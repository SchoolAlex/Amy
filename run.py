# Copyright 2016 TryAmyAI All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Imports from other files
from setup import setup
from start import start
import ran

# Imports from python
import os
import sys

# Get the prefix
pre = "Amy >> "
# Get the text file to see how many times the program has run
txt = open(ran.txt)
ran = txt.read()
# If the program hasn't run before...
if(ran == 0):
    # Go to the setup of the program
    setup()
# If it has....
else:
    # Run basic startup of the program
    start()
