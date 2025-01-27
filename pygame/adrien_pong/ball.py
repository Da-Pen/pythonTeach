import pygame
import random
import colors

class Ball:
    def __init__(self):
        self.x = 500
        self.y = 250
        self.speed_x = 3
        self.speed_y = 3
        self.randomly_generate_direction()
        self.is_sad = False

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def randomly_generate_direction(self):
        self.speed_y = random.randint(1, 5)
        self.speed_x = random.randint(1, 5)

    def draw(self, screen):
        pygame.draw.circle(screen, colors.YELLOW, (self.x, self.y), 25)
        pygame.draw.circle(screen, colors.BLACK, (self.x - 12, self.y - 12), 3)
        pygame.draw.circle(screen, colors.BLACK, (self.x + 12, self.y - 12), 3)
        pygame.draw.line(screen, colors.BLACK, (self.x - 12, self.y), (self.x - 6, self.y + 10), 3)
        pygame.draw.line(screen, colors.BLACK, (self.x + 6, self.y + 10), (self.x + 12, self.y), 3)
        pygame.draw.line(screen, colors.BLACK, (self.x - 6, self.y + 10), (self.x + 6, self.y + 10), 3)

        if self.is_sad == True:
            pygame.draw.circle(screen, colors.YELLOW, (self.x, self.y), 25)
            pygame.draw.circle(screen, colors.BLACK, (self.x - 12, self.y - 12), 3)
            pygame.draw.circle(screen, colors.BLACK, (self.x + 12, self.y - 12), 3)
            pygame.draw.line(screen, colors.BLACK, (self.x - 12, self.y + 6), (self.x - 6, self.y - 10), 3)
            pygame.draw.line(screen, colors.BLACK, (self.x - 6, self.y - 10), (self.x + 6, self.y - 10), 3)
            pygame.draw.line(screen, colors.BLACK, (self.x + 6, self.y - 10), (self.x + 6, self.y + 6), 3)
    def change_into_sad_face(self):
        self.is_sad = True
