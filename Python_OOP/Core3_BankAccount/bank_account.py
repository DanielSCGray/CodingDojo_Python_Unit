# Create a BankAccount class with the attributes interest rate and balance

# Add a deposit method to the BankAccount class

# Add a withdraw method to the BankAccount class

# Add a display_account_info method to the BankAccount class

# Add a yield_interest method to the BankAccount class

# Create 2 accounts

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
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

acct1 = BankAccount()
acct2 = BankAccount()

acct1.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()

acct2.deposit(500).withdraw(150).withdraw(250).deposit(400).withdraw(600).withdraw(450).yield_interest().display_account_info()

BankAccount.display_all()