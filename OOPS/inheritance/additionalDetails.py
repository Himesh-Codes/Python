import sys
sys.path.insert(0, 'Python/OOPS/exception handlings')
from personalDetails import PersonalDetails
class PersonalAdditionalDetails(PersonalDetails):
    def __init__(self, *args):
        super(PersonalAdditionalDetails).__init__(*args)
        