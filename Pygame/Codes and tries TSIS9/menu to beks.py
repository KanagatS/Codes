import pygame
from os import system

pygame.init()

WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FONT = pygame.font.SysFont('Arial', 60)

BG = pygame.image.load('bg.jpg')
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))


def buttons(ok):
    easy = pygame.Rect(50, 600, 270, 80)
    medium = pygame.Rect(405, 600, 270, 80)
    hard = pygame.Rect(750, 600, 270, 80)

    x, y = pygame.mouse.get_pos()

    if easy.collidepoint(x, y) and ok:
        system('easy.py')
    if medium.collidepoint(x, y) and ok:
        system('medium.py')
    if hard.collidepoint(x, y) and ok:
        system('hard.py')


def draw_menu():
    WIN.blit(BG, (0, 0))

    WIN.blit(FONT.render('TSIS 9 by Beksultan', True, BLACK), (30, 30))
    WIN.blit(FONT.render('Snake game :D', True, BLACK), (30, 100))
    WIN.blit(FONT.render('Welcome! Choose you level', True, BLACK), (160, 250))
    WIN.blit(FONT.render("and LET'S GO", True, BLACK), (320, 320))

    WIN.blit(FONT.render('EASY', True, BLACK), (105, 610))
    WIN.blit(FONT.render('MEDIUM', True, BLACK), (417, 610))
    WIN.blit(FONT.render('HARD', True, BLACK), (800, 610))

    pygame.draw.rect(WIN, RED, [50, 600, 270, 80], 4)
    pygame.draw.rect(WIN, RED, [405, 600, 270, 80], 4)
    pygame.draw.rect(WIN, RED, [750, 600, 270, 80], 4)


def main():
    run = True
    click = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        draw_menu()
        buttons(click)
        pygame.display.update()
        click = False

    pygame.quit()


main()
