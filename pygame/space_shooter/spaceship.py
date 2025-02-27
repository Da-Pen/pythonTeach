import pygame
from bullet import Bullet

class Spaceship:
    def __init__(self, screen_width, screen_height):
        self._width = 80
        self._height = 80

        # load image
        self._image = pygame.image.load("images/spaceship.png")
        # resize
        self._image = pygame.transform.scale(self._image, (self._width, self._height))

        self._x = (screen_width / 2)  # represents middle of spaceship
        self._y = screen_height - self._height - 10

    def shoot_bullet(self):
        return Bullet(self._x, self._y)

    def set_x(self, x):
        self._x = x

    def draw(self, screen):
        screen.blit(self._image, (self._x - (self._width / 2), self._y))
