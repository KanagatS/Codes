import pygame
import random
import time

pygame.init()

pygame.display.set_caption('SNAKE')

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_GREEN = (153, 255, 153)
YELLOW = (255, 255, 0)

WALL = pygame.image.load('wall.png')
wall =pygame.transform.scale(pygame.image.load("wall.png"),(30,30))

FONT = pygame.font.SysFont('Courier', 35)
FONT_2 = pygame.font.SysFont('Arial', 48)

FPS = 60
VEL = 5



class Food():
    def __init__(self):
        self.x = random.randint(32, WIDTH - 32 - 35)
        self.y = random.randint(32, HEIGHT - 32 - 35)
        self.image = pygame.image.load('apple.png')
        self.image = pygame.transform.scale(self.image, (35, 35))

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


class Snake():
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx = VEL
        self.dy = 0
        self.elements = [[100, 100], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False
        self.dir = 'right'

    def draw(self):
        for element in self.elements[1:]:
            pygame.draw.circle(WIN, BLACK, element, self.radius)

    def move(self):
        if self.is_add:
            self.addSnake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

        if self.elements[0][0] > WIDTH:
            self.elements[0][0] = 0
        elif self.elements[0][0] < 0:
            self.elements[0][0] = WIDTH
        elif self.elements[0][1] > HEIGHT:
            self.elements[0][1] = 0
        elif self.elements[0][1] < 0:
            self.elements[0][1] = HEIGHT

    def addSnake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False


def game_over():
    WIN.fill(RED)
    GAMEOVER_TEXT = FONT_2.render('GAME OVER!', True, BLACK)
    SCORE_TEXT = FONT_2.render('Your score: ' + str(snake.score), True, BLACK)

    WIN.blit(GAMEOVER_TEXT, (240, 250))
    WIN.blit(SCORE_TEXT, (240, 350))

    pygame.display.update()
    time.sleep(3)

    pygame.quit()


def collision_with_tail():
    if snake.elements[0] in snake.elements[1:]:
        return True
    else:
        return False


def collision_with_wall():
    return ((snake.elements[0][0] > WIDTH - 32 - snake.radius // 2 or snake.elements[0][0] < 32 + snake.radius // 2) or
            (snake.elements[0][1] > HEIGHT - 32 - snake.radius // 2 or snake.elements[0][1] < 32 + snake.radius // 2))


def draw_walls():
    for x in range(32, WIDTH - 32, 32):
        WIN.blit(WALL, (x, 0))
        WIN.blit(WALL, (x, HEIGHT - 32))
    for y in range(0, HEIGHT, 32):
        WIN.blit(WALL, (0, y))
        WIN.blit(WALL, (WIDTH - 32, y))


def collision_with_food():
    if (food.x in range(snake.elements[0][0] - 35, snake.elements[0][0]) and
            (food.y in range(snake.elements[0][1] - 35, snake.elements[0][1]))):
        snake.is_add = True
        food.x = random.randint(32, WIDTH - 32 - 35)
        food.y = random.randint(32, HEIGHT - 32 - 35)


def show_score(x, y, score):
    score_text = FONT.render('Score: ' + str(score), True, BLACK)
    WIN.blit(score_text, (x, y))


def draw_window():
    WIN.fill(LIGHT_GREEN)
    WIN.blit(wall, (130, 200))
    WIN.blit(wall, (160, 200))
    WIN.blit(wall, (190, 200))
    WIN.blit(wall, (220, 200))
    WIN.blit(wall, (250, 200))
    WIN.blit(wall, (280, 200))
    WIN.blit(wall, (310, 200))
    WIN.blit(wall, (340, 200))
    WIN.blit(wall, (370, 200))
    WIN.blit(wall, (400, 200))
    WIN.blit(wall, (430, 200))
    WIN.blit(wall, (460, 200))
    WIN.blit(wall, (490, 200))
    WIN.blit(wall, (520, 200))
    WIN.blit(wall, (550, 200))
    WIN.blit(wall, (580, 200))
    WIN.blit(wall, (610, 200))
    WIN.blit(wall, (640, 200))
    WIN.blit(wall, (670, 200))

    WIN.blit(wall, (130, 400))
    WIN.blit(wall, (160, 400))
    WIN.blit(wall, (190, 400))
    WIN.blit(wall, (220, 400))
    WIN.blit(wall, (250, 400))
    WIN.blit(wall, (280, 400))
    WIN.blit(wall, (310, 400))
    WIN.blit(wall, (340, 400))
    WIN.blit(wall, (370, 400))
    WIN.blit(wall, (400, 400))
    WIN.blit(wall, (430, 400))
    WIN.blit(wall, (460, 400))
    WIN.blit(wall, (490, 400))
    WIN.blit(wall, (520, 400))
    WIN.blit(wall, (550, 400))
    WIN.blit(wall, (580, 400))
    WIN.blit(wall, (610, 400))
    WIN.blit(wall, (640, 400))
    WIN.blit(wall, (670, 400))

    WIN.blit(wall, (130, 600))
    WIN.blit(wall, (160, 600))
    WIN.blit(wall, (190, 600))
    WIN.blit(wall, (220, 600))
    WIN.blit(wall, (250, 600))
    WIN.blit(wall, (280, 600))
    WIN.blit(wall, (310, 600))
    WIN.blit(wall, (340, 600))
    WIN.blit(wall, (370, 600))
    WIN.blit(wall, (400, 600))
    WIN.blit(wall, (430, 600))
    WIN.blit(wall, (460, 600))
    WIN.blit(wall, (490, 600))
    WIN.blit(wall, (520, 600))
    WIN.blit(wall, (550, 600))
    WIN.blit(wall, (580, 600))
    WIN.blit(wall, (610, 600))
    WIN.blit(wall, (640, 600))
    WIN.blit(wall, (670, 600))

    draw_walls()

    movement()

    snake.draw()
    snake.move()

    collision_with_food()

    food.draw()

    show_score(40, 35, snake.score)


def movement():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and snake.dir != 'left':
        snake.dx = VEL
        snake.dy = 0
        snake.dir = 'right'
    elif pressed[pygame.K_LEFT] and snake.dir != 'right':
        snake.dx = -VEL
        snake.dy = 0
        snake.dir = 'left'
    elif pressed[pygame.K_UP] and snake.dir != 'down':
        snake.dx = 0
        snake.dy = -VEL
        snake.dir = 'up'
    elif pressed[pygame.K_DOWN] and snake.dir != 'up':
        snake.dx = 0
        snake.dy = VEL
        snake.dir = 'down'





snake = Snake()
food = Food()
run=True
clock = pygame.time.Clock()
def main():

    run = True

    while run:

        if 130 < snake.elements[0][0] < 160 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 160 < snake.elements[0][0] < 190 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 190 < snake.elements[0][0] < 220 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 220 < snake.elements[0][0] < 250 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 250 < snake.elements[0][0] < 280 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 280 < snake.elements[0][0] < 310 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 310 < snake.elements[0][0] < 340 and 200 < snake.elements[0][1] < 240:
            game_over()
        if 340 < snake.elements[0][0] < 370 and 200 < snake.elements[0][1] < 240:
            game_over()
        if 370 < snake.elements[0][0] < 400 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 400 < snake.elements[0][0] < 430 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 430 < snake.elements[0][0] < 460 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 460 < snake.elements[0][0] < 490 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 490 < snake.elements[0][0] < 520 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 520 < snake.elements[0][0] < 550 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 580 < snake.elements[0][0] < 610 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 610 < snake.elements[0][0] < 640 and 200 < snake.elements[0][1] < 230:
            game_over()
        if 640 < snake.elements[0][0] < 670 and 200 < snake.elements[0][1] < 230:
            game_over()

        if 130 < snake.elements[0][0] < 160 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 160 < snake.elements[0][0] < 190 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 190 < snake.elements[0][0] < 220 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 220 < snake.elements[0][0] < 250 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 250 < snake.elements[0][0] < 280 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 280 < snake.elements[0][0] < 310 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 310 < snake.elements[0][0] < 340 and 400 < snake.elements[0][1] < 240:
            game_over()
        if 340 < snake.elements[0][0] < 370 and 400 < snake.elements[0][1] < 240:
            game_over()
        if 370 < snake.elements[0][0] < 400 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 400 < snake.elements[0][0] < 430 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 430 < snake.elements[0][0] < 470 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 460 < snake.elements[0][0] < 490 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 490 < snake.elements[0][0] < 520 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 520 < snake.elements[0][0] < 550 and 400 < snake.elements[0][1] < 430:
            game_over()

        if 550 < snake.elements[0][0] < 580 and 400 < snake.elements[0][1] < 430:
            game_over()

        if 580 < snake.elements[0][0] < 610 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 610 < snake.elements[0][0] < 640 and 400 < snake.elements[0][1] < 430:
            game_over()
        if 640 < snake.elements[0][0] < 670 and 400 < snake.elements[0][1] < 430:
            game_over()

        if 130 < snake.elements[0][0] < 160 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 160 < snake.elements[0][0] < 190 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 190 < snake.elements[0][0] < 220 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 220 < snake.elements[0][0] < 250 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 250 < snake.elements[0][0] < 280 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 280 < snake.elements[0][0] < 310 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 310 < snake.elements[0][0] < 340 and 600 < snake.elements[0][1] < 240:
            game_over()
        if 340 < snake.elements[0][0] < 370 and 600 < snake.elements[0][1] < 240:
            game_over()
        if 370 < snake.elements[0][0] < 400 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 400 < snake.elements[0][0] < 430 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 430 < snake.elements[0][0] < 470 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 460 < snake.elements[0][0] < 490 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 490 < snake.elements[0][0] < 520 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 520 < snake.elements[0][0] < 550 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 580 < snake.elements[0][0] < 610 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 610 < snake.elements[0][0] < 640 and 600 < snake.elements[0][1] < 630:
            game_over()
        if 640 < snake.elements[0][0] < 670 and 600 < snake.elements[0][1] < 630:
            game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


        if collision_with_wall() or collision_with_tail():
            game_over()

        draw_window()
        pygame.display.update()
        clock.tick(FPS)



    pygame.quit()


if __name__ == '__main__':
    main()
