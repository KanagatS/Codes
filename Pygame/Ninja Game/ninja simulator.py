import pygame

win = pygame.display.set_mode((1300, 650))
pygame.display.set_caption('First Game')

walkRight = [pygame.image.load('Ninja Sprites/Run__000.png'),
             pygame.image.load('Ninja Sprites/Run__001.png'),
             pygame.image.load('Ninja Sprites/Run__002.png'),
             pygame.image.load('Ninja Sprites/Run__003.png'),
             pygame.image.load('Ninja Sprites/Run__004.png'),
             pygame.image.load('Ninja Sprites/Run__005.png'),
             pygame.image.load('Ninja Sprites/Run__006.png'),
             pygame.image.load('Ninja Sprites/Run__007.png'),
             pygame.image.load('Ninja Sprites/Run__008.png'),
             pygame.image.load('Ninja Sprites/Run__009.png')]

walkLeft = [pygame.image.load('Ninja Sprites/RunLeft/Run_000.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_001.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_002.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_003.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_004.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_005.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_006.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_007.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_008.png'),
            pygame.image.load('Ninja Sprites/RunLeft/Run_009.png'), ]

playerStand = [pygame.image.load('Ninja Sprites/Idle__000.png'),
               pygame.image.load('Ninja Sprites/Idle__001.png'),
               pygame.image.load('Ninja Sprites/Idle__002.png'),
               pygame.image.load('Ninja Sprites/Idle__003.png'),
               pygame.image.load('Ninja Sprites/Idle__004.png'),
               pygame.image.load('Ninja Sprites/Idle__005.png'),
               pygame.image.load('Ninja Sprites/Idle__006.png'),
               pygame.image.load('Ninja Sprites/Idle__007.png'),
               pygame.image.load('Ninja Sprites/Idle__008.png'),
               pygame.image.load('Ninja Sprites/Idle__009.png')]

bg = pygame.image.load('Ninja Sprites/bgg.jpg')

clock = pygame.time.Clock()

x = 30
y = 650 - 130 - 439
width = 232
height = 439
speed = 10

is_jump = False
jump_cnt = 10

left, right = False, False
justStand = True
animCount = 0


def draw_window():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if right:
        win.blit(walkRight[animCount // 3], (x, y))
        animCount += 1
    elif left:
        win.blit(walkLeft[animCount // 3], (x, y))
        animCount += 1
    else:
        win.blit(playerStand[animCount // 3], (x, y))
        animCount += 1

    pygame.display.update()


run = True
while run:
    clock.tick(30)
    pygame.time.delay(50)

    # termination condition
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    # roles of buttons
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 10:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1300 - width - 10:
        x += speed
        right = True
        left = False
    else:
        left = False
        right = False
        # animCount = 0

    if not(is_jump):
        # if keys[pygame.K_UP] and y > 10:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < 650 - height - 10:
        #     y += speed
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_cnt >= -10:
            if jump_cnt < 0:
                y += (jump_cnt ** 2) / 2
            else:
                y -= (jump_cnt ** 2) / 2
            jump_cnt -= 1
        else:
            is_jump = False
            jump_cnt = 10

    # function to draw
    draw_window()

pygame.quit()
