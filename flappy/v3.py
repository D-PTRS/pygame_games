import pygame
import random
from sys import exit

pygame.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60


def draw(win, rect_x, rect_y, pipe_x, pipe_y, pipe_x2, pipe_y2, pipe2_height, pipe4_height,
         start_state, text, text_font, text_col, text_x, text_y, end_state):

    win.fill("blue")


    player = pygame.Rect(rect_x, rect_y, 70, 70)

    pipe = pygame.Rect(pipe_x, pipe_y, 150, 500)
    pipe2 = pygame.Rect(pipe_x, pipe_y - 500, 150, pipe2_height)

    pipe3 = pygame.Rect(pipe_x2, pipe_y2 -100, 150, 500)
    pipe4 = pygame.Rect(pipe_x2, pipe_y2 - 600, 150, pipe4_height)

    bottom = pygame.Rect(0, 580, 800, 20)
    top = pygame.Rect(0, -20, 800, 20)

    pygame.draw.rect(win, "yellow", player)

    pygame.draw.rect(win, "dark green", pipe)
    pygame.draw.rect(win, "dark green", pipe2)

    pygame.draw.rect(win, "dark green", pipe3)
    pygame.draw.rect(win, "dark green", pipe4)

    pygame.draw.rect(win, (150, 75, 0), bottom)
    pygame.draw.rect(win, "blue", top)

    if not start_state or end_state:
        img = text_font.render(text, True, text_col)
        win.blit(img, (text_x, text_y))

    pygame.display.flip()
    return (player, pipe, pipe2, pipe3, pipe4, bottom, top, pipe2_height, pipe4_height,
            pipe_y, pipe_y2)


def pipes(pipe_x, rect_x, pipe_x2, pipe2_height, pipe4_height, pipe_y, pipe_y2, start_state, score, end_state):
    state = random.randint(1, 5)

    if start_state:
        pipe_x -= 1
        pipe_x2 -= 1
    if end_state:
        pipe_x -= 0
        pipe_x2 -= 0

    if pipe_x == rect_x - 165:
        pipe_x = pipe_x2 + 400
        score += 1
        if state == 1:
            pipe_y = 320
        elif state == 2:
            pipe_y = 290
        elif state == 3:
            pipe_y = 470
        elif state == 4:
            pipe_y = 400
        elif state == 5:
            pipe_y = 500
    if pipe_x2 == rect_x - 165:
        pipe_x2 = pipe_x + 400
        score += 1
        if state == 1:
            pipe_y2 = 320
        elif state == 2:
            pipe_y2 = 290
        elif state == 3:
            pipe_y2 = 470
        elif state == 4:
            pipe_y2 = 400
        elif state == 5:
            pipe_y2 = 500
    return pipe_x, pipe_x2, pipe2_height, pipe4_height, pipe_y, pipe_y2, score


def main():
    clock = pygame.time.Clock()
    rect_x, rect_y = 200, 300
    pipe_x, pipe_y = 400, 400
    pipe_x2, pipe_y2 = 800, 400
    pipe2_height, pipe4_height = 300, 300

    run = True

    start_state = False
    end_state = False

    text_font = pygame.font.SysFont("Cooper", 30)
    text_col = (255, 255, 255)
    text = "PRESS ANY BUTTON TO START !\nPRESS ( r ) TO RESET"

    score = 0

    vel = 60

    while run:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE and not end_state:  # single space press ( can hold down key )
                    rect_y -= vel

            if e.type == pygame.KEYDOWN:
                start_state = True

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r: # restarts game if player presses ( r )
                    start_state = False
                    end_state = False
                    rect_x, rect_y = 200, 300
                    pipe_x, pipe_y = 400, 400
                    pipe_x2, pipe_y2 = 800, 400
                    pipe2_height, pipe4_height = 300, 300

                    text_font = pygame.font.SysFont("Cooper", 30)
                    text_col = (255, 255, 255)
                    text = "PRESS ANY BUTTON TO START !\nPRESS ( r ) TO RESET"

                    score = 0

        if start_state:
            rect_y += 3  # gravity
        if end_state:
            rect_y += 0


        pipe_x, pipe_x2, pipe2_height, pipe4_height, pipe_y, pipe_y2, score = (
            pipes(pipe_x, rect_x, pipe_x2, pipe2_height, pipe4_height,
            pipe_y, pipe_y2, start_state, score, end_state))

        player, pipe, pipe2, pipe3, pipe4, bottom, top, pipe2_height, pipe4_height, pipe_y, pipe_y2 = (
        draw(WIN, rect_x, rect_y,
        pipe_x, pipe_y, pipe_x2, pipe_y2,pipe2_height, pipe4_height,
        start_state, text, text_font, text_col, 300, 300, end_state))

        if player.colliderect(pipe):
            end_state = True
            start_state = False
            text = f"YOU GOT {score}"

        if player.colliderect(pipe2):
            end_state = True
            start_state = False
            text = f"YOU GOT {score}"

        if player.colliderect(pipe3):
            end_state = True
            start_state = False
            text = f"YOU GOT {score}"

        if player.colliderect(pipe4):
            end_state = True
            start_state = False
            text = f"YOU GOT {score}"

        if player.colliderect(bottom):
            end_state = True
            start_state = False
            text = f"YOU GOT {score}"

        if player.colliderect(top):
            end_state = True
            start_state = False
            text = f"YOU GOT {score}"


    pygame.quit()


if __name__ == "__main__":
    main()