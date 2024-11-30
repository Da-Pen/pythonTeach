import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_COLOR = (200, 150, 100)
APPLE_COLOR = (255, 0, 0)

def random_apple_x():
    return random.randrange(0, 450)

def run_program():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Apple Catcher!!!")

    clock = pygame.time.Clock()

    player_width, player_height = 100, 100
    player_x = 250 - (player_width/2)
    player_y = 500 - player_height - 20
    player_speed = 3

    apple_x, apple_y = random_apple_x(), -50
    apple_width, apple_height = 50, 50
    apple_fall_speed = 3

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        apple_y += apple_fall_speed
        if apple_y + apple_height >= player_y:
            if apple_x > player_x and apple_x + apple_width < player_x + player_width:
                apple_y = -50
                apple_x = random_apple_x()
                score += 1
                # make it harder by making the next apple fall faster.
                apple_fall_speed += 0.3
                # to make sure the player can still catch it, also increase the player speed.
                player_speed += 1
            else:
                print("Score:", score)
                pygame.quit()
                sys.exit()

        # Fill background
        screen.fill(WHITE)
        pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, APPLE_COLOR, (apple_x, apple_y, apple_width, apple_height))

        pygame.display.flip()
        clock.tick(60)

run_program()
