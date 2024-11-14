import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def challenge_1(screen):
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (0, 0, 250, 250))
    pygame.draw.rect(screen, BLACK, (250, 250, 250, 250))


def challenge_2(screen):
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (0, 0, 250, 250))
    pygame.draw.rect(screen, BLACK, (250, 250, 250, 250))
    pygame.draw.circle(screen, BLUE, (250, 250), 50)


def challenge_3(screen):
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (0, 0, 250, 250))
    pygame.draw.rect(screen, BLACK, (250, 250, 250, 250))
    pygame.draw.rect(screen, WHITE, (125, 125, 250, 250))


def challenge_4(screen):
    screen.fill(BLACK)

    pygame.draw.circle(screen, RED, (250, 250), 50)
    pygame.draw.rect(screen, GREEN, (0, 200, 200, 100))
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))


# includes lines
def challenge_5(screen):
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, 0), (250, 250))
    pygame.draw.line(screen, WHITE, (500, 0), (250, 250))


def challenge_6(screen):
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (250, 0), (500, 250))
    pygame.draw.line(screen, BLUE, (500, 250), (250, 500))
    pygame.draw.line(screen, RED, (250, 500), (0, 250))
    pygame.draw.line(screen, GREEN, (0, 250), (250, 0))


def challenge_7(screen):
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 500))
    pygame.draw.line(screen, BLACK, (200, 0), (200, 500))
    pygame.draw.line(screen, BLACK, (300, 0), (300, 500))
    pygame.draw.line(screen, BLACK, (400, 0), (400, 500))


# uses loops
def challenge_8(screen):
    screen.fill(WHITE)
    for i in range(0, 501, 10):
        pygame.draw.line(screen, BLACK, (i, 0), (i, 500))


def challenge_9(screen):
    screen.fill(BLACK)
    for i in range(0, 501, 10):
        pygame.draw.line(screen, GREEN, (i, 0), (0, i))


def challenge_10(screen):
    screen.fill(BLACK)
    for i in range(0, 501, 10):
        pygame.draw.line(screen, GREEN, (i, 0), (0, 500 - i))


def challenge_11(screen):
    screen.fill(BLACK)
    for i in range(0, 501, 10):
        pygame.draw.line(screen, GREEN, (i, 0), (0, 500 - i))
        pygame.draw.line(screen, GREEN, (i, 500), (500, 500 - i))


def challenge_12(screen):
    screen.fill(BLACK)
    for i in range(250, 0, -10):
        color = GREEN
        if i % 20 == 0:
            color = BLACK
        pygame.draw.circle(screen, color, (250, 250), i)


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

        challenge_12(screen)

        pygame.display.flip()
        clock.tick(60)

run_program()
