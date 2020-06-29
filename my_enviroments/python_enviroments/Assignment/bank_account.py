class BankAccount():
    def __init__(self, accountID, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.id = accountID

    def deposit(self, amount):
        if self.balance < 35:
            self.balance = self.balance + amount - 5
            return self
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < 35:
            self.balance = self.balance - amount - 5
            print(f"ID: {self.id} Insufficient funds: Charging $5 fee")
            return self
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"ID: {self.id}, Account balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

    # Transfer

    def transfer(self, from_user, to_user, amount):
        from_user.make_withdrawal(amount)
        to_user.make_deposit(amount)


account1 = BankAccount(1, 2, 300)
account1.deposit(300).deposit(200).deposit(100).withdraw(200)
account1.yield_interest()
account1.display_user_balance()


account2 = BankAccount(2, 3, 1000)
account2.yield_interest()
account2.deposit(500).deposit(500).withdraw(
    100).withdraw(100).withdraw(100).withdraw(100)
account2.display_user_balance()


account3 = BankAccount(3, 5, 0)
account3.deposit(10).withdraw(10)
account3.display_user_balance()
