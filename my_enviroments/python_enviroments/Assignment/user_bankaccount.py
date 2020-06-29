class BankAccount:
    def __init__(self, id, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.id = id

    def deposit(self, amount):
        if self.balance < 0:
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


class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checkings = BankAccount(1, int_rate=0.01, balance=0)
        self.savings = BankAccount(1, int_rate=0.1, balance=0)

    def make_deposit(self, amount):
        self.checkings.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.checkings.withdraw(amount)
        return self

    def update_display_user(self):
        self.checkings.display_user_balance()


user1 = User("Nathan", "nhan13574@gmail.com")

user1.make_deposit(300).make_withdraw(100)
user1.update_display_user()
