# INTRODUCTION TO OOP:
# First: make students create this program (driving car) without OOP
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
#
# Next, show code below to show how to use OOP to create the driving car

import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Car:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

    def drive(self):
        self.x += self.speed

    def draw(self, screen):
        # top part of car
        pygame.draw.rect(screen, self.color, (self.x + 25, self.y, 50, 25))
        # bottom of car
        pygame.draw.rect(screen, self.color, (self.x, self.y + 25, 100, 25))
        # back wheel
        pygame.draw.circle(screen, BLACK, (self.x + 20, self.y + 50), 10)
        # back wheel
        pygame.draw.circle(screen, BLACK, (self.x + 80, self.y + 50), 10)


def run_program():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Car")

    clock = pygame.time.Clock()

    # top left corner of car
    red_car = Car(0, 400, RED, 8)
    blue_car = Car(0, 300, BLUE, 7)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            red_car.drive()
        if keys[pygame.K_SPACE]:
            blue_car.drive()

        # Fill background
        screen.fill(WHITE)

        # draw the car
        red_car.draw(screen)
        blue_car.draw(screen)

        pygame.display.flip()
        clock.tick(60)

run_program()

# Exercises in other OOP file
