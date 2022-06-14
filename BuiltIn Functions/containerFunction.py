#!/usr/bin/env python3
"""
Container functions
"""

rooms = ('R1', 'R2', 'R3', 'R4', 'R5')
# gives an iterator
roomsRev = reversed(rooms)
for room in roomsRev:
    print(room)

# gives an iterator
roomsRevTuple = tuple(reversed(rooms))

print(rooms)
print(roomsRevTuple)
# gives the sum of tuple, start value 10 is added with sum
print(sum(roomsRev, 10))
# gives min of tuple, max is used for max of tuple
print(min((1, 2, 3)))

# any will give True if any item is true
print(any(roomsRevTuple))

# all will give True if all items is true
print(any(roomsRevTuple))

# zip function gives iterator with combination
zipTuple = zip(roomsRevTuple, rooms)

for r1, r2 in zipTuple:
    print(f'{r1} - {r2}')
    
# enumerate will be giving the index and item of the iterarator
for index, item in enumerate(roomsRevTuple):
    print(f'{index} : {item}')