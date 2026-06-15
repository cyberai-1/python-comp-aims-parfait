class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Invalid deposit amount.")
            return
        self.balance -= amount  # error 1

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount  # error 2

    def get_balance(self):
        return f"{self.owner} — Balance: {self.balance}"

account = BankAccount("Fatou Diallo", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(5000)
account.deposit(-100)
print(account.get_balance())  # error 3
print(account.get_balance())  # error 4

