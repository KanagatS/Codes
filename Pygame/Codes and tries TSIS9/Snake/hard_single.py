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

FONT = pygame.font.SysFont('Courier', 35)
FONT_2 = pygame.font.SysFont('Arial', 48)


# pygame.mixer.music.load('bg.mp3')
# pygame.mixer.music.play(-1)

eaten = pygame.mixer.Sound('apple.wav')
end = pygame.mixer.Sound('end.wav')

FPS = 60
VEL = 5

area1y = random.randint(32, 200 - 35)
area2y = random.randint(400 + 35, 600-35)
area3y = random.randint(600 + 35, 800-35-35)

areasy = []
areasy.append(area1y)
areasy.append(area2y)
areasy.append(area3y)


class Food():
    def __init__(self):
        self.x = random.randint(32, WIDTH - 32 - 35)
        self.y = random.choice(areasy)
        self.image = pygame.transform.scale(
            pygame.image.load("apple.png"), (30, 30))
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
    pygame.mixer.music.stop()
    end.play()
    WIN.fill(RED)
    GAMEOVER_TEXT = FONT_2.render('GAME OVER!', True, BLACK)
    SCORE_TEXT = FONT_2.render('Your score: ' + str(snake.score), True, BLACK)

    WIN.blit(GAMEOVER_TEXT, (240, 250))
    WIN.blit(SCORE_TEXT, (240, 350))

    pygame.display.update()
    time.sleep(7.5)

    pygame.quit()


def collision_with_barrier():
    if 130 < snake.elements[0][0] < 160 and 200 < snake.elements[0][1] < 230:
        return True
    elif 160 < snake.elements[0][0] < 190 and 200 < snake.elements[0][1] < 230:
        return True
    elif 190 < snake.elements[0][0] < 220 and 200 < snake.elements[0][1] < 230:
        return True
    elif 220 < snake.elements[0][0] < 250 and 200 < snake.elements[0][1] < 230:
        return True
    elif 250 < snake.elements[0][0] < 280 and 200 < snake.elements[0][1] < 230:
        return True
    elif 280 < snake.elements[0][0] < 310 and 200 < snake.elements[0][1] < 230:
        return True
    elif 310 < snake.elements[0][0] < 340 and 200 < snake.elements[0][1] < 240:
        return True
    elif 340 < snake.elements[0][0] < 370 and 200 < snake.elements[0][1] < 240:
        return True
    elif 370 < snake.elements[0][0] < 400 and 200 < snake.elements[0][1] < 230:
        return True
    elif 400 < snake.elements[0][0] < 430 and 200 < snake.elements[0][1] < 230:
        return True
    elif 430 < snake.elements[0][0] < 460 and 200 < snake.elements[0][1] < 230:
        return True
    elif 460 < snake.elements[0][0] < 490 and 200 < snake.elements[0][1] < 230:
        return True
    elif 490 < snake.elements[0][0] < 520 and 200 < snake.elements[0][1] < 230:
        return True
    elif 520 < snake.elements[0][0] < 550 and 200 < snake.elements[0][1] < 230:
        return True
    elif 550 < snake.elements[0][0] < 580 and 200 < snake.elements[0][1] < 230:
        return True
    elif 580 < snake.elements[0][0] < 610 and 200 < snake.elements[0][1] < 230:
        return True
    elif 610 < snake.elements[0][0] < 640 and 200 < snake.elements[0][1] < 230:
        return True
    elif 640 < snake.elements[0][0] < 670 and 200 < snake.elements[0][1] < 230:
        return True
    elif 670 < snake.elements[0][0] < 700 and 200 < snake.elements[0][1] < 230:
        return True

    elif 130 < snake.elements[0][0] < 160 and 400 < snake.elements[0][1] < 430:
        return True
    elif 160 < snake.elements[0][0] < 190 and 400 < snake.elements[0][1] < 430:
        return True
    elif 190 < snake.elements[0][0] < 220 and 400 < snake.elements[0][1] < 430:
        return True
    elif 220 < snake.elements[0][0] < 250 and 400 < snake.elements[0][1] < 430:
        return True
    elif 250 < snake.elements[0][0] < 280 and 400 < snake.elements[0][1] < 430:
        return True
    elif 280 < snake.elements[0][0] < 310 and 400 < snake.elements[0][1] < 430:
        return True
    elif 310 < snake.elements[0][0] < 340 and 400 < snake.elements[0][1] < 240:
        return True
    elif 340 < snake.elements[0][0] < 370 and 400 < snake.elements[0][1] < 240:
        return True
    elif 370 < snake.elements[0][0] < 400 and 400 < snake.elements[0][1] < 430:
        return True
    elif 400 < snake.elements[0][0] < 430 and 400 < snake.elements[0][1] < 430:
        return True
    elif 430 < snake.elements[0][0] < 470 and 400 < snake.elements[0][1] < 430:
        return True
    elif 460 < snake.elements[0][0] < 490 and 400 < snake.elements[0][1] < 430:
        return True
    elif 490 < snake.elements[0][0] < 520 and 400 < snake.elements[0][1] < 430:
        return True
    elif 520 < snake.elements[0][0] < 550 and 400 < snake.elements[0][1] < 430:
        return True
    elif 550 < snake.elements[0][0] < 580 and 400 < snake.elements[0][1] < 430:
        return True
    elif 580 < snake.elements[0][0] < 610 and 400 < snake.elements[0][1] < 430:
        return True
    elif 610 < snake.elements[0][0] < 640 and 400 < snake.elements[0][1] < 430:
        return True
    elif 640 < snake.elements[0][0] < 670 and 400 < snake.elements[0][1] < 430:
        return True
    elif 670 < snake.elements[0][0] < 700 and 400 < snake.elements[0][1] < 430:
        return True

    elif 130 < snake.elements[0][0] < 160 and 600 < snake.elements[0][1] < 630:
        return True
    elif 160 < snake.elements[0][0] < 190 and 600 < snake.elements[0][1] < 630:
        return True
    elif 190 < snake.elements[0][0] < 220 and 600 < snake.elements[0][1] < 630:
        return True
    elif 220 < snake.elements[0][0] < 250 and 600 < snake.elements[0][1] < 630:
        return True
    elif 250 < snake.elements[0][0] < 280 and 600 < snake.elements[0][1] < 630:
        return True
    elif 280 < snake.elements[0][0] < 310 and 600 < snake.elements[0][1] < 630:
        return True
    elif 310 < snake.elements[0][0] < 340 and 600 < snake.elements[0][1] < 240:
        return True
    elif 340 < snake.elements[0][0] < 370 and 600 < snake.elements[0][1] < 240:
        return True
    elif 370 < snake.elements[0][0] < 400 and 600 < snake.elements[0][1] < 630:
        return True
    elif 400 < snake.elements[0][0] < 430 and 600 < snake.elements[0][1] < 630:
        return True
    elif 430 < snake.elements[0][0] < 460 and 600 < snake.elements[0][1] < 630:
        return True
    elif 460 < snake.elements[0][0] < 490 and 600 < snake.elements[0][1] < 630:
        return True
    elif 490 < snake.elements[0][0] < 520 and 600 < snake.elements[0][1] < 630:
        return True
    elif 520 < snake.elements[0][0] < 550 and 600 < snake.elements[0][1] < 630:
        return True
    elif 550 < snake.elements[0][0] < 580 and 600 < snake.elements[0][1] < 630:
        return True
    elif 580 < snake.elements[0][0] < 610 and 600 < snake.elements[0][1] < 630:
        return True
    elif 610 < snake.elements[0][0] < 640 and 600 < snake.elements[0][1] < 630:
        return True
    elif 640 < snake.elements[0][0] < 670 and 600 < snake.elements[0][1] < 630:
        return True
    elif 670 < snake.elements[0][0] < 700 and 600 < snake.elements[0][1] < 630:
        return True

    else:
        return False


