#!/usr/bin/env python3
"""
Built-in functions
"""

class Function():
    
    def numericFunction(self):
        x = '12'
        y = int(x)
        z = float(x)
        #print absolute value
        a = abs(y)
        #divmod return quotient & reminder as a tuple
        b = divmod(y, 5)
        #complex number
        c = complex(y, 5)
        
        print(f'x: {type (x)}')
        print(f'x: {x}')
        print(f'y: {type(x)}')
        print(f'y: {y}')
        print(f'z: {type(z)}')
        print(f'z: {z}')
        print(f'a: {type(a)}')
        print(f'a: {a}')
        print(f'b: {type(b)}')
        print(f'b: {b}')
        print(f'c: {type(c)}')
        print(f'c: {c}')
        
fun = Function()
fun.numericFunction()
        
        