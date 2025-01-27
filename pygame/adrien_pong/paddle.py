import pygame
import colors


class Paddle:
    def __init__(self, x):
        self.is_phone_skin_needed = False
        self.is_domino_skin_needed = False
        self.x = x
        self.y = 200
        self.width = 25
        self.height = 100
        self.speed = 3
        self.color = colors.GRAY
        self.is_the_santa_hat_needed = False
        self.is_pokka_dots_needed = False
        self.pokka_dot_color = colors.RED
    def move_up(self):
        self.y -= self.speed
        if self.y <= 0:
            self.y = 0
    def move_down(self):
        self.y += self.speed
        if self.y >= 400:
            self.y = 400
    def draw(self, screen):
        if self.is_the_santa_hat_needed == True:
            pygame.draw.polygon(screen, colors.RED, [(self.x - 6, self.y), (self.x + 12.5, self.y - 40), (self.x + 31, self.y)])
            pygame.draw.circle(screen, colors.WHITE, (self.x + 12.5, self.y - 50), 10)
            pygame.draw.rect(screen, colors.WHITE, (self.x, self.y, self.width, self.height))
            self.is_pokka_dots_needed = False
        elif self.is_pokka_dots_needed == True:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.circle(screen, self.pokka_dot_color, (self.x + 6, self.y + 16), 4)
            pygame.draw.circle(screen, self.pokka_dot_color, (self.x + 19, self.y + 29), 4)
            pygame.draw.circle(screen, self.pokka_dot_color, (self.x + 8, self.y + 41), 4)
            pygame.draw.circle(screen, self.pokka_dot_color, (self.x + 19, self.y + 59), 4)
            pygame.draw.circle(screen, self.pokka_dot_color, (self.x + 9, self.y + 74), 4)
            pygame.draw.circle(screen, self.pokka_dot_color, (self.x + 17, self.y + 84), 4)
            if self.color == colors.RED:
                self.pokka_dot_color = colors.BLUE
            elif self.color == colors.BLUE and self.pokka_dot_color == colors.BLUE:
                self.pokka_dot_color = colors.RED
            self.is_the_santa_hat_needed = False
        elif self.is_phone_skin_needed == True:
            pygame.draw.rect(screen, colors.BLUE, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, colors.BLACK, (self.x + 2, self.y + 2, self.width - 3.25, self.height - 15))
            pygame.draw.circle(screen, colors.WHITE, (self.x + 12.5, self.y + 95), 4, 2)
        elif self.is_domino_skin_needed:
            pygame.draw.rect(screen, colors.WHITE, (self.x, self.y, self.width, self.height))
            pygame.draw.line(screen, colors.BLACK, (self.x, self.y + 55), (self.x + self.width, self.y + self.height // 2 + 5), 2)
            pygame.draw.circle(screen, colors.BLACK, (self.x + 5, self.y + 15), 4)
            pygame.draw.circle(screen, colors.BLACK, (self.x + 20, self.y + 15), 4)
            pygame.draw.circle(screen, colors.BLACK, (self.x + 12, self.y + 30), 4)
            pygame.draw.circle(screen, colors.BLACK, (self.x + 5, self.y + 45), 4)
            pygame.draw.circle(screen, colors.BLACK, (self.x + 20, self.y + 45), 4)
            pygame.draw.circle(screen, colors.BLACK, (self.x + 7, self.y + 70), 4)
            pygame.draw.circle(screen, colors.BLACK, (self.x + 20, self.y + 85), 4)

        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    def change_skin(self, new_color):
        self.color = new_color
        self.is_the_santa_hat_needed = False
        self.is_pokka_dots_needed = False
        self.is_phone_skin_needed = False
        self.is_domino_skin_needed = False
    def change_skin_into_santa_hat(self):
        self.is_the_santa_hat_needed = True
        self.is_pokka_dots_needed = False
        self.is_phone_skin_needed = False
        self.is_domino_skin_needed = False
    def change_skin_into_pokka_dots(self):
        self.is_pokka_dots_needed = True
        self.is_the_santa_hat_needed = False
        self.is_phone_skin_needed = False
        self.is_domino_skin_needed = False
    def change_skin_into_phone(self):
        self.is_phone_skin_needed = True
        self.is_the_santa_hat_needed = False
        self.is_pokka_dots_needed = False
        self.is_domino_skin_needed = False
    def change_skin_into_domino(self):
        self.is_domino_skin_needed = True
        self.is_the_santa_hat_needed = False
        self.is_pokka_dots_needed = False
        self.is_phone_skin_needed = False
