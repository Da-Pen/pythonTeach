import pygame
import sys
from paddle import Paddle
import colors
from ball import Ball

def run_program():
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    left_paddle = Paddle(50)
    right_paddle = Paddle(925)
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(colors.BLACK)
        for i in range(25, 450, 50):
            pygame.draw.rect(screen, colors.GRAY, (487.5, i, 25, 25))

        ball.draw(screen)
        ball.move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.move_up()
        if keys[pygame.K_UP]:
            right_paddle.move_up()
        if keys[pygame.K_DOWN]:
            right_paddle.move_down()
        if keys[pygame.K_s]:
            left_paddle.move_down()
        if keys[pygame.K_p]:
            right_paddle.change_skin(colors.RED)
        if keys[pygame.K_l]:
            right_paddle.change_skin(colors.ORANGE)
        if keys[pygame.K_o]:
            right_paddle.change_skin(colors.YELLOW)
        if keys[pygame.K_i]:
            right_paddle.change_skin(colors.GREEN)
        if keys[pygame.K_k]:
            right_paddle.change_skin(colors.BLUE)
        if keys[pygame.K_m]:
            right_paddle.change_skin(colors.PURPLE)
        if keys[pygame.K_j]:
            right_paddle.change_skin(colors.WHITE)
        if keys[pygame.K_u]:
            right_paddle.change_skin(colors.BEIGE)
        if keys[pygame.K_n]:
            right_paddle.change_skin_into_santa_hat()
        if keys[pygame.K_h]:
            right_paddle.change_skin_into_pokka_dots()
        if keys[pygame.K_y]:
            right_paddle.change_skin_into_phone()
        if keys[pygame.K_b]:
            right_paddle.change_skin_into_domino()
        if keys[pygame.K_q]:
            left_paddle.change_skin(colors.RED)
        if keys[pygame.K_z]:
            left_paddle.change_skin(colors.ORANGE)
        if keys[pygame.K_x]:
            left_paddle.change_skin(colors.YELLOW)
        if keys[pygame.K_e]:
            left_paddle.change_skin(colors.GREEN)
        if keys[pygame.K_d]:
            left_paddle.change_skin(colors.BLUE)
        if keys[pygame.K_c]:
            left_paddle.change_skin(colors.PURPLE)
        if keys[pygame.K_r]:
            left_paddle.change_skin(colors.WHITE)
        if keys[pygame.K_a]:
            left_paddle.change_skin(colors.BEIGE)
        if keys[pygame.K_f]:
            left_paddle.change_skin_into_santa_hat()
        if keys[pygame.K_v]:
            left_paddle.change_skin_into_pokka_dots()
        if keys[pygame.K_t]:
            left_paddle.change_skin_into_phone()
        if keys[pygame.K_g]:
            left_paddle.change_skin_into_domino()

        left_paddle.draw(screen)
        right_paddle.draw(screen)
        pygame.display.flip()
        clock.tick(60)

run_program()
