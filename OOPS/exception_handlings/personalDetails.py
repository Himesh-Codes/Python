from datetime import date
import sys

class PersonalDetails():
    def __init__(self, **details):
        if 'name' in details: self._name = details['name'] 
        
    # getter
    def name(self, name = None) -> str:
        if name: self._name = name
        try: return self._name
        except AttributeError: return None
        
    #generic exception handling using sys
    def dateOfBirth(self, setter = None) -> date:
        if setter: self._dob = setter
        try: return self._dob
        except: return f'Error: {sys.exc_info()[1]}'
        