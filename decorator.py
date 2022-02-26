#!/usr/bin/env python3
"""
    Decorator used for encode genearate token
"""
import generator

def encoder(encode):
    encode()
def encodeToken(string):
    startString = '&ghas6$87887Ggjsd'
    endString = '+{ndfsdfkkdf*'
    
    return f'{startString}{string}{endString}'

for token in generator.tokenGenerator('Himesh'):
    if token:
        @encodeToken 
        encoder