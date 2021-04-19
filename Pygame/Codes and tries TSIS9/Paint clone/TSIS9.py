import pygame

pygame.init()

pygame.display.set_caption('Paint Clone for TSIS9')

WIDTH, HEIGHT = 1700, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
BROWN = (146, 46, 0)
RED = (255, 0, 0)
ORANGE = (255, 141, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 200)
GREY = (180, 180, 180)
WHITE = (255, 255, 255)


FONT = pygame.font.SysFont('Arial', 30)


def draw_circle():
    pass


def draw_rect():
    pass


def color_picking(click):
    COLOR = None

    black = pygame.Rect(1600, 0, 100, 60)
    brown = pygame.Rect(1600, 60, 100, 60)
    red = pygame.Rect(1600, 120, 100, 60)
    orange = pygame.Rect(1600, 180, 100, 60)
    yellow = pygame.Rect(1600, 240, 100, 60)
    green = pygame.Rect(1600, 300, 100, 60)
    blue = pygame.Rect(1600, 360, 100, 60)
    purple = pygame.Rect(1600, 420, 100, 60)
    grey = pygame.Rect(1600, 480, 100, 60)
    white = pygame.Rect(1600, 540, 100, 60)

    rectangle = pygame.Rect(1600, 600, 100, 60)
    circle = pygame.Rect(1600, 660, 100, 60)
    eraser = pygame.Rect(1600, 720, 100, 60)

    mx, my = pygame.mouse.get_pos()

    if black.collidepoint((mx, my)) and click:
        COLOR = BLACK
    elif brown.collidepoint((mx, my)) and click:
        COLOR = BROWN
    elif red.collidepoint((mx, my)) and click:
        COLOR = RED
    elif orange.collidepoint((mx, my)) and click:
        COLOR = ORANGE
    elif yellow.collidepoint((mx, my)) and click:
        COLOR = YELLOW
    elif green.collidepoint((mx, my)) and click:
        COLOR = GREEN
    elif brown.collidepoint((mx, my)) and click:
        COLOR = BROWN
    elif blue.collidepoint((mx, my)) and click:
        COLOR = BLUE
    elif purple.collidepoint((mx, my)) and click:
        COLOR = PURPLE
    elif grey.collidepoint((mx, my)) and click:
        COLOR = GREY
    elif white.collidepoint((mx, my)) and click:
        COLOR = WHITE
    elif rectangle.collidepoint((mx, my)) and click:
        draw_rect()
    elif circle.collidepoint((mx, my)) and click:
        draw_circle()
    elif eraser.collidepoint((mx, my)) and click:
        COLOR = WHITE

    if COLOR != None:
        print(COLOR)


def draw_menu(open):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, [0, 0, WIDTH, HEIGHT], 3)

    pygame.draw.line(WIN, BLACK, (1600, 0), (1600, 900), 3)

    for y in range(0, 760+1, 60):
        pygame.draw.rect(WIN, BLACK, [1600, y, 100, 61], 3)


def main():
    run = True
    click = False
    clear = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_c:
                    clear = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        draw_menu(open)
        color_picking(click)
        pygame.display.update()
        click = False

    pygame.quit()


if __name__ == '__main__':
    main()