def collision_with_tail():
    if snake.elements[0] in snake.elements[1:]:
        return True
    else:
        return False


def collision_with_wall():
    return ((snake.elements[0][0] > WIDTH - 32 - snake.radius // 2 or snake.elements[0][0] < 32 + snake.radius // 2) or
            (snake.elements[0][1] > HEIGHT - 32 - snake.radius // 2 or snake.elements[0][1] < 32 + snake.radius // 2))


def draw_barrier():
    WIN.blit(WALL, (130, 200))
    WIN.blit(WALL, (160, 200))
    WIN.blit(WALL, (190, 200))
    WIN.blit(WALL, (220, 200))
    WIN.blit(WALL, (250, 200))
    WIN.blit(WALL, (280, 200))
    WIN.blit(WALL, (310, 200))
    WIN.blit(WALL, (340, 200))
    WIN.blit(WALL, (370, 200))
    WIN.blit(WALL, (400, 200))
    WIN.blit(WALL, (430, 200))
    WIN.blit(WALL, (460, 200))
    WIN.blit(WALL, (490, 200))
    WIN.blit(WALL, (520, 200))
    WIN.blit(WALL, (550, 200))
    WIN.blit(WALL, (580, 200))
    WIN.blit(WALL, (610, 200))
    WIN.blit(WALL, (640, 200))
    WIN.blit(WALL, (670, 200))

    WIN.blit(WALL, (130, 400))
    WIN.blit(WALL, (160, 400))
    WIN.blit(WALL, (190, 400))
    WIN.blit(WALL, (220, 400))
    WIN.blit(WALL, (250, 400))
    WIN.blit(WALL, (280, 400))
    WIN.blit(WALL, (310, 400))
    WIN.blit(WALL, (340, 400))
    WIN.blit(WALL, (370, 400))
    WIN.blit(WALL, (400, 400))
    WIN.blit(WALL, (430, 400))
    WIN.blit(WALL, (460, 400))
    WIN.blit(WALL, (490, 400))
    WIN.blit(WALL, (520, 400))
    WIN.blit(WALL, (550, 400))
    WIN.blit(WALL, (580, 400))
    WIN.blit(WALL, (610, 400))
    WIN.blit(WALL, (640, 400))
    WIN.blit(WALL, (670, 400))

    WIN.blit(WALL, (130, 600))
    WIN.blit(WALL, (160, 600))
    WIN.blit(WALL, (190, 600))
    WIN.blit(WALL, (220, 600))
    WIN.blit(WALL, (250, 600))
    WIN.blit(WALL, (280, 600))
    WIN.blit(WALL, (310, 600))
    WIN.blit(WALL, (340, 600))
    WIN.blit(WALL, (370, 600))
    WIN.blit(WALL, (400, 600))
    WIN.blit(WALL, (430, 600))
    WIN.blit(WALL, (460, 600))
    WIN.blit(WALL, (490, 600))
    WIN.blit(WALL, (520, 600))
    WIN.blit(WALL, (550, 600))
    WIN.blit(WALL, (580, 600))
    WIN.blit(WALL, (610, 600))
    WIN.blit(WALL, (640, 600))
    WIN.blit(WALL, (670, 600))


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
        food.y = random.choice(areasy)
        eaten.play()


def show_score(x, y, score):
    score_text = FONT.render('Score: ' + str(score), True, BLACK)
    WIN.blit(score_text, (x, y))


def draw_window():
    WIN.fill(LIGHT_GREEN)

    draw_walls()
    draw_barrier()

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


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        if collision_with_wall() or collision_with_tail() or collision_with_barrier():
            game_over()

        draw_window()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
