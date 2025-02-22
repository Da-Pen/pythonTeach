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

    x, y = 0, 0
    speed = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed

        # Fill background
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (x, y, 100, 100))

        pygame.display.flip()
        clock.tick(60)

run_program()

# Exercises:
#   (a) When it is partially outside the screen, it is blue
#   (b) Disallow it from going outside the screen
#   (c) Create a circle that starts at the center of the screen. Also:
#       - It moves with arrow keys.
#       - When "b" is clicked, it gets bigger.
#       - When "s" is clicked, it gets smaller, (smallest radius: 1. If s is clicked when
#         the radius is already 1, it doesn't get any smaller).
#       - When space is clicked, it resets to the original size.
#       - Challenge: It can't go outside the screen. The size increase is also limited,
#         ex. if you click "b" and the size increase would cause it to go out of the screen,
#         then disallow it from getting bigger.

