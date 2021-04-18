import pygame

pygame.init()

pygame.display.set_caption('Paint Clone for TSIS9')

WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 160, 0)
YELLOW = (255, 255, 0)


def draw_menu(open):
    WIN.fill(WHITE)
    
    if open:
        pygame.draw.circle(WIN, BLACK, (250, 360), 60)

def main():
    run = True
    click = False
    open = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_n:
                    open = not open
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        draw_menu(open)

        pygame.display.update()
        click = False

    pygame.quit()


if __name__ == '__main__':
    main()
