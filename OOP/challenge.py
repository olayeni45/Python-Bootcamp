class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print("Deposit accepted")

    def withdraw(self, amount):
        if(amount > self.balance):
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal accepted")

    def __str__(self) -> str:
        return f"Account owner: {self.owner} \nAccount Balance: ${self.balance}"

acct1 = Account("Jose", 100)
print(acct1)
print("")

acct1.deposit(50)
print(acct1)
print("")

acct1.withdraw(75)
print(acct1)
print("")

acct1.withdraw(500)
print(acct1)
print("")