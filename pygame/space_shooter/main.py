import pygame
import sys
import colors
from spaceship import Spaceship
from asteroid import BigAsteroid, NormalAsteroid
from lives import Lives

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


def run_program():
    # Initialize Pygame
    pygame.init()

    my_font = pygame.font.SysFont('Arial', 50)

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Shooter")

    clock = pygame.time.Clock()

    spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
    bullets = []
    asteroids = []

    lives = Lives(3)
    score = 0
    frame_counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        frame_counter += 1
        if frame_counter >= 10000:
            frame_counter = 0

        # update
        x = pygame.mouse.get_pos()[0]
        spaceship.set_x(x)

        # every 20 frames, generate a new bullet
        if frame_counter % 20 == 0:
            bullets.append(spaceship.shoot_bullet())

        # every 150 frames, generate a new big asteroid
        if frame_counter % 100 == 0:
            asteroids.append(BigAsteroid.new_big_asteroid(SCREEN_WIDTH))

        # every 70 frames, generate a new normal asteroid
        if frame_counter % 70 == 0:
            asteroids.append(NormalAsteroid.new_normal_asteroid(SCREEN_WIDTH))

        for bullet in bullets:
            bullet.update()
            # detect if out of screen
            if bullet.out_of_screen():
                bullets.remove(bullet)

        for asteroid in asteroids:
            asteroid.update()

            # detect if out of screen
            if asteroid.out_of_screen(SCREEN_HEIGHT):
                asteroids.remove(asteroid)
                lost_game = lives.lose_life()
                if lost_game:
                    print(f"Final score: {score}")
                    pygame.quit()
                    sys.exit()

            # detect if hit a bullet
            # Note: this is NOT the most efficient way to detect bullet collisions. Options:
            # This solution (both bullets and asteroids are unordered lists)
            # - Insert new bullet: O(1)
            # - Insert new asteroid: O(1)
            # - Bullet collision detection: O(a * b)
            #
            # Note that the bullet collision detection is run every frame, while
            # insertion of new bullets / asteroids is much less frequent
            #
            # Keep bullets sorted
            # - Insert new bullet: O(b)
            # - Insert new asteroid: O(1)
            # - Bullet collision detection: O(a * log(b))
            #
            # Keep asteroids sorted
            # - Insert new bullet: O(1)
            # - Insert new asteroid: O(a)
            # - Bullet collision detection: O(log(a) * b)
            #
            # Keep both asteroids and bullets sorted
            # - Insert new bullet: O(b)
            # - Insert new asteroid: O(a)
            # - Bullet collision detection (two pointer iteration): O(a + b)
            #
            # Keep bullets in binary search tree
            # - Insert new bullet: O(log(b))
            # - Insert new asteroid: O(1)
            # - Bullet collision detection: O(log(b) * a)
            # - Bullet removal: O(log(b))
            # - Note: the log(b)s are assuming that the tree is balanced. Can
            #   use a self-balancing tree (like an AVL) to make sure of this.
            #
            # Keep asteroids in binary search tree
            # - Vice versa of above
            #
            # Keep asteroids in quad tree
            # - This is advanced. Will introduce concept but not go in detail
            #   about time complexities. Just want to give students an idea of
            #   more possibilities.
            # - Note that this algorithm specifically applies to 2D space. The
            #   others are more general
            for bullet in bullets:
                if asteroid.hit_by_bullet(bullet):
                    asteroids.remove(asteroid)
                    asteroids.extend(asteroid.get_children())
                    score += 1

        # draw
        screen.fill(colors.BLACK)

        for bullet in bullets:
            bullet.draw(screen)

        spaceship.draw(screen)

        for asteroid in asteroids:
            asteroid.draw(screen)

        lives.draw(screen)

        text_surface = my_font.render(str(score), False, colors.WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH - text_surface.get_width() - 10, 5))

        pygame.display.flip()
        clock.tick(60)

run_program()
