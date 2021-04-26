import pygame
from os import system
import time

pygame.init()

pygame.display.set_caption('Snake Game Menu')

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ARROW = pygame.image.load('arrow.png')
ARROW = pygame.transform.rotate(ARROW, 90)

FONT = pygame.font.SysFont('Arial', 50)
FONT_small = pygame.font.SysFont('Arial', 35)
FONT_verysmall = pygame.font.SysFont('Arial', 22)


def menu_functions(click, single, multi):
    easy_level_button = pygame.Rect(60, 500, 175, 175)
    medium_level_button = pygame.Rect(313, 500, 175, 175)
    hard_level_button = pygame.Rect(565, 500, 175, 175)

    easy, medium, hard = False, False, False

    mx, my = pygame.mouse.get_pos()

    if easy_level_button.collidepoint((mx, my)) and click:
        easy = True
    if medium_level_button.collidepoint((mx, my)) and click:
        medium = True
    if hard_level_button.collidepoint((mx, my)) and click:
        hard = True

    if single:
        if easy:
            system('easy_single.py')
        elif medium:
            system('medium_single.py')
        elif hard:
            system("hard_single.py")

    elif multi:
        if easy:
            os.system('easy_multi.py')
        elif medium:
            os.system("medium_multi.py")
        elif hard:
            os.system("hard_multi.py")


def draw_menu(single, multi):
    WIN.fill((128, 128, 128))

    CHOOSE_MODE = FONT.render('GAME MODE', True, BLACK)
    SINGLEPLAYER = FONT_small.render('SINGLE', True, WHITE)
    MULTIPLAYER = FONT_small.render('MULTI', True, WHITE)
    CHOOSE_LEVEL = FONT.render('LEVEL', True, BLACK)

    WIN.blit(CHOOSE_MODE, (230, 130))
    WIN.blit(SINGLEPLAYER, (150, 260))
    WIN.blit(MULTIPLAYER, (550, 260))
    WIN.blit(CHOOSE_LEVEL, (290, 400))

    pygame.draw.rect(WIN, YELLOW, [60, 250, 310, 60], 3)
    pygame.draw.rect(WIN, YELLOW, [450, 250, 310, 60], 3)

    pygame.draw.rect(WIN, YELLOW, [60, 500, 175, 175], 3)
    pygame.draw.rect(WIN, YELLOW, [313, 500, 175, 175], 3)
    pygame.draw.rect(WIN, YELLOW, [565, 500, 175, 175], 3)

    EASY = FONT_small.render('EASY', True, WHITE)
    MEDIUM = FONT_small.render('MEDIUM', True, WHITE)
    HARD = FONT_small.render('HARD', True, WHITE)

    WIN.blit(EASY, (100, 560))
    WIN.blit(MEDIUM, (330, 560))
    WIN.blit(HARD, (605, 560))

    if single:
        WIN.blit(ARROW, (170, 320))
    elif multi:
        WIN.blit(ARROW, (565, 320))


def main():
    run = True
    click = False
    single, multi = False, False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_1:
                    single = True
                    multi = False
                elif event.key == pygame.K_2:
                    multi = True
                    single = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        draw_menu(single, multi)
        menu_functions(click, single, multi)
        pygame.display.update()
        click = False

    pygame.quit()


main()
