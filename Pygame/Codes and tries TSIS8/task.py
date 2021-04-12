import pygame
import random
import time
import sys

pygame.init()

pygame.display.set_caption('TSIS 8')

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.Font(None, 60)
FONT_SMALL = pygame.font.Font(None, 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

FPS = 60
SPEED = 12
SCORE = 0

PLAYER = pygame.image.load('player.png')
PLAYER = pygame.transform.scale(PLAYER, (200, 120))
PLAYER = pygame.transform.rotate(PLAYER, 270)

ENEMY = []
for i in range(2):
    ENEMY.append(pygame.image.load(f'enemy_{i}.png'))
    ENEMY[i] = pygame.transform.scale(ENEMY[i], (200, 120))
    ENEMY[i] = pygame.transform.rotate(ENEMY[i], 270)

TREES = []
for i in range(3):
    TREES.append(pygame.image.load(f'tree_{i}.png'))
    TREES[i] = pygame.transform.scale(TREES[i], (100, 100))

BACKGROUND = pygame.image.load('road.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (HEIGHT, WIDTH))
BACKGROUND = pygame.transform.rotate(BACKGROUND, 90)

SCORE_TEXT = FONT.render(str(SCORE), True, BLACK)
GAMEOVER_TEXT = FONT.render('GAME OVER', True, BLUE)

# player = pygame.Rect(500, 500, 200, 120)
# enemy = random.choice(ENEMY)
# trees = random.choice(TREES)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy_0.png")
        self.image = pygame.transform.scale(self.image, (200, 120))
        self.image = pygame.transform.rotate(self.image, 270)

        #self.image = random.choice(ENEMY)

        self.surf = pygame.Surface((200, 120))
        self.rect = self.surf.get_rect(center=(random.randint(500, WIDTH), 5))

    def move(self):
        global SCORE
        self.rect.move_ip(0, random.randint(5, 15))
        if (self.rect.top > WIDTH):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(0, 150), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (200, 120))
        self.image = pygame.transform.rotate(self.image, 270)

        self.surf = pygame.Surface((200, 120))
        self.rect = self.surf.get_rect(center=(400, 800))

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top > 5:
            self.rect.move_ip(0, -SPEED)
        if pressed[pygame.K_DOWN] and self.rect.top < 800:
            self.rect.move_ip(0, SPEED)
        if pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-SPEED, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(SPEED, 0)


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(SCORE_TEXT, (20, 20))

    for i in all_sprites:
        WIN.blit(i.image, i.rect)
        i.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        # pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        WIN.fill(RED)
        WIN.blit(GAMEOVER_TEXT, (200, 250))

        pygame.display.update()

        for i in all_sprites:
            i.kill()
        time.sleep(2)

        pygame.quit()

    # WIN.blit(PLAYER, (player.x, player.y))
    # WIN.blit(enemy, (random.randint(170, 720), 5))
    # WIN.blit(trees, (random.randint(10, 100), 5))


# def player_movement(pressed, player):
#     if pressed[pygame.K_LEFT] and player.x - VEL > 170:
#         player.x -= VEL
#     if pressed[pygame.K_RIGHT] and player.x + VEL < 720:
#         player.x += VEL
#     if pressed[pygame.K_UP] and player.y - VEL > 5:
#         player.y -= VEL
#     if pressed[pygame.K_DOWN] and player.y + VEL < 800:
#         player.y += VEL


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        draw_window()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
