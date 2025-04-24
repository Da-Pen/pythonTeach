class Whale:
    def __init__(self, name, species, ocean):
        self.name = name
        self.species = species
        self.ocean = ocean

    # first show what it prints when we comment it out, then when we add the __str__ method
    # def __str__(self):
    #     return (f"Hi, my name is {self.name} and I am a {self.species}"
    #             f" whale that lives in the {self.ocean} ocean.")

wailord = Whale("Wailord", "blue", "Pacific")
print(wailord)