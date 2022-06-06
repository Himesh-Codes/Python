#!/usr/bin/env python3
animals = ['cat', 'dog']
while (len(animals)) != 0:
    print(animals[(len(animals)) - 1])
    animals.pop()
else:
    print('End of the stock')
    
for animal in animals:
    print(animal)
else:
    print('Results end here')