import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw(screen):
    # Fill background
    screen.fill(WHITE)

    # Draw a face
    pygame.draw.circle(screen, BLACK, (200, 200), 10)
    pygame.draw.circle(screen, BLACK, (300, 200), 10)

    pygame.draw.rect(screen, BLACK, (200, 300, 100, 20))


def run_program():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("My Game")

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
