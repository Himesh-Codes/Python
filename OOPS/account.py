#!user/bin/env python3

class Account():
    # This is a class level variable so object is same to every instance of class
    accounts: list
       
    def __init__(self, **reference):
        self.accounts = []
        # object can be created like this, and this is object level varible since py have no private declaration
        self._reference_id = reference['id'] if 'id' in reference else 1212
        
    def addAccount(self, number: str):
        self.accounts.append(number)
        
    #safe to get the values of object variable using getters
    def referenceId(self, setter = None):
        if setter: self._reference_id = setter
        return self._reference_id
        

def main():
    account = Account(id=7676)
    account.addAccount('101112322')
    print(account.accounts)
    print(account.referenceId())

if __name__ == '__main__':
    main()
    