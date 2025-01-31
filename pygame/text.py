import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def draw_text(screen, font):
    # Fill background
    screen.fill(WHITE)
    # create text surface
    text_surface = font.render('ummmm!!!', False, BLUE)
    # draw in top center of screen
    screen.blit(text_surface, (250 - text_surface.get_width()/2, 0))


def run_program():
    # Initialize Pygame
    pygame.init()
    my_font = pygame.font.SysFont('Arial', 30)

    # Set up the display
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Text!!!")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_text(screen, my_font)

        pygame.display.flip()
        clock.tick(60)

run_program()
