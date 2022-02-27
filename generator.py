#!/usr/bin/env python3
"""
    Generator used for genearate token
"""
import random
import string


def tokenGenerator(*args):
    count = 5
    name = ''
    specialToken = ''

    if len(args) < 1:
        raise TypeError('Expected one argument first arg as name')
    elif len(args) == 1:
        name = args[0]
    elif len(args) == 2:
        specialToken = args[1]
    elif len(args) == 3:
        name = args[0]
        count = args[2]
    else:
        raise TypeError('maximum 3 argument')
     
    while count != 0:
        count -= 1
        randomcode = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        yield f'{name}-{randomcode}-{specialToken}' 
        
for token in tokenGenerator('TimS'):
    print(token)
    