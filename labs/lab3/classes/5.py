class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
        print(f"Deposited: {money}. Balance {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print("Balance isn't enough. Withdrawal denied.")
        else:
            self.balance -= money
            print(f"Withdrew: {money}. Balance: {self.balance}")


acc1 = Account("dana", 1000)

acc1.withdraw(500)
acc1.deposit(200)