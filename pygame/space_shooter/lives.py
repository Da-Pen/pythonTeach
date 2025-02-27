import pygame

class Lives:
    def __init__(self, num_lives):
        self._num_lives = num_lives

        self._width, self._height = 50, 50

        self._image_original = pygame.image.load("images/heart.png")
        self._image_scaled = pygame.transform.scale(
            self._image_original,(self._width, self._height)
        )

    # returns True if no lives left :(
    def lose_life(self):
        self._num_lives -= 1
        if self._num_lives == 0:
            return True
        return False

    def draw(self, screen):
        for i in range(self._num_lives):
            screen.blit(self._image_scaled, (20 + i * (self._width + 20), 10))


