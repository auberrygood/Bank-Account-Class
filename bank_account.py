# FIXME: Add Bank Account class definition here

class BankAccount:
    
    def __init__(self, opening_balance=0):
        self.balance = opening_balance
    
    def balance(self):
        print (self.balance)
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print (self.balance)
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print(f"Invalid transaction: not enough funds to withdraw ${withdraw_amount}.")
            #solution: raise ValueError(f"Invalid transaction: not enough funds to withdraw ${withdraw_amount}")
        else:
            self.balance = self.balance - withdraw_amount
            print(self.balance)
    #pass


# You can see how this class should be used below. Make sure you
# run your code and test it out to make sure it works.

# account_1 = BankAccount()
# account_2 = BankAccount()
# account_3 = BankAccount(100)
# account_3.balance
#   >>> 100
# account_1.deposit(100)
# account_1.balance
#   >>> 100
# account_2.deposit(50)
# account_2.balance
#   >>> 50
# account_3.deposit(75)
# account_3.balance
#   >>> 175
# account_2.withdraw(10)
# account_2.balance
#   >>> 40
# account_1.withdraw(10)
# account_1.balance
#   >>> 90
# account_2.withdraw(50)
#   >>> "Invalid transaction: not enough funds to withdraw $50." 
# account_2.balance
#   >>> 40    # still 40 since the previous transaction was not successful
