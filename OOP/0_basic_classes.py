# Introduce idea of objects in the real world
#   There are "things" in the real world with:
#       - Properties (characteristics / attributes)
#       - Methods (things they can do, actions)
#   Examples: Student, Dog, Hamster, Shirt, Soccer Player, Cereal, Movie
# Classes are blueprints, objects are instances
#   Examples: Student -> Adrien, Dog -> Bolt, Movie -> Frozen II
# Exercises:
#   - For each class, name some objects, properties, and methods.
#       - Song, Book, Drink, Restaurant, Actor, Language, Sport

class Dog:
    # init method
    def __init__(self, name):
        # attribute
        self.name = name

# how to create an object
fido = Dog("Fido")
# how to access an attribute
print(fido.name)

bolt = Dog("Bolt")
print(bolt.name)


class Plant:
    def __init__(self, height):
        # attribute
        self.height = height

    # method
    def grow(self):
        self.height += 1


my_plant = Plant(3)
print(my_plant.height)

# how to call a method
my_plant.grow()

print(my_plant.height)


# Exercises
#   - Create a class called Person that has a name and age
#       - They can say_hello(), ex. "Hi, my name is Adrien, and I am 10 years old"
#       - They can get_older() - their age increases by 1
#   - Add the bark() function to this Dog class. If their weight is <= 100, print "woof!".
#       If their weight is > 100, print "WOOF!".
#   - Create a class called Thief that has an amount of money.
#       - They can rob(other_thief), which will give them all the money the other thief has
#       - They can work(hours), which will give them $20/h
#   - Create a class called Boxer that has a name, # wins, # losses, power, and speed.
#       - They can train(hours) - Their power and speed each go up by a random number between 1 and hours.
#       - They can fight(other_boxer) - The boxer with a bigger combined speed and power wins. If they are the same, a random boxer wins.
#   - Create a class called BankAccount that has a name, accountNumber and balance
#       - They can deposit(amount) and withdraw(amount)
#       - They can ask for a transactionHistory() - return all past deposits and withdrawals as a list of tuples (transaction_type, amount)
