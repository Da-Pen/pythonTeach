# Imagine you are a very small bank.
# A bank that's so small that it only has one client.

# The client has a name, userID, and balance.
clientName = "Elizabeth Grant"
clientUserID = 340582
clientBalance = 1000

# What if she wants to withdraw money?
clientBalance -= 10
print(f"{clientName} withdrew $10. Their new balance is {clientBalance}")

# # What if she wants to deposit money?
# clientBalance += 25
# print(f"{clientName} deposited $25. Their new balance is {clientBalance}")
#
# # Now let's say our bank grows and we have two customers. How do we add another customer?
# client2Name = "Victoria LeGrand"
# client2UserID = 256230
# client2Balance = 5000
#
# # We can continue doing transactions with the two
# client2Balance -= 100
# print(f"{client2Name} withdrew $100. Their new balance is {client2Balance}")
#
# clientBalance += 20
# print(f"{clientName} deposited $20. Their new balance is {clientBalance}")
#
# # Simple enough. But what if we keep getting more clients? Maybe we could use a dictionary:
# clients = {
#     340582: {
#         "name": "Elizabeth Grant",
#         "balance": 1035,
#     },
#     256230: {
#         "name": "Victoria LeGrand",
#         "balance": 4900,
#     }
# }
#
#
# # and define a function for withdrawing and depositing:
# def deposit(client, amount):
#     client["balance"] += amount
#     print(f"{client["name"]} deposited ${amount}. Their new balance is {client["balance"]}.")
#
# def withdraw(client, amount):
#     if client["balance"] < amount:
#         print("could not withdraw")
#         return
#     client["balance"] -= amount
#     print(f"{client["name"]} withdrew ${amount}. Their new balance is {client["balance"]}.")

# now we can use those functions:
# deposit(clients[340582], 5)
# withdraw(clients[256230], 500)

# Much better. We can accept new clients much more easily:
# clients[112454] = {
#     # "name": "María Zardoya",
#     "first_name": "Maria",
#     "last_name": "Zardoya",
#     "balance": 3000
# }
# withdraw(clients[112454], 1000)

# But there are still problems with this approach.

# Problem: what if we accidentally add a new client with a typo?
# clients[555343] = {
#     "name": "Ella O'Connor",
#     "Balance": 50  # there is absolutely nothing telling us that this could be wrong
# }
#
# deposit(clients[555343], 1000)

# Problem: There is nothing about the deposit and withdraw functions that stops you
#   from calling them with another variable type as the client
# my_dog = {
#     "name": "Bolt",
#     "breed": "White Shepherd",
#     "age": 3
# }
# deposit(my_dog, 100)

# Problem: changing the structure of the user is complicated. For example, what if we wanted to
#   split up the first and last name?

# Solution: Objects!
# Introduce idea of objects in the real world
#   There are "things" in the real world with:
#       - Properties (characteristics / attributes)
#       - Methods (things they can do, actions -- essentially functions)
#   Examples: Student, Dog, Hamster, Shirt, SoccerPlayer, Cereal, Movie
# Classes are blueprints, objects are instances
#   Examples: Student -> Adrien, Dog -> Bolt, Movie -> Frozen II
# Exercises:
#   - For each class, name some objects, properties, and methods.
#       - Song, Book, Drink, Restaurant, Actor, Language, Sport




# BankAccount as an object:
class BankAccount:
    def __init__(self, userID, name, balance):
        print(f"Creating BankAccount for {name}...")
        self.userID = userID
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount}. Their new balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough balance, could not withdraw")
            return
        self.balance -= amount
        print(f"{self.name} withdrew {amount}. Their new balance is {self.balance}")

# How to use this class:
# elizabethsBankAccount = BankAccount(340582, "Elizabeth Grant", 1000)
# elizabethsBankAccount.withdraw(100)
# elizabethsBankAccount.deposit(500)

# my_dog = {
#     "name": "Bolt",
#     "breed": "White Shepherd",
#     "age": 3
# }
# my_dog.withdraw(100)  # Editor gives us a warning

# Do exercises in OOP.py
