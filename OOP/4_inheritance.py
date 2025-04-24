import random

# Superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Unknown animal noises"

# Subclass
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Subclass
class Dog(Animal):
    def speak(self):
        return "Woof!"


a = Animal("Mystery Beast")
d = Dog("Fido")
c = Cat("Whiskers")

print(a.name, "says:", a.speak())
print(d.name, "says:", d.speak())
print(c.name, "says:", c.speak())

# Exercise:
#   Create a Vehicle class, along with two subclasses: Car and Boat
#   Vehicle has:
#    - An __init__ method that takes a name parameter and stores it.
#    - A move() method that returns the string "Unknown vehicle movement".
#   Car class:
#    - Overrides the move() method to return "Drives on roads".
#   Boat class:
#    - Overrides the move() method to return "Sails on water".
#   Create instances of Car and Boat, call their move() methods, and print
#   the results to confirm the correct behavior.

# Exercise: Create a SoccerPlayer class with subclasses Defender and Striker.
# SoccerPlayer has a name and two methods:
# - pass_ball() prints "Ronaldo passed the ball." (replace Ronaldo with their name)
# - shoot_ball() makes the player attempt a shot. There is a 20% chance of scoring.
#   - If they score, print "Ronaldo scored!"
#   - If they miss, print "Ronaldo missed :("
# Defender and Striker are the same as SoccerPlayer, except:
# - Defenders have a 10% chance of scoring when they shoot_ball()
# - Strikers have a 40% chance of scoring when they shoot_ball()
#
# Hint: random.random() generates a random number between 0 and 1. So for example,
#   if you want something to have a 60% chance of success, you can do
#   success = random.random() > 0.4


class SoccerPlayer:
    def __init__(self, name):
        self.name = name

    def pass_ball(self):
        print(f"{self.name} passed the ball.")

    def shoot_ball(self):
        success = random.random() > 0.8  # random.random() generates a number between 0 and 1
        if success:
            print(f"{self.name} scored!")
        else:
            print(f"{self.name} missed :(")

class Defender(SoccerPlayer):
    def shoot_ball(self):
        success = random.random() > 0.9  # random.random() generates a number between 0 and 1
        if success:
            print(f"{self.name} scored!")
        else:
            print(f"{self.name} missed :(")

class Striker(SoccerPlayer):
    def shoot_ball(self):
        success = random.random() > 0.6  # random.random() generates a number between 0 and 1
        if success:
            print(f"{self.name} scored!")
        else:
            print(f"{self.name} missed :(")

soccer_player = SoccerPlayer("Tracy")
striker = SoccerPlayer("Madeline")
defender = SoccerPlayer("Jacques")

soccer_player.pass_ball()
defender.pass_ball()

soccer_player.shoot_ball()
striker.shoot_ball()
defender.shoot_ball()









# can access attributes from superclass directly with self._
# can access methods from superclass directly with self._()

# can "override" attributes and methods from superclass
# with both of these, if you create an instance of the subclass,
# you will get the subclass one when trying to use the attribute/method

# can explicitly call superclass methods with super()
# ex. super().__init__(), super().other_method()

class Wizard:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def cast_spell(self, spell_name):
        return f"{self.name} casts {spell_name} with power {self.power_level}!"

    def learn_spell(self):
        self.power_level += 1


class StudentWizard(Wizard):
    def __init__(self, name, year, power_level):
        super().__init__(name, power_level)  # calls the __init__() method of the superclass
        self.year = year

    def intro(self):
        # can access superclass attribute with self
        return f"I am {self.name}, a year {self.year} student at Wizard High with power level {self.power_level}"

    def cast_spell(self, spell_name):
        result = random.choice(["success", "fail"])
        if result == "fail":
            return f"{self.name} failed to cast spell {spell_name}!"
        # accessing superclass method
        return super().cast_spell(spell_name)

    def go_to_class(self):
        # learns 10 spells
        for i in range(10):
            self.learn_spell()

# Example usage
harry = StudentWizard("Harold the Bewildered", 3, 6)
print(harry.intro())
print(harry.cast_spell("Kawanabasha"))
harry.go_to_class()
print(harry.cast_spell("Ouagadougou"))

# Exercise:
# Create a Book class that has the following:
#  - An __init__() method that takes a title and stores it as an instance attribute.
#  - A method called summary() that returns a string like: "This is a book titled 'X'."
# Then, create a subclass called Ebook that:
#  - Inherits from Book.
#  - Adds an attribute file_size in megabytes, which is passed into its __init__() method.
#  - Has a method called describe() that returns a string like: "The ebook 'X' is Y MB large."
#  - Has a method called preview() that calls the summary() method from the superclass.
