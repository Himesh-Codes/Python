#!/usr/bin/env python3
"""
Example hello world 
"""
import platform

print("Hello World!!!")
name = input("What is your name")
print("Welcome!!, ", name)

# binding of variable in string
print("This is a python version {}". format(platform.python_version())) 

#from Python 3.6 - F stands for formatting
print(f'WELCOME!!! {name}')
