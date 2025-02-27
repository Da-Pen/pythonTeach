
class Pet:
    def __init__(self, species, name, age, weight):
        self.species = species
        self.name = name
        self.age = age
        self.weight = weight

    def get_info(self):
        return f"My name is {self.name}, I am a {self.age} year-old {self.species}. I weigh {self.weight} lbs."

    def eat(self):
        print(f"{self.name} is eating!")
        self.weight += 1

class Dog(Pet):
    def __init__(self, name, age, weight):
        super().__init__("dog", name, age, weight)

    def play_catch(self):
        print(f"{self.name} is playing catch!")
        self.weight -= 2


my_dog = Dog("Zoey", 2, 80)
print(my_dog.get_info())
my_dog.play_catch()
print(my_dog.get_info())
my_dog.eat()
print(my_dog.get_info())

