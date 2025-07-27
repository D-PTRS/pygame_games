import pygame
from sys import exit
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Ball:
    def __init__(self, x_pos, y_pos, x_speed, y_speed, side, colour):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.side = side
        self.colour = colour
        self.rect = None

    def ball_draw(self):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.side, self.side)
        pygame.draw.rect(WIN, self.colour, self.rect, 0, 7)

        return self.rect

    def move_ball(self, bottom_section_1, middle_section_1, top_section_1,
                  bottom_section_2, middle_section_2, top_section_2,
                  right, left, top_border, bottom_border):
        """moves ball left or right and handles change of direction"""
        if right:
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed
        if left:
            self.x_pos -= self.x_speed
            self.y_pos -= self.y_speed

        if self.rect.colliderect(top_border) and left:
            self.y_speed = self.y_speed * -1
            self.y_pos += 4

        if self.rect.colliderect(top_border) and right:
            self.y_speed = self.y_speed * -1
            self.y_pos += 4

        if self.rect.colliderect(bottom_border) and left:
            self.y_speed = self.y_speed * -1
            self.y_pos -= 4

        if self.rect.colliderect(bottom_border) and right:
            self.y_speed = self.y_speed * -1
            self.y_pos -= 4

        if self.rect.colliderect(middle_section_1):
            right = True
            left = False
            self.y_speed = 0
            self.x_speed = 5

        if self.rect.colliderect(middle_section_2):
            left = True
            right = False
            self.y_speed = 0
            self.x_speed = 4

        if self.rect.colliderect(top_section_1):
            right = True
            left = False
            self.y_speed = 2
            self.y_speed = self.y_speed * -1

        if self.rect.colliderect(top_section_2):
            right = False
            left = True
            self.y_speed = 2
            self.y_speed = self.y_speed * -1

        if self.rect.colliderect(bottom_section_1):
            right = True
            left = False
            self.y_speed = 2
            self.y_speed = self.y_speed * 1

        if self.rect.colliderect(bottom_section_2):
            right = False
            left = True
            self.y_speed = 2
            self.y_speed = self.y_speed * 1

        return right, left, self.y_pos, self.y_speed


