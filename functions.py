#!/usr/bin/env python3
"""
    Training for the PYTHON functions, conditions, loops, objects
"""
imInevitable = True
if imInevitable:
    print("I m inevitable")
elif imInevitable == False:
    print("No i am not.. but may..")
else:
    print("No result")


def printStar(line_number):
    while line_number != 0:
        current_index = line_number

        while current_index != 0:

            print("*", end=" ", flush=True)
            current_index -= 1
        # print a new line after each iteration
        print()
        line_number -= 1


returnvalue = printStar(3)
print(returnvalue)
