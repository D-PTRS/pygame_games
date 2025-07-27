import pygame
from sys import exit
pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60


def draw(win, rect_x, rect_y, pipe_x, pipe_y, pipe_x2, pipe_y2):
    win.fill("blue")

    player = pygame.Rect(rect_x, rect_y, 70, 70)

    pipe = pygame.Rect(pipe_x, pipe_y, 150, 500)
    pipe2 = pygame.Rect(pipe_x, pipe_y - 500, 150, 300)

    pipe3 = pygame.Rect(pipe_x2, pipe_y2, 150, 500)
    pipe4 = pygame.Rect(pipe_x2, pipe_y2 - 500, 150, 300)

    bottom = pygame.Rect(0, 580, 800, 20)
    top = pygame.Rect(0, -20, 800, 20)

    pygame.draw.rect(win, "yellow", player)

    pygame.draw.rect(win, "dark green", pipe)
    pygame.draw.rect(win, "dark green", pipe2)

    pygame.draw.rect(win, "dark green", pipe3)
    pygame.draw.rect(win, "dark green", pipe4)

    pygame.draw.rect(win, (150, 75, 0), bottom)
    pygame.draw.rect(win, "blue", top)

    pygame.display.flip()
    return player, pipe, pipe2, pipe3, pipe4, bottom, top


def pipes(pipe_x, rect_x, pipe_x2):

    pipe_x -= 1
    pipe_x2 -= 1
    if pipe_x == rect_x - 165:
        pipe_x = pipe_x2 + 400
    if pipe_x2 == rect_x - 165:
        pipe_x2 = pipe_x + 400
    return pipe_x, pipe_x2


def main():
    clock = pygame.time.Clock()
    rect_x, rect_y = 200, 300
    pipe_x, pipe_y = 400, 400
    pipe_x2, pipe_y2 = 800, 400
    run = True
    i = 0
    last_used = 0
    can_use = True
    score = 0
    while run:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks() // 1000 # time in s
        if current_time == i:
            #print(current_time)
            i += 1

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE: # single space press ( can hold down key )
                    rect_y -= 60

        rect_y += 3 # gravity

        pipe_x, pipe_x2 = pipes(pipe_x, rect_x, pipe_x2)
        player, pipe, pipe2, pipe3, pipe4, bottom, top = draw(WIN, rect_x, rect_y, pipe_x, pipe_y, pipe_x2, pipe_y2)

        if player.colliderect(pipe):
            exit()

        if player.colliderect(pipe2):
            exit()

        if player.colliderect(pipe3):
            exit()

        if player.colliderect(pipe4):
            exit()

        if player.colliderect(bottom):
            exit()

        if player.colliderect(top):
            exit()


    pygame.quit()

if __name__ == "__main__":
    main()