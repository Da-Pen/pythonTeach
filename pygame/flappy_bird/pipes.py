import pygame
import constants
import random

class Pipes:
    def __init__(self, x, gap_size):
        self.x = x
        self.gap_start = random.randrange(0, constants.SCREEN_HEIGHT - gap_size)
        self.gap_end = self.gap_start + gap_size

    def draw(self, screen):
        # top pipe
        pygame.draw.rect(screen, constants.PIPE_COLOR, (self.x, 0, constants.PIPE_WIDTH, self.gap_start))
        # bottom pipe
        pygame.draw.rect(screen, constants.PIPE_COLOR, (self.x, self.gap_end, constants.PIPE_WIDTH, constants.SCREEN_HEIGHT))

    def move_left(self, speed):
        self.x -= speed
