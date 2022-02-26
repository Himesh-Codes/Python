#!/usr/bin/env python3
#cmd+shift+p for linting selection
"""
Conditions & Operators
"""
amountOne = 121
amountTwo = 121
amounts = [121, 22.3]
# Is operator 
if(amountOne is amountOne):
    print('Same object')

# IN / not IN - membership operator
if(amountOne not in amounts):
    print('Have same value')
    
"""
Conditional Assignments
"""
SECURITY_AREA = "inside" if(True) else "outside"
print(SECURITY_AREA)

"""
Operators
"""
freeGuards = 12
freeTraffic = 5

assign = 12 / 5
print(assign)

# Integer division without decimal point
strictassign = 12 // 5
print(strictassign)

# Boolean operators
if freeGuards > 11 and freeTraffic > 3:
    print("Enough for drill")
elif freeGuards < 13 or freeTraffic < 3:
    print("No drill")
    
