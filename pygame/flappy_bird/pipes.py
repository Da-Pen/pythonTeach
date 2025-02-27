import pygame
import constants
import random

COLOR = (0, 200, 0)
WIDTH = 50
DISTANCE_BETWEEN_PIPES = 300  # distance between a pair of pipes and the next pair of pipes
START_GAP_SIZE = 300  # gap between top and bottom pipes when the game starts
GAP_SIZE_DECREASE = 5  # how much to decrease the distance between top and bottom pipes for each new pipe pair
MIN_GAP_SIZE = 100  # min gap between top and bottom pipes

class PipePair:
    def __init__(self, x, gap_size):
        self.x = x
        self.gap_start = random.randrange(0, constants.SCREEN_HEIGHT - gap_size)
        self.gap_end = self.gap_start + gap_size

    def draw(self, screen):
        # top pipe
        pygame.draw.rect(screen, COLOR, (self.x, 0, WIDTH, self.gap_start))
        # bottom pipe
        pygame.draw.rect(screen, COLOR, (self.x, self.gap_end, WIDTH, constants.SCREEN_HEIGHT))

    def move_left(self, speed):
        self.x -= speed
