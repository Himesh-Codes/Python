class PersonalDetails():
    def __init__(self, **details):
        if 'name' in details: self._name = details['name'] 
    # getter
    def name(self, name = None) -> str:
        if name: self._name = name
        try: return self._name
        except AttributeError: return None
