import pygame
import colors

LENGTH = 20
COLOR = colors.GREEN

class Bullet:
    def __init__(self, x, y, speed=10):
        self._x = x
        self._y = y  # y position of top of bullet
        self._speed = speed

    def update(self):
        self._y -= self._speed

    def draw(self, screen):
        pygame.draw.line(screen, COLOR, (self._x, self._y), (self._x, self._y + LENGTH), 5)

    def out_of_screen(self):
        return self._y < -LENGTH

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y