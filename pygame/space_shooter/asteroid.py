import pygame
import random

class Asteroid:
    def __init__(self, x, y, speed, width, height, image):
        self._width = width
        self._height = height
        self._image = image
        self._speed = speed
        self._x = x
        self._y = y

    def draw(self, screen):
        screen.blit(self._image, (self._x, self._y))

    def update(self):
        self._y += self._speed

    def out_of_screen(self, screen_height):
        return self._y > screen_height

    def hit_by_bullet(self, bullet):
        bullet_x = bullet.get_x()
        bullet_y = bullet.get_y()

        # simplification: just check if the top left corner of the bullet is in the asteroid
        return (
                self._x < bullet_x < self._x + self._width and
                self._y < bullet_y < self._y + self._height
        )

    def get_children(self):
        return []


class NormalAsteroid(Asteroid):
    _width = 50
    _height = 50
    _image_original = pygame.image.load("images/asteroid.png")
    _image_scaled = pygame.transform.scale(_image_original, (_width, _height))

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            2,
            NormalAsteroid._width,
            NormalAsteroid._height,
            NormalAsteroid._image_scaled
        )

    @staticmethod
    def new_normal_asteroid(screen_width):
        return NormalAsteroid(
            random.uniform(0, screen_width - NormalAsteroid._width),
            -NormalAsteroid._height
        )


class BigAsteroid(Asteroid):
    _width = 100
    _height = 100
    _image_original = pygame.image.load("images/asteroid.png")
    _image_scaled = pygame.transform.scale(_image_original, (_width, _height))

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            1,
            BigAsteroid._width,
            BigAsteroid._height,
            BigAsteroid._image_scaled
        )

    @staticmethod
    def new_big_asteroid(screen_width):
        return BigAsteroid(
            random.uniform(0, screen_width - BigAsteroid._width),
            -BigAsteroid._height
        )

    def get_children(self):
        return [
            NormalAsteroid(self._x - 30, self._y),
            NormalAsteroid(self._x + 30, self._y)
        ]
