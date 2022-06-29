#!/usr/bin/env python3
"""
Custom module
"""

class Saytime():
    
    __localiseWord = {
        'noon': 'noon',
        'midnight': 'midnight',
        'til': 'till',
        'past': 'past'
    }
    
    def __init__(self, hour = None, minute = None):
        self.__time(hour, minute)
        
    def __time(self, hour, minute):
        if hour in range(12, 15):
            print( f'The {hour}:{minute} is {self.__localiseWord["noon"]}')
        elif hour in range(0, 2):
            print( f'The {hour}:{minute} is {self.__localiseWord["midnight"]} ')
            