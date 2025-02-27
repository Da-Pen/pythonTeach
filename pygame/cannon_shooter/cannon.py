import pygame
import math

COLOR = (150, 150, 150)
WIDTH = 100
HEIGHT = 50
START_ANGLE = 45

class Cannon:
    def __init__(self):
        self.angle = START_ANGLE
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.surface, COLOR, (0, 0, WIDTH, HEIGHT))

    def draw(self, screen):
        rotated_surface = pygame.transform.rotate(self.surface, self.angle)

        # Draw rotated rectangle
        # Calculate position to draw on.
        # use angle to calculate distance between bottom of pipe to bottom of rotated_surface
        dist_to_surface_bottom = math.sqrt(2 * ((HEIGHT/2) ** 2)) * math.cos(math.radians(45 - self.angle))
        surface_height = rotated_surface.get_height()
        x = - (dist_to_surface_bottom - 50)
        y = screen.get_height() - surface_height + (dist_to_surface_bottom - 50)
        screen.blit(rotated_surface, (x, y))

    def rotate_clockwise(self):
        if self.angle > 0:
            self.angle -= 1

    def rotate_counter_clockwise(self):
        if self.angle < 90:
            self.angle += 1