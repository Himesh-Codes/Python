#!/usr/bin/env python3
"""
Object/Class functions
"""

accountNumber = 'AC12121222090'
# return the class of the object
aType = type(accountNumber)

# check the object refers to any class instance, return True/False
aInstance = isinstance(accountNumber, int)

print(accountNumber)
print(aType)
print(aInstance)