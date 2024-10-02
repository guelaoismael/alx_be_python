class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if self.account_balance >= amount :
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        return f"Current Balance: ${self.account_balance}"