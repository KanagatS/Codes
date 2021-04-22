import pygame
import random


def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


def main():
    screen = pygame.display.set_mode((1600, 900))
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10

    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }

    BLACK = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and radius < 30:
                    radius += 1
                if event.key == pygame.K_DOWN and radius > 3:
                    radius -= 1
                if event.key == pygame.K_c:
                    screen.fill((255, 255, 255))
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                color = (0, 12, 49)
                pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    drawLine(screen, last_pos, event.pos, radius, color)
                last_pos = event.pos
        #screen.fill((255, 255, 255))
        pygame.display.flip()

    pygame.quit()


main()
