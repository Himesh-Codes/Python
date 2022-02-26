from decimal import *

#!/usr/bin/env python3
"""
Training for types and values
"""

Companyname = 'x'
print(type(Companyname))

companyAddress = '''
                    10 th Avenu, 445D
                    LA, Sanfransisco
                '''
print(f'The company address is {companyAddress}')

# since every thing are object in python we can do every operation as object form
companyAlterName = 'XYZ'.lower()
print('Company alter name : {}'.format(companyAlterName))

# String with spaces using format positional arguments
"""
 - 1 & 0 are the index for th positions for values in format
 - The full colon after the index used for spacing >, < are used for left or right position of variable for spacing
 - Even the single qoutes are printed without escape
 - If we give zero in front of index it will be printed
"""
registercode = "WWW '{1:<7}' '{0:>6}'".format(9, 8)
print(registercode)
registercode = "WWW '{1:<07}' '{0:>06}'".format(9, 8)
print(registercode)
# without index the order the value given will be placed
registercode = "WWW '{}' '{}'".format(12, 28)
print(registercode)
# other ways to inject variable, f strings from py 3.6
r_X = 12
r_Y = 76
registercode = f"WWW '{r_X}' '{r_Y}'"
print(registercode)

"""
Numeric type
"""
# The floating point accuracy issue, the result will not be zero, but approx zero
accountFaulty = .1 + .1 + .1 - .3
print(accountFaulty)

# So in the calculation of money we cannot use floating point number we use py lib, we will get accurate ZERO
accountBalance2020 = Decimal('0.10')
accountBalance2021 = Decimal('0.30')
balance = accountBalance2020 + accountBalance2020 + \
    accountBalance2020 - accountBalance2021
print(balance)

"""
 Boolean type 
"""
# Boolean value can be result of comparison operator
greater = 12 > 11
print('X is greater {}'.format(greater))

# False predicted output, empty string, O
x = ''
y = 0
if y:
    print('True')
else:
    print('False')

"""
Sequencial type
"""
# List
gateNumbers = [1, 2, 3, 4]
gateNumbers[2] = 1
# Tuple - Non mutable
securityNumbers = (1, 2, 3, 4, 5)
# securityNumbers[1] = 23 - Throws error if dare to touch the line, so non mutable
for gate in gateNumbers:
    print(gate)
# Range - Non mutable
randomTokens = range(2, 13, 2)

for token in randomTokens:
    print(f'Token {token} is generated')

# Mutable when print the range in a list
constructedTokens = list(range(5))
constructedTokens[0] = 101

for token in constructedTokens:
    print(f'Ordered token {token} is generated')

# Dictionary
liftVacancy = {'one': 10, 'two': 7, 'three': 6}

for lift, count in liftVacancy.items():
    print(f'Lift {lift} has vacancy {count}.')

"""
Search for type, id for object literal, is usage, is instance
"""
lineOne = [1, "James", 2, "Alex"]
lineTwo = [1, "Katei", 2, "Dimple"]
# Both result below will same since the value 1 object literal will have same unique id
print(id(lineOne[0]))
print(id(lineTwo[0]))

# Is check the values are of same object literal
if lineTwo[0] is lineOne[0]:
    print("Same")

# is instance for check type
if  isinstance(lineOne, tuple) :
    print("Tuple")
elif isinstance(lineOne, list):
    print("List")