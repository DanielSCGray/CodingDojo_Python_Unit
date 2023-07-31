class BankAccount:
    all_accounts =[]

    def __init__(self, balance=0, int_rate=.01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            return self
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        print(f"Account interest rate: {self.int_rate}%")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self
    @classmethod
    def display_all(cls):
        for acct in cls.all_accounts:
            acct.display_account_info()
'''
Create a User class with an __init__ method

Add a make_deposit method to the User class that calls on it's bank account's instance methods.

Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.

Add a display_user_balance method to the User class that displays user's account balance

SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
'''

class User:
    def __init__(self, name, email, account_name):
        self.name = name
        self.email = email
        self.account = {account_name : BankAccount()}

    def make_deposit(self, account_name, amount):
        self.account[account_name].deposit(amount)
        return self

    def make_withdrawl(self, account_name, amount):
        self.account[account_name].withdraw(amount)
        return self
    
    def add_account(self, new_account_name):
        if new_account_name in self.account.keys():
            print(f'ERROR: Account {new_account_name} already exists')
            return self
        self.account[new_account_name] = BankAccount()
        return self
    
    def transfer_money(self, acct_name, amount, other_user, other_user_acct_name):
        self.account[acct_name].withdraw(amount)
        other_user.account[other_user_acct_name].deposit(amount)
        return self




test = User('test', 'gmail', 'did_it_work')
test.account['did_it_work'].display_account_info()
# It Did!
test.add_account('second_acct').account['second_acct'].display_account_info().deposit(100).display_account_info()

user2 = User('Joe', 'email', 'main')

test.transfer_money('second_acct', 50, user2, 'main').account['second_acct'].display_account_info()

user2.account['main'].display_account_info()

test.add_account('did_it_work')