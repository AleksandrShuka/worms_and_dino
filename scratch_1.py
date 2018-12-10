import pygame
import random


class Bullet:
    def __init__(self, x, y, facing, isLeft):
        self.isLeft = isLeft
        self.x = x
        self.y = y
        self.speed = 10 * facing

    def draw(self, win):
        if self.isLeft:
            win.blit(playerBulletsLeft[animationCount // 4], (self.x + weightPerson - 40, self.y + heightPerson - 60))
        else:
            win.blit(playerBulletsRight[animationCount // 4], (self.x + weightPerson - 40, self.y + heightPerson - 60))


class Worm:
    def __init__(self):
        self.x = random.randrange(0, 1230)
        self.y = 590

    def draw(self):
        win.blit(enemyWorm[animationCount // 4], (self.x, self.y))


def draw_window():
    win.blit(background, (0, 0))
    global animationCount, isLeft, x, worms, isDie

    if animationCount == 40:
        animationCount = 0

    if right:
        isLeft = False
        if isRun:
            if not isJump:
                win.blit(playerRunRight[animationCount // 4], (x, y))
            else:
                win.blit(playerJumpRight[animationCount // 4], (x, y))
        else:
            if not isJump:
                win.blit(playerWalkRight[animationCount // 4], (x, y))
            else:
                win.blit(playerJumpRight[animationCount // 4], (x, y))
    elif left:
        isLeft = True
        if isRun:
            if not isJump:
                win.blit(playerRunLeft[animationCount // 4], (x, y))
            else:
                win.blit(playerJumpLeft[animationCount // 4], (x, y))
        else:
            if not isJump:
                win.blit(playerWalkLeft[animationCount // 4], (x, y))
            else:
                win.blit(playerJumpLeft[animationCount // 4], (x, y))
    else:
        if isJump and not isLeft:
            win.blit(playerJumpRight[animationCount // 4], (x, y))
        elif isJump and isLeft:
            win.blit(playerJumpLeft[animationCount // 4], (x, y))
        elif not isLeft:
            if x < 0:
                x += 5
            win.blit(playerStandRight[animationCount // 4], (x, y))
        else:
            if x > 1240 - weightPerson:
                x -= 10
            win.blit(playerStandLeft[animationCount // 4], (x, y))

    for elem in bullets:
        elem.draw(win)

    for worm in worms:
        flag = 0
        if (x < worm.x and worm.x - x < 50 or x > worm.x and x - worm.x < 5) and worm.y - y < 40:
            isDie = True
        for elem in bullets:
            if (elem.x < worm.x and worm.x - elem.x < 50 or elem.x > worm.x and elem.x - worm.x < 5) and worm.y - elem.y < 40:
                worms.pop(worms.index(worm))
                bullets.pop(bullets.index(elem))
                flag = 1
        if not flag:
            worm.draw()

    animationCount += 1
    pygame.display.update()


pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Welcome to DOPSA")

background = pygame.image.load('1_game_background.png')
background = pygame.transform.scale(background, (1280, 720))

playerBulletsRight = [pygame.image.load('bullet_right/bullet_1.png'), pygame.image.load('bullet_right/bullet_2.png'),
                      pygame.image.load('bullet_right/bullet_3.png'), pygame.image.load('bullet_right/bullet_4.png'),
                      pygame.image.load('bullet_right/bullet_5.png'), pygame.image.load('bullet_right/bullet_6.png'),
                      pygame.image.load('bullet_right/bullet_7.png'), pygame.image.load('bullet_right/bullet_8.png'),
                      pygame.image.load('bullet_right/bullet_9.png'), pygame.image.load('bullet_right/bullet_10.png')]
playerBulletsLeft = [pygame.image.load('bullet_left/bullet_1.png'), pygame.image.load('bullet_left/bullet_2.png'),
                     pygame.image.load('bullet_left/bullet_3.png'), pygame.image.load('bullet_left/bullet_4.png'),
                     pygame.image.load('bullet_left/bullet_5.png'), pygame.image.load('bullet_left/bullet_6.png'),
                     pygame.image.load('bullet_left/bullet_7.png'), pygame.image.load('bullet_left/bullet_8.png'),
                     pygame.image.load('bullet_left/bullet_9.png'), pygame.image.load('bullet_left/bullet_10.png')]
playerWalkRight = [pygame.image.load('walk_right/walk_1.png'), pygame.image.load('walk_right/walk_2.png'),
                   pygame.image.load('walk_right/walk_3.png'), pygame.image.load('walk_right/walk_4.png'),
                   pygame.image.load('walk_right/walk_5.png'), pygame.image.load('walk_right/walk_6.png'),
                   pygame.image.load('walk_right/walk_7.png'), pygame.image.load('walk_right/walk_8.png'),
                   pygame.image.load('walk_right/walk_9.png'), pygame.image.load('walk_right/walk_10.png')]
playerWalkLeft = [pygame.image.load('walk_left/walk_1.png'), pygame.image.load('walk_left/walk_2.png'),
                  pygame.image.load('walk_left/walk_3.png'), pygame.image.load('walk_left/walk_4.png'),
                  pygame.image.load('walk_left/walk_5.png'), pygame.image.load('walk_left/walk_6.png'),
                  pygame.image.load('walk_left/walk_7.png'), pygame.image.load('walk_left/walk_8.png'),
                  pygame.image.load('walk_left/walk_9.png'), pygame.image.load('walk_left/walk_10.png')]
playerStandRight = [pygame.image.load('idle_right/idle_1.png'), pygame.image.load('idle_right/idle_2.png'),
                    pygame.image.load('idle_right/idle_3.png'), pygame.image.load('idle_right/idle_4.png'),
                    pygame.image.load('idle_right/idle_5.png'), pygame.image.load('idle_right/idle_6.png'),
                    pygame.image.load('idle_right/idle_7.png'), pygame.image.load('idle_right/idle_8.png'),
                    pygame.image.load('idle_right/idle_9.png'), pygame.image.load('idle_right/idle_10.png')]
playerStandLeft = [pygame.image.load('idle_left/idle_1.png'), pygame.image.load('idle_left/idle_2.png'),
                   pygame.image.load('idle_left/idle_3.png'), pygame.image.load('idle_left/idle_4.png'),
                   pygame.image.load('idle_left/idle_5.png'), pygame.image.load('idle_left/idle_6.png'),
                   pygame.image.load('idle_left/idle_7.png'), pygame.image.load('idle_left/idle_8.png'),
                   pygame.image.load('idle_left/idle_9.png'), pygame.image.load('idle_left/idle_10.png')]
playerRunRight = [pygame.image.load('run_right/run_1.png'), pygame.image.load('run_right/run_2.png'),
                  pygame.image.load('run_right/run_3.png'), pygame.image.load('run_right/run_4.png'),
                  pygame.image.load('run_right/run_5.png'), pygame.image.load('run_right/run_6.png'),
                  pygame.image.load('run_right/run_7.png'), pygame.image.load('run_right/run_8.png'),
                  pygame.image.load('run_right/run_9.png'), pygame.image.load('run_right/run_10.png')]
playerRunLeft = [pygame.image.load('run_left/run_1.png'), pygame.image.load('run_left/run_2.png'),
                 pygame.image.load('run_left/run_3.png'), pygame.image.load('run_left/run_4.png'),
                 pygame.image.load('run_left/run_5.png'), pygame.image.load('run_left/run_6.png'),
                 pygame.image.load('run_left/run_7.png'), pygame.image.load('run_left/run_8.png'),
                 pygame.image.load('run_left/run_9.png'), pygame.image.load('run_left/run_10.png')]
playerJumpRight = [pygame.image.load('jump_right/jump_1.png'), pygame.image.load('jump_right/jump_2.png'),
                   pygame.image.load('jump_right/jump_3.png'), pygame.image.load('jump_right/jump_4.png'),
                   pygame.image.load('jump_right/jump_5.png'), pygame.image.load('jump_right/jump_6.png'),
                   pygame.image.load('jump_right/jump_7.png'), pygame.image.load('jump_right/jump_8.png'),
                   pygame.image.load('jump_right/jump_9.png'), pygame.image.load('jump_right/jump_10.png')]
playerJumpLeft = [pygame.image.load('jump_left/jump_1.png'), pygame.image.load('jump_left/jump_2.png'),
                  pygame.image.load('jump_left/jump_3.png'), pygame.image.load('jump_left/jump_4.png'),
                  pygame.image.load('jump_left/jump_5.png'), pygame.image.load('jump_left/jump_6.png'),
                  pygame.image.load('jump_left/jump_7.png'), pygame.image.load('jump_left/jump_8.png'),
                  pygame.image.load('jump_left/jump_9.png'), pygame.image.load('jump_left/jump_10.png')]
enemyWorm = [pygame.image.load('worm_1/frame_1.png'), pygame.image.load('worm_1/frame_2.png'),
             pygame.image.load('worm_1/frame_3.png'), pygame.image.load('worm_1/frame_4.png'),
             pygame.image.load('worm_1/frame_5.png'), pygame.image.load('worm_1/frame_6.png'),
             pygame.image.load('worm_1/frame_7.png'), pygame.image.load('worm_1/frame_8.png'),
             pygame.image.load('worm_1/frame_9.png'), pygame.image.load('worm_1/frame_10.png')]

for i in range(10):
    playerJumpRight[i] = pygame.transform.scale(playerJumpRight[i], (100, 70))
    playerJumpLeft[i] = pygame.transform.scale(playerJumpLeft[i], (100, 70))
    playerRunLeft[i] = pygame.transform.scale(playerRunLeft[i], (100, 70))
    playerRunRight[i] = pygame.transform.scale(playerRunRight[i], (100, 70))
    playerStandRight[i] = pygame.transform.scale(playerStandRight[i], (100, 70))
    playerStandLeft[i] = pygame.transform.scale(playerStandLeft[i], (100, 70))
    playerWalkRight[i] = pygame.transform.scale(playerWalkRight[i], (100, 70))
    playerWalkLeft[i] = pygame.transform.scale(playerWalkLeft[i], (100, 70))
    playerBulletsRight[i] = pygame.transform.scale(playerBulletsRight[i], (40, 40))
    playerBulletsLeft[i] = pygame.transform.scale(playerBulletsLeft[i], (40, 40))
    enemyWorm[i] = pygame.transform.scale(enemyWorm[i], (50, 70))

clock = pygame.time.Clock()

timerSpawn = timer = animationCount = 0
weightPerson = 60
heightPerson = 70
speed = 3
speedY = 5
acceleration = -0.3
x = 800
y = 660 - heightPerson
bullets, worms = [], []

isQuit = isRun = isJump = left = isLeft = right = isDie = False  # initialization

while not isQuit:
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if timerSpawn == 100:
        if len(worms) < 5:
            worms.append(Worm())
        else:
            worms.pop(0)
            worms.append(Worm())
        timerSpawn = 0

    for bullet in bullets:
        if bullet.x > 1280 or bullet.x < -30:
            bullets.pop(bullets.index(bullet))
        else:
            if bullet.y < 585:
                bullet.y -= speedY * 3
            bullet.x += bullet.speed

    if keys[pygame.K_f]:
        if len(bullets) < 2 and timer > 10:
            timer = 0
            if isLeft:
                bullets.append(Bullet(x, y, -1, isLeft))
            else:
                bullets.append(Bullet(x, y, 1, isLeft))
    if keys[pygame.K_h]:
        isRun = True
        speed = 6
    else:
        isRun = False
        speed = 3

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > -weightPerson + 20:
        left = True
        right = False
        x -= speed
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < 1280 - weightPerson:
        left = False
        right = True
        x += speed
    else:
        left = False
        right = False

    if keys[pygame.K_SPACE]:
        isJump = True

    if isJump:
        y -= speedY * 3
        speedY += acceleration
        if y > 660 - heightPerson:
            speedY = 5
            y = 660 - heightPerson
            isJump = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            isQuit = True

    timerSpawn += 1
    timer += 1
    if isDie:
        y = 100
    draw_window()

pygame.quit()
