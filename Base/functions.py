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


# return value is not mandatory for function else None is returned
returnvalue = printStar(3)
print(returnvalue)


def printMyName(name, subname=''):
    print(f'{name}',  ',{subname}' if(subname) else '')

#args
def printMyNames(*names):
    if len(names):
        for name in names:
            print(name, flush=True)

# kwargs
def printMyNamesDetails(**names):
    if len(names):
        for key in names:
            print(names[key], flush=True)

printMyName('Himesh')
printMyNames('Alex', 'Riya')
printMyNamesDetails(sales = 'Neethu', accounts = 'Jio')
subBranch = {'manager': 'Nikhil', 'sales': 'Hanna'}
# dictionary can be passed only by this way
printMyNamesDetails(**subBranch)

#function inside function - after 1st scripts executed 2nd will start
def printPersonalDetails():
    print('Arun')
    def printAddress():
        print('Mangalassery')
    print('Neelakandan')
    printAddress()

printPersonalDetails()