#!/usr/bin/env python3
"""
    We can create whatever data with comprehension
"""


def main():
    randomRollNumbers = range(9)
    oddRollNumbers = [rollNumber for rollNumber in randomRollNumbers if rollNumber % 2 != 0]
    oddEvenRollTuples = [(rollNumber, rollNumber-1) for rollNumber in randomRollNumbers if rollNumber % 2 != 0]
    rollNumberGroupingDictionary = {rollNumber + 1: rollNumber * 2 for rollNumber in randomRollNumbers }
    
    print(randomRollNumbers)
    print(oddRollNumbers)
    print(oddEvenRollTuples)
    print(rollNumberGroupingDictionary)

main()