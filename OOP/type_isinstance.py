class Character:
    pass

class Superhero(Character):
    pass

class Villain(Character):
    pass


character = Character()

print(type(character))
print(isinstance(character, Character))
print(isinstance(character, Superhero))

superhero = Superhero()

print(type(superhero))
print(isinstance(superhero, Character))
print(isinstance(superhero, Superhero))
print(isinstance(superhero, Villain))

print(issubclass(Superhero, Character))
print(issubclass(Character, Superhero))
