import pygame
import sys

from cannon import Cannon

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def run_program():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Cannon")

    clock = pygame.time.Clock()

    cannon = Cannon()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            cannon.rotate_counter_clockwise()
        if keys[pygame.K_DOWN]:
            cannon.rotate_clockwise()

        cannon.draw(screen)

        pygame.display.flip()
        clock.tick(60)

run_program()
