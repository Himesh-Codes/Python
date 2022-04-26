#!/usr/bin/env python3
"""
    Decorator used for encode genearate token
"""
import generator

def encodeToken(setToken):
    string = setToken()
    startString = '&ghas6$87887Ggjsd'
    endString = '+{ndfsdfkkdf*'
    
    print(f'Encoded : {startString}{string}{endString}')

for token in generator.tokenGenerator('Himesh', '', 1):
    if token:
        @encodeToken 
        def setToken():
            return token