class Dog:
    species = "Canis lupus familiaris"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute

rex = Dog("Rex")
print(f"{rex.name} is a {rex.species}")

frida = Dog("Frida")
print(f"{frida.name} is a {frida.species}")


# Class attributes can be non-constants:
class House:
    num_houses = 0

    def __init__(self):
        House.num_houses += 1

house1 = House()
print(f"There are now {House.num_houses} house(s)")
house2 = House()
print(f"There are now {House.num_houses} house(s)")
house3 = House()
print(f"There are now {House.num_houses} house(s)")
