import pygame
import math
import sys

pygame.init()

pygame.display.set_caption('TSIS 7')

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.14

def draw_radians():
    pass

def draw_text():
    FONT = pygame.font.Font(None, 36)
    SIN_text = FONT.render('sin x', 1, BLACK)
    COS_text = FONT.render('cos x', 1, BLACK)
    WIN.blit(SIN_text, (550, 100))
    WIN.blit(COS_text, (550, 120))


def draw_cos():
    for x in range(80, 870 + 1):
        cos1 = 240 * math.cos((x - 80) / 80 * PI)
        cos2 = 240 * math.cos((x - 77) / 80 * PI)
        pygame.draw.aalines(WIN, BLUE, False, [(x - 1, cos1 + 325), (x, cos2 + 325)])


def draw_sin():
    for x in range(80, 870 + 1):
        sin1 = 240 * math.sin((x - 80) / 80 * PI)
        sin2 = 240 * math.sin((x - 77) / 80 * PI)
        pygame.draw.aalines(WIN, RED, False, [(x - 1, sin1 + 325), (x, sin2 + 325)])


def draw_grid_y():
    pygame.draw.line(WIN, BLACK, (80, 50), (80, 600))
    pygame.draw.line(WIN, BLACK, (870, 50), (870, 600))

    for y in range(50, 600 + 1, 69):
        pygame.draw.line(WIN, BLACK, (50, y), (900, y))

    for y in range(50, 600 + 1, 34):
        pygame.draw.line(WIN, BLACK, (50, y), (75, y))
        pygame.draw.line(WIN, BLACK, (875, y), (900, y))

    for y in range(50, 600 + 1, 17):
        pygame.draw.line(WIN, BLACK, (50, y), (68, y))
        pygame.draw.line(WIN, BLACK, (882, y), (900, y))


def draw_grid_x():
    pygame.draw.line(WIN, BLACK, (50, 80), (900, 80))
    pygame.draw.line(WIN, BLACK, (50, 570), (900, 570))

    for x in range(50, 900 + 1, 140):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 600))

    for x in range(50, 900 + 1, 70):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 75))
        pygame.draw.line(WIN, BLACK, (x, 600), (x, 575))

    for x in range(50, 900 + 1, 35):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 68))
        pygame.draw.line(WIN, BLACK, (x, 600), (x, 582))


def draw_lines():
    pygame.draw.line(WIN, BLACK, (50, 325), (900, 325), 3)  # x
    pygame.draw.line(WIN, BLACK, (475, 50), (475, 600), 3)  # y


def draw_borders():
    pygame.draw.rect(WIN, BLACK, (50, 50, 850, 550), 3)


def draw_window():
    WIN.fill(WHITE)
    draw_borders()
    draw_lines()
    draw_grid_x()
    draw_grid_y()
    draw_sin()
    draw_cos()
    draw_text()
    draw_radians()
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
