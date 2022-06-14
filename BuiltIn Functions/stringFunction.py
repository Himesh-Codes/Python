#!/usr/bin/env python3
"""
Built-in string functions
"""

class StringFunction():
    def __init__(self, num):
       self._num = num
        
    # repr method will be return the representation of the object 
    def __repr__(self):
        return f'The number of order is : {self._num}'
    
    # str method will be return the string representation of the object 
    def __str__(self): 
        return f'String: The number of order is : {self._num}'
        
stringOp = StringFunction(22)
# if str special method is presented it will return the value from same, else rep return value is printed
print(stringOp)

# we can print rep using rep()
print(repr(stringOp))

# ascii will be print the unicode of characters in __repr__ function
print(ascii(stringOp))

# chr function prints the character represent by the unicode
print(chr(128400))

# ord gives the unicode number of the character
print(ord('🖐'))
