import pygame
import constants

class Bird:
    def __init__(self):
        self.x = constants.BIRD_START_X
        self.y = constants.BIRD_START_Y
        self.width = constants.BIRD_WIDTH
        self.height = constants.BIRD_HEIGHT
        self.speed_y = 0

    def fall(self):
        self.speed_y += constants.BIRD_FALL_ACCELERATION
        self.y += self.speed_y

    def jump(self):
        self.speed_y = -constants.BIRD_JUMP_FORCE

    def draw(self, screen):
        pygame.draw.rect(screen, constants.BIRD_COLOR, (self.x, self.y, self.width, self.height))
