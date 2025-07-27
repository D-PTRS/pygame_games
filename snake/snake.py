import pygame
from sys import exit
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def snake_pos(x, y, pos_lst, length):
    """returns a list of positions where snake segments should be drawn"""
    if [x, y] != pos_lst[-1]:
        pos_lst.append([x, y])

    return pos_lst[-length:]


def snake(win, pos_lst):
    """draws a snake segment at each x, y in pos_lst """
    snake_rect = None
    for [x, y] in pos_lst:
        snake_rect = pygame.Rect(x, y, 20, 20)

        pygame.draw.rect(win, "green", snake_rect)

    # pygame.display.flip()
    #
    return snake_rect


def food(win, num_food, food_x, food_y, snake_rect, score, length, food_x_2, food_y_2, food_x_3, food_y_3):
    """draws food, generates new food if player eats it, and updates score and length"""
    food_rect = pygame.Rect(food_x, food_y, 20, 20)
    food_rect_2 = pygame.Rect(food_x_2, food_y_2, 20, 20)
    food_rect_3 = pygame.Rect(food_x_3, food_y_3, 20, 20)

    if snake_rect.colliderect(food_rect):
        food_x = random.randrange(40, 740, 20)
        food_y = random.randrange(140, 540, 20)
        score += 1
        length += 1

    if snake_rect.colliderect(food_rect_2):
        food_x_2 = random.randrange(40, 740, 20)
        food_y_2 = random.randrange(140, 540, 20)
        score += 1
        length += 1

    if snake_rect.colliderect(food_rect_3):
        food_x_3 = random.randrange(40, 740, 20)
        food_y_3 = random.randrange(140, 540, 20)
        score += 1
        length += 1


    if num_food == 0:
        pygame.draw.rect(win, "red", food_rect)
        pygame.draw.rect(win, "red", food_rect_2)
        pygame.draw.rect(win, "red", food_rect_3)

    # pygame.display.flip()

    return food_x, food_y, score, length, food_x_2, food_y_2, food_x_3, food_y_3


def draw(win, pos_lst):
    """draws grid"""
    win.fill((0, 0, 0))


    for num in range(40, WIDTH - 40, 20): # draws all vertical lines in grid
        line = pygame.Rect(num, 140, 1, HEIGHT - 200)
        pygame.draw.rect(win, "grey", line)

    for num in range(140, HEIGHT - 40, 20):  # draws all horizontal lines in grid
        line = pygame.Rect(40, num, WIDTH - 100, 1)
        pygame.draw.rect(win, "grey", line)

    snake_rect = snake(win, pos_lst)


    #pygame.display.flip()
    return snake_rect


def draw_score(win, text, font, x, y):
    img = font.render(text, False, "white")
    win.blit(img, (x, y))


def game_over_draw(win, game_over_text, font, x, y, score_font, reset_x, reset_y, reset_text, quit_text):
    img = font.render(game_over_text, False, "white")
    win.blit(img, (x, y))
    img_2 = score_font.render(reset_text, False, "white")
    win.blit(img_2, (reset_x, reset_y))
    img_2 = score_font.render(quit_text, False, "white")
    win.blit(img_2, (reset_x, reset_y + 40))


def main():

    fps = 12

    clock = pygame.time.Clock()

    run = True
    x, y = 140, 240
    pos_lst = [[100, 240], [120, 240], [140, 240]]

    length = 3

    num_food = 0

    score = 0

    left_side = pygame.Rect(39, 140, 1, HEIGHT - 200)
    right_side = pygame.Rect(741, 140, 1, HEIGHT - 200)
    top = pygame.Rect(40, 139, WIDTH - 100, 1)
    bottom = pygame.Rect(40, 540, WIDTH - 100, 1)

    snake_rect = snake(WIN, pos_lst)


    food_x = random.randrange(40, 740, 20)
    food_y = random.randrange(140, 540, 20)

    food_x_2 = random.randrange(40, 740, 20)
    food_y_2 = random.randrange(140, 540, 20)

    food_x_3 = random.randrange(40, 740, 20)
    food_y_3 = random.randrange(140, 540, 20)

    score_font = pygame.font.SysFont("Cooper", 40)
    game_over_font = pygame.font.SysFont("Cooper", 150)

    up = False
    down = False
    left = False
    right = False

    game_over = False

    while run:
        clock.tick(fps)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

            if e.type == pygame.KEYDOWN and not game_over:
                if e.key == pygame.K_w and not down:
                    up = True
                    down = False
                    left = False
                    right = False
                elif e.key == pygame.K_s and not up:
                    down = True
                    up = False
                    left = False
                    right = False
                elif e.key == pygame.K_a and not right:
                    left = True
                    up = False
                    down = False
                    right = False
                elif e.key == pygame.K_d and not left:
                    right = True
                    up = False
                    down = False
                    left = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    x, y = 140, 240
                    pos_lst = [[100, 240], [120, 240], [140, 240]]
                    game_over = False
                    score = 0
                    length = 3

                    up = False
                    down = False
                    left = False
                    right = False
                if e.key == pygame.K_q:
                    exit()

                    food_x = random.randrange(40, 740, 20)
                    food_y = random.randrange(140, 540, 20)

                    food_x_2 = random.randrange(40, 740, 20)
                    food_y_2 = random.randrange(140, 540, 20)

                    food_x_3 = random.randrange(40, 740, 20)
                    food_y_3 = random.randrange(140, 540, 20)

        if snake_rect.colliderect(left_side):
            game_over = True

        if snake_rect.colliderect(right_side):
            game_over = True

        if snake_rect.colliderect(top):
            game_over = True

        if snake_rect.colliderect(bottom):
            game_over = True

        if up:
            y -= 20
        elif down:
            y += 20
        elif left:
            x -= 20
        elif right:
            x += 20

        pos_lst = snake_pos(x, y, pos_lst, length)

        snake_rect = draw(WIN, pos_lst)
        food_x, food_y, score, length, food_x_2, food_y_2, food_x_3, food_y_3 = food(WIN, num_food,
                                                                                    food_x, food_y, snake_rect,
                                                                                     score, length,
                                                                                    food_x_2, food_y_2,
                                                                                     food_x_3, food_y_3)

        draw_score(WIN, str(score), score_font, 80, 100)

        if game_over:
            game_over_draw(WIN, "GAME OVER", game_over_font, 80, 280,
                           score_font, 280, 370, "press r to reset", "press q to quit")

        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()