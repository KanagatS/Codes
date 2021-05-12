import pygame

pygame.init()

pygame.display.set_caption('Tic-Tac-Toe')

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CROSS = pygame.image.load('cross.png')
NIX = pygame.image.load('circle.png')


def buttons(click, obj):
    buttons = []

    bt1 = pygame.Rect(100, 130, 200, 200)
    buttons.append(bt1)
    bt2 = pygame.Rect(300, 130, 200, 200)
    buttons.append(bt2)
    bt3 = pygame.Rect(500, 130, 200, 200)
    buttons.append(bt3)

    bt4 = pygame.Rect(100, 330, 200, 200)
    buttons.append(bt4)
    bt5 = pygame.Rect(300, 330, 200, 200)
    buttons.append(bt5)
    bt6 = pygame.Rect(500, 330, 200, 200)
    buttons.append(bt6)

    bt7 = pygame.Rect(100, 530, 200, 200)
    buttons.append(bt7)
    bt8 = pygame.Rect(300, 530, 200, 200)
    buttons.append(bt8)
    bt9 = pygame.Rect(500, 530, 200, 200)
    buttons.append(bt9)

    mx, my = pygame.mouse.get_pos()

    # obj = None
    if obj == True:
        FIGURE = CROSS
    else:
        FIGURE = NIX

    for i in range(len(buttons)):
        if (buttons[i].collidepoint((mx, my)) and click):
            WIN.blit(FIGURE, (buttons[i].topleft))
            obj = not obj

    if obj != True:
        print(obj)


def draw_window():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, [100, 130, 600, 600], 3)

    for x in range(100, 700, 200):
        pygame.draw.line(WIN, BLACK, (x, 130), (x, 730), 3)

    for y in range(130, 730, 200):
        pygame.draw.line(WIN, BLACK, (100, y), (700, y), 3)


def main():
    clock = pygame.time.Clock()
    run = True
    FPS = 60
    click = False
    obj = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        draw_window()
        buttons(click, obj)
        pygame.display.update()
        clock.tick(FPS)
        click = False

    pygame.quit()


if __name__ == '__main__':
    main()
