import pygame
import random
import math
from pygame import mixer

# inintalizing the pygame


pygame.init()

# new blank window
screen = pygame.display.set_mode((800, 600))
# Title and Icon
pygame.display.set_caption("Gamer")
icon = pygame.image.load('d.png')
pygame.display.set_icon(icon)

# Background
back = pygame.image.load("back.jpg")
# Background Music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Player
player = pygame.image.load("spaceship.png")
playerX = 370
playerY = 500
playerx_change = 0
# emeny
enemy = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 1
for i in range(num_of_enemy):
    enemy.append(pygame.image.load("mega.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(10, 250))
    enemyX_change.append(0.3)
    enemyY_change.append(100)
# bullet
bullet_img = pygame.image.load("bullet.png")

bulletY = 500
bulletY_change = 1
bulletX_change = 0
bullet_state = "ready"
# Score
score_value = 0
font = pygame.font.Font("fonts.ttf", 32)
testX = 10
testy = 10


def show_show(x, y):
    score = font.render("Socre :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Sounds
bullet_sound = mixer.Sound("laser.wav")
died = mixer.Sound("explosion.wav")

# can't see
# if bullet_state == fire the bullet will appear

def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def position_player(x, y):
    screen.blit(player, (x, y))


def position_enemy(x, y, i):
    screen.blit(enemy[i], (x, y))


def cool(enemyX, enemyY, bulletX, bulletY):
    dis = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if dis <= 40:
        return True


# making the while loop to stop the program stop quickly
running = True  # ture for flase :)
while running:

    for event in pygame.event.get():  # this check every single time that button is clicked or not
        if event.type == pygame.QUIT:
            running = False
    screen.blit(back, (0, 0))
    if enemyY[i] > 480:
        True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerx_change = +2
        if event.key == pygame.K_LEFT:
            playerx_change = -2
        if event.key == pygame.K_SPACE:
            print("if main")

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            playerx_change = 0
        if event.key == pygame.K_SPACE:
            if bullet_state == "ready":
                bulletX = playerX
                bullet_sound.play()
                fire(bulletX, bulletY)

    playerX += playerx_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        if cool(enemyX[i], enemyY[i], playerX, bulletY) is True:
            bulletY = 500
            died.play()
            bullet_state = "ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(10, 250)
            score_value += 1
        position_enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletY_change
    # collistion
    # cool(enemyX , enemyY , playerX , bulletY)

    position_player(playerX, playerY)
    show_show(testX, testy)

    pygame.display.update()  # update function to update the window or screen every changes
    # background
