#!/usr/bin/env python3
"""
Module library for python
"""
# https://docs.python.org/3/library/index.html

import os
import random
import sys
from saytime import Saytime

def currentPlatform():
    plaformDetails = sys.version_info
    print('Python version: {}.{}.{}'.format(*plaformDetails))
    print(sys.platform)
    print(os.name)
    # env path for python
    print(os.getenv('PATH'))
    # get current working directory
    print(os.getcwd())
    # random integer
    print(random.randint(1, 999))
    rollNum = list(range(25))
    print(rollNum)
    # shuffle items on an iterable
    random.shuffle(rollNum)
    print(rollNum)
    printTime()
    
def printTime():
    Saytime(12, 21)

if __name__ == '__main__': currentPlatform()
    