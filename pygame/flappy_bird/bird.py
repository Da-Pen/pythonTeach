import pygame
import constants

START_X = 100
START_Y = 200
WIDTH = 50
HEIGHT = 50
FALL_ACCELERATION = 0.5
JUMP_FORCE = 10
COLOR = (250, 200, 0)

class Bird:
    def __init__(self):
        self.x = START_X
        self.y = START_Y
        self.width = WIDTH
        self.height = HEIGHT
        self.speed_y = 0

    def fall(self):
        self.speed_y += FALL_ACCELERATION
        self.y += self.speed_y

    def jump(self):
        self.speed_y = -JUMP_FORCE

    def draw(self, screen):
        pygame.draw.rect(screen, COLOR, (self.x, self.y, self.width, self.height))
