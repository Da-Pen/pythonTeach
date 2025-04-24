class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Bolt")
dog2 = Dog("Bolt")

# prints memory addresses of dogs - notice that they're different
print("dog1:", dog1)
print("dog2:", dog2)

print(dog1 == dog2)  # not equal!

dog3 = dog1
print("dog3:", dog3)
print(dog1 == dog3)  # equal!

dog3.name = "Fido"
print(dog1.name)
print(dog2.name)
print(dog3.name)
