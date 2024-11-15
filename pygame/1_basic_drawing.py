import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw(screen):
    # Fill background
    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, (250, 250), 50)
    pygame.draw.rect(screen, BLACK, (0, 200, 150, 100))
    pygame.draw.line(screen, BLACK, (0, 0), (250, 250))
    pygame.draw.polygon(screen, GREEN, ((500, 0), (250, 250), (500, 500), (375, 250)))


def run_program():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Drawings!!!")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw(screen)

        pygame.display.flip()
        clock.tick(60)

run_program()
