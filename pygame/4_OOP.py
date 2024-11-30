# TODO
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def run_program():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Moving Square!!!")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill background
        screen.fill(WHITE)

        pygame.display.flip()
        clock.tick(60)

run_program()