def paddle_move(player_1_y, player_2_y, ball_y, state, left, y_speed):
    """updates players y value based on key presses and computer logic follows ball y value"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_1_y -= 4
    if keys[pygame.K_s]:
        player_1_y += 4

    needed_y = ball_y

    if not left:
        if player_2_y != needed_y and state == 1:
            if needed_y > player_2_y:
                player_2_y += 1
            elif player_2_y > needed_y:
                player_2_y -= 1

        if player_2_y - 30 != needed_y and state == 2:
            if needed_y > player_2_y - 25:
                player_2_y += 2.9
            elif player_2_y - 30 > needed_y:
                player_2_y -= 2.9

        if player_2_y - 60 != needed_y and state == 3:
            if needed_y > player_2_y - 60:
                player_2_y += 2.9
            elif player_2_y - 60 > needed_y:
                player_2_y -= 2.9

    state = random.randint(1, 3)

    return player_1_y, player_2_y, ball_y, state, y_speed


def paddle(player_1_x, player_1_y, win, player_2_x, player_2_y):
    """draws both paddles at their x, y position (both paddles have different segments which changes ball direction)"""
    bottom_section_1 = pygame.Rect(player_1_x, player_1_y, 20, 30)
    middle_section_1 = pygame.Rect(player_1_x, player_1_y - 30, 20, 30)
    top_section_1 = pygame.Rect(player_1_x, player_1_y - 60, 20, 30)
    pygame.draw.rect(win, "red", bottom_section_1)
    pygame.draw.rect(win, "red", middle_section_1)
    pygame.draw.rect(win, "red", top_section_1)

    bottom_section_2 = pygame.Rect(player_2_x, player_2_y, 20, 30)
    middle_section_2 = pygame.Rect(player_2_x, player_2_y - 30, 20, 30)
    top_section_2 = pygame.Rect(player_2_x, player_2_y - 60, 20, 30)
    pygame.draw.rect(win, "blue", bottom_section_2)
    pygame.draw.rect(win, "blue", middle_section_2)
    pygame.draw.rect(win, "blue", top_section_2)

    return bottom_section_1, middle_section_1, top_section_1, bottom_section_2, middle_section_2, top_section_2


def draw(win, text, font, x, y, text_2, x2, y2):
    """colours background, draws line in the center and border and the score"""
    win.fill((0, 0, 0))
    pygame.draw.rect(win, "white", ((WIDTH / 2) - 1, 0, 1, HEIGHT))

    pygame.draw.rect(win, "white", (0, 0, 5, HEIGHT)) # left border
    pygame.draw.rect(win, "white", (WIDTH - 5, 0, 5, HEIGHT)) # right border
    pygame.draw.rect(win, "white", (0, 0, WIDTH, 5)) # top border
    pygame.draw.rect(win, "white", (0, HEIGHT - 5, WIDTH, 5)) # bottom border

    img = font.render(text, True, "white")
    win.blit(img, (x, y))

    img = font.render(text_2, True, "white")
    win.blit(img, (x2, y2))


def win_text(win, text, x, y, font):
    img = font.render(text, False, "white")
    win.blit(img, (x, y))


def main():
    run = True

    player_1_x, player_1_y = 35, 400
    comp_x, comp_y = WIDTH - 55, 400

    ball_x, ball_y = (WIDTH / 2) - 7.5, (HEIGHT / 2) - 15

    clock = pygame.time.Clock()

    ball_y_speed = 0

    ball = Ball(ball_x, ball_y, 4, ball_y_speed, 15, "white")

    ball_going_right = False
    ball_going_left = True

    left_border = pygame.Rect(0, 0, 5, HEIGHT)
    right_border = pygame.Rect(WIDTH - 5, 0, 5, HEIGHT)
    top_border = pygame.Rect(0, 0, WIDTH, 5)
    bottom_border = pygame.Rect(0, HEIGHT - 5, WIDTH, 5)

    state = random.randint(1,3)

    player_score = 0
    comp_score = 0

    text_font = pygame.font.SysFont("Cooper", 100)
    win_font = pygame.font.SysFont("Cooper", 250)

    while run:

        clock.tick(120)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        draw(WIN, str(player_score), text_font, 440, 20, str(comp_score), 520, 20)
        bottom_section_1, middle_section_1, top_section_1, bottom_section_2, middle_section_2, top_section_2 = (
        paddle(player_1_x, player_1_y, WIN, comp_x, comp_y))

        player_1_y, comp_y, ball_y, state, ball_y_speed= paddle_move(player_1_y, comp_y, ball_y, state, ball_going_left, ball_y_speed)

        ball_rect = ball.ball_draw()
        ball_going_right, ball_going_left, ball_y, ball_y_speed = ball.move_ball(bottom_section_1, middle_section_1, top_section_1,
                       bottom_section_2, middle_section_2, top_section_2,
                       ball_going_right, ball_going_left, top_border, bottom_border)

        if ball_rect.colliderect(left_border):
            comp_score += 1
            ball_y_speed = 0
            ball_x, ball_y = 500 - 7.5, 400 - 15
            ball = Ball(ball_x, ball_y, 4, ball_y_speed, 15, "white")
            ball_going_right = True
            ball_going_left = False
            player_1_x, player_1_y = 35, 400
            comp_x, comp_y = WIDTH - 55, 400

        if ball_rect.colliderect(right_border):
            player_score += 1
            ball_y_speed = 0
            ball_x, ball_y = 500 - 7.5, 400 - 15
            ball = Ball(ball_x, ball_y, 4, ball_y_speed, 15, "white")
            ball_going_right = False
            ball_going_left = True
            player_1_x, player_1_y = 35, 400
            comp_x, comp_y = WIDTH - 55, 400

        if comp_score == 5:
            text = "  ROBOT \n   WINS!"
            win_text(WIN, text, 70, 300, win_font)
            ball_going_right = False
            ball_going_left = False
            player_1_x, player_1_y = 35, 400
            comp_x, comp_y = WIDTH - 55, 400
            ball = Ball(ball_x, ball_y, 4, ball_y_speed, 0, "White")
        if player_score == 5:
            text = "YOU WIN!"
            win_text(WIN, text, 70, 300, win_font)
            ball_going_right = False
            ball_going_left = False
            player_1_x, player_1_y = 35, 400
            comp_x, comp_y = WIDTH - 55, 400
            ball = Ball(ball_x, ball_y, 4, ball_y_speed, 0, "White")


        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":
    main()
