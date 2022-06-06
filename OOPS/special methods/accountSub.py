#!user/bin/env python3

class AccountSub():
    accounts: list
       
    def __init__(self, **reference):
        self.accounts = []
        # object can be created like this
        self._reference_id = reference['id'] if 'id' in reference else 1212
        
    def addAccount(self, number: str):
        self.accounts.append(number)
        
    # special method - on print of the instance
    def __str__(self) -> str:
        return f'The first found account is {self.accounts[0]}'

def main():
    account = AccountSub(id=7676)
    account.addAccount('101112322')
    print(account.accounts)
    # print the object to get custom value
    print(account)

if __name__ == '__main__':
    main()
    