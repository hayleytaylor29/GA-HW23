class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi! My name is {self.name}")

me = User('Hayley')
me.greet()

class BankAccount():
    def __init__(self, account_type, starting_balance):
        self.type = account_type
        self.balance = starting_balance
        self.interest_rate = .02
        self.overdraft_fees = 0
        self.net_balance = 0
    def deposit(self, amount):
        if amount < 0:
            return False
        else:
            self.balance += amount
            return self.balance
    def withdraw(self, amount):
        if amount < 0:
            return False
        elif self.balance < 0:
            self.overdraft_fees += 20
        elif amount > self.balance:
            print("You have insufficient funds")
        else:
            self.balance -= amount - self.overdraft_fees if self.balance >= -100 else 0
    def accumulated_interest(self, interest_rate):
        self.balance += (self.balance * self.interest_rate)
        return self.balance

basic_account = BankAccount("basic_account", 1000)
basic_account.deposit(600)
print(f'Basic Account: ${basic_account.balance}')
basic_account.withdraw(30)
print(f'Basic Account: ${basic_account.balance}')
basic_account.accumulated_interest(0.02)
#was not able to just call the interest rate from the self.interest_rate
print(f'Basic Account: ${basic_account.balance}')
    


class ChildrensAccount(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)
        self.type = account_type
        self.balance = starting_balance
        self.interest_rate = 0
    def accumulated_interest(self, interest_rate):
        self.balance += 10

child_account = ChildrensAccount("child_account", 100)
child_account.deposit(20)
print(f'Childrens Account: ${child_account.balance}')
child_account.withdraw(5)
print(f'Childrens Account: ${child_account.balance}')
child_account.accumulated_interest(0)
print(f'Childrens Account: ${child_account.balance}')




class OverdraftAccount(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)
        self.overdraft_penalty = 40
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= self.overdraft_penalty
            print(f'You have insufficient funds, you will only be charged your overdraft fee of ${self.overdraft_penalty}')
            return False
    def accumulated_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        if self.balance < 0:
            self.interest_rate = 0

over = OverdraftAccount("checking", 50)
over.withdraw(20)
print(f'Checking Account: ${over.balance}')
over.accumulated_interest()
print(f'Checking Account: ${over.balance}')

'''still having a hard time understanding how to use the dunder methods, hoping
we can go over this more in class'''
'''class Dunder(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)

    def __format__(self, starting_balance, other_accounts):
        return Dunder(self.type, starting_balance)
    
    def __add__(self, other_accounts):
        combined_balance = self.balance + other_accounts.balance
        return Dunder(self.type, combined_balance)
    
    def __sub__(self, other_accounts):
        combined_balance = self.balance - other_accounts.balance
        return Dunder(self.type, combined_balance)
    
    

    

#print(str(basic_account.balance))
#print(basic_account.balance)
#accounts = Dunder()
account1 = Dunder('basic_account', 400)
account2 = Dunder('child_account', 100)
account3 = Dunder('checking', 3000)
print(format(account1 + account2 + account3))
print(format(account1 - account2 - account3))'''