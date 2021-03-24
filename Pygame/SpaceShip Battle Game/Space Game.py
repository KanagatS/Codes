import pygame
pygame.font.init()

# Article of Program
pygame.display.set_caption('Just Name')

# Parametres of Display
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Black border to separate areas
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

# Fonts of several text
HEALTH_FONT = pygame.font.SysFont('comiscant', 42)
WINNER_FONT = pygame.font.SysFont('comiscant', 100)

# Parametres of game
FPS = 60
VELOCITY = 10
BULLET_VELOCITY = 13
MAX_COUNT_OF_BULLETS = 5

# Definition of hitting
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Image of first spaceship
YELLOW_SPACESHIP = pygame.image.load('Sprites/Yellow.png')
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (55, 45))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)

# Image of another spaceship
RED_SPACESHIP = pygame.image.load('Sprites/Red.png')
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (55, 45))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)

# Image of background
BACKGROUND = pygame.image.load('Sprites/space.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))


# Function that displays images on the screen
def draw_window(red, yellow, bullets_red, bullets_yellow, RED_HP, YELLOW_HP):
    WIN.blit(BACKGROUND, (0, 0))  # First of all it's background

    pygame.draw.rect(WIN, BLACK, BORDER)  # Then it's separating border

    RED_HP_TEXT = HEALTH_FONT.render(
        'HEALTH: ' + str(RED_HP), 1, WHITE)  # Text of health (red)
    YELLOW_HP_TEXT = HEALTH_FONT.render(
        'HEALTH: ' + str(YELLOW_HP), 1, WHITE)  # Text of health (yellow)

    # Insrting text of health
    WIN.blit(RED_HP_TEXT, (WIDTH - RED_HP_TEXT.get_width() - 10, 10))
    WIN.blit(YELLOW_HP_TEXT, (10, 10))  # Also inserting text of health

    # Inserting yellow spaceship
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))  # Inserting red spaceship

    for bullet in bullets_yellow:  # Drawing and animating bullets of yellow spaceship
        pygame.draw.rect(WIN, YELLOW, bullet)

    for bullet in bullets_red:  # Drawing and animating bullets of red spaceship
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()  # Always need to update display


def yellow_movement(keys, yellow):  # Roles of each key
    if keys[pygame.K_a] and yellow.x - VELOCITY > 0:  # left
        yellow.x -= VELOCITY
    if keys[pygame.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x:  # right
        yellow.x += VELOCITY
    if keys[pygame.K_w] and yellow.y - VELOCITY > 0:  # up
        yellow.y -= VELOCITY
    if keys[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT - 5:  # down
        yellow.y += VELOCITY


def red_movement(keys, red):  # The same as previous
    if keys[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width:  # left
        red.x -= VELOCITY
    if keys[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH:  # right
        red.x += VELOCITY
    if keys[pygame.K_UP] and red.y - VELOCITY > 0:  # up
        red.y -= VELOCITY
    if keys[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT - 5:  # down
        red.y += VELOCITY


def bullet_movement(bullets_yellow, bullets_red, yellow, red):  # Bullet movement algorithm
    for bullet in bullets_yellow:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            bullets_yellow.remove(bullet)
        elif bullet.x > WIDTH:
            bullets_yellow.remove(bullet)

    for bullet in bullets_red:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            bullets_red.remove(bullet)
        elif bullet.x < 0:
            bullets_red.remove(bullet)


def draw_winner(text):  # Fucntion that will show who's winner
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                         2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)  # It will stand for 5000 ms or 5 s


def main():
    # Location by coordinates, then width and height
    red = pygame.Rect(700, 300, 55, 45)
    yellow = pygame.Rect(100, 300, 55, 45)

    bullets_red, bullets_yellow = [], []  # I created two list to contain bullets

    YELLOW_HP, RED_HP = 10, 10  # Hit Points of each spaceship

    clock = pygame.time.Clock()  # Start of main loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  # Termination condition
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:  # Roles of keys to fire the bullet
                if event.key == pygame.K_LCTRL and len(bullets_yellow) < MAX_COUNT_OF_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height // 2 - 5 // 2, 10, 5)
                    bullets_yellow.append(bullet)
                if event.key == pygame.K_RCTRL and len(bullets_red) < MAX_COUNT_OF_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height // 2 - 5 // 2, 10, 5)
                    bullets_red.append(bullet)

            if event.type == RED_HIT:  # Iterating the HP after hit
                RED_HP -= 1

            if event.type == YELLOW_HIT:  # Iterating the HP after hit
                YELLOW_HP -= 1

        winner_text = ''  # Initially it's the empty string

        if RED_HP <= 0:  # Condition for choosing a winner
            winner_text = 'YELLOW WINS'

        if YELLOW_HP <= 0:
            winner_text = 'RED WINS'

        if winner_text != '':  # it means that someone won
            draw_winner(winner_text)
            break

        keys = pygame.key.get_pressed()  # Access to pressed keys

        yellow_movement(keys, yellow)  # Function of roles of each keys
        red_movement(keys, red)

        # Same as previous, but with bullets
        bullet_movement(bullets_yellow, bullets_red, yellow, red)

        # Function that will show who's the winner
        draw_window(red, yellow, bullets_red,
                    bullets_yellow, RED_HP, YELLOW_HP)

    main()


if __name__ == "__main__":  # Be honestly i didn't totally understand, why we need this, but it should be :D
    main()
