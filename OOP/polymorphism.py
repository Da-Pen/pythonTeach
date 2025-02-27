# TODO: improve this or delete. Polymorphism isn't that well demonstrated using Python.

# Idea: you can create an object and use it while not actually knowing which type it is

class Car:
    def __init__(self):
        self.x = 0
        self.gas = 0

    def fill_gas(self):
        self.gas = 100

    def drive(self):
        if self.gas < 10:
            print("Not enough gas!")
            return
        self.x += 10
        self.gas -= 10


class BigTruck(Car):
    def fill_gas(self):
        self.gas = 200


class Racecar(Car):
    def drive(self):
        super().drive()
        self.x += 10


def main():
    cars = [Car(), BigTruck(), Racecar()]
    for car in cars:
        # Here we "don't know" which class we are working with,
        # But it doesn't matter because all cars have the
        # fill_gas() and drive() methods
        car.fill_gas()
        car.drive()
        print(type(car), car.x, car.gas)

main()