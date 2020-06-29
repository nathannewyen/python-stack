

class User():
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance
        # self.id = customerID

# Widthdrawal

    def make_withdrawal(self, amount):
        self.account_balance -= amount

# Make Deposit

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

# Transfer

    def transfer(self, from_user, to_user, amount):
        from_user.make_withdrawal(amount)
        to_user.make_deposit(amount)

        # Display User Balance

    def display_user_balance(self):
        print(f"""
Name: {self.name}
Account balance: ${self.account_balance}
        """)


user1 = User("Guido", 500)
user2 = User("Nick", 300)
user3 = User("Nathan", 1000)

# User1
user1.make_deposit(150).make_deposit(150).make_deposit(
    150).make_deposit(150).make_withdrawal(300)

user1.transfer(user1, user3, 500)
user1.display_user_balance()


# User2
user2.make_deposit(300)
user2.make_withdrawal(100)
user2.display_user_balance()


# User3
user3.make_deposit(3000)
user3.make_withdrawal(500)
user3.display_user_balance()


# ##########
