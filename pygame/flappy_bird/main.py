import pygame
import sys

import constants
from bird import Bird
from pipes import Pipes

def run_program():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird!!!")

    clock = pygame.time.Clock()

    bird = Bird()

    # gap between top and bottom pipe. Gets smaller over time.
    current_pipe_gap_size = constants.START_PIPE_GAP_SIZE
    pipes = [Pipes(constants.SCREEN_WIDTH, current_pipe_gap_size)]

    current_game_x_speed = constants.START_GAME_X_SPEED

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Detect key press
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # check if we need to generate new pipes
        if constants.SCREEN_WIDTH - pipes[-1].x >= constants.DISTANCE_BETWEEN_PIPES:
            if current_pipe_gap_size > constants.MIN_PIPE_GAP_SIZE:
                current_pipe_gap_size -= constants.PIPE_GAP_SIZE_DECREASE
            pipes.append(Pipes(constants.SCREEN_WIDTH, current_pipe_gap_size))

        # update bird position
        bird.fall()

        # update pipes positions
        for pipe in pipes:
            pipe.move_left(current_game_x_speed)

        # increase game speed
        current_game_x_speed += constants.GAME_X_SPEED_INCREASE_PER_FRAME

        # DRAWING
        # Fill background
        screen.fill(constants.WHITE)
        # draw bird
        bird.draw(screen)
        # draw pipes
        for pipe in pipes:
            pipe.draw(screen)

        pygame.display.flip()
        clock.tick(60)

run_program()

