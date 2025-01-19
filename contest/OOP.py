# Note: There is also an OOP file in the pygame folder which teaches OOP using pygame.
# The approach is similar, just more general in this one.

# First show students this Dog program and ask them to code it without OOP.
# Ask them how they approached it.
#   - They might have done it with dictionaries, parallel lists, or variables for each attribute
#   - Tell them the issues with their implementation.
#       - What if we had more dogs?
#       - What if we had more attributes / function?

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

# Show them how this Dog class would be programmed with OOP

class Dog:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print(f"{self.name} created with weight {self.weight} lbs")

    def play_catch(self):
        if self.weight > 25:
            self.weight -= 10
            print(f"{self.name} played catch. Their new weight is {self.weight} lbs")
        else:
            print(f"{self.name} is too hungry to play catch! Their weight is still {self.weight} lbs")

    def eat(self, food_weight):
        self.weight += food_weight
        print(f"{self.name} at some food. Their new weight is {self.weight} lbs")



def main():
    dogs = [Dog("Marley", 100),  Dog("Bolt", 50)]

    while True:
        print("Choose a dog:")
        for i in range(len(dogs)):
            print(f"\t({i}) {dogs[i].name}")
        dog = dogs[int(input())]
        action = int(input(f"What do you want {dog.name} to do?\n\t(0) Play catch\n\t(1) Eat\n"))
        if action == 0:
            dog.play_catch()
        elif action == 1:
            food_weight = int(input(f"How many pounds of food are they eating? "))
            dog.eat(food_weight)

main()


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
