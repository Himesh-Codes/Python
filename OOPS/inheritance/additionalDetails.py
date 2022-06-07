# while importing from different directory module error happen as py will look only on current directory
# first way is STATIC path below
import sys
# sys.path.insert(0, '/Users/himeshs/Codes/Python/Python/OOPS/exception_handlings')

# second way is let py select the directory
import os
PERSONAL_DETAILS_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'exception_handlings'))
sys.path.insert(0, PERSONAL_DETAILS_DIR)
from personalDetails import PersonalDetails

class PersonalAdditionalDetails(PersonalDetails):
    cuurentname = 'none'
    def __init__(self, **details):
        super().__init__(**details)
        self._address = details['address'] if 'address' in details else None
            
    #overrided the function of parent
    def name(self) -> str:
        cuurentname = super().name()
        if cuurentname:
            cuurentname = cuurentname[::-1]  
        return cuurentname
    
    def address(self, setter = None) -> str:
        if setter: self._address = setter
        return self._address


person = PersonalAdditionalDetails(name='Himesh', address = 'ABC Village, 770')
person2 = PersonalAdditionalDetails()
print(person.name())
print(person2.name())
print(person.cuurentname)
print(person.address())
print(person.dateOfBirth())
