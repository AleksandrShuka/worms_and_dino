import pygame
import random
import time


def init_animations():
    animations = dict()

    animations['MenuBG'] = pygame.image.load('image/menu/background_menu.png')
    animations['background_lvl_1.png'] = pygame.image.load('image/background_lvl_1.png')

    animations['PlayButton'] = [pygame.image.load('image/menu/play.jpg'), pygame.image.load('image/menu/play1.jpg')]
    animations['SettingButton'] = [pygame.image.load('image/menu/settings.jpg'), pygame.image.load('image/menu/settings1.jpg')]
    animations['ExitButton'] = [pygame.image.load('image/menu/exit.jpg'), pygame.image.load('image/menu/exit1.jpg')]
    animations['MarkButton'] = [pygame.image.load('image/menu/znak.png'), pygame.image.load('image/menu/znak1.png')]

    animations['DeadRight'] = [pygame.image.load('image/dead_right/dead_1.png'), pygame.image.load('image/dead_right/dead_2.png'),
                               pygame.image.load('image/dead_right/dead_3.png'), pygame.image.load('image/dead_right/dead_4.png'),
                               pygame.image.load('image/dead_right/dead_5.png'), pygame.image.load('image/dead_right/dead_6.png'),
                               pygame.image.load('image/dead_right/dead_7.png'), pygame.image.load('image/dead_right/dead_8.png')]
    animations['BulletsRight'] = [pygame.image.load('image/bullet_right/bullet_1.png'),
                                  pygame.image.load('image/bullet_right/bullet_2.png'),
                                  pygame.image.load('image/bullet_right/bullet_3.png'),
                                  pygame.image.load('image/bullet_right/bullet_4.png'),
                                  pygame.image.load('image/bullet_right/bullet_5.png'),
                                  pygame.image.load('image/bullet_right/bullet_6.png'),
                                  pygame.image.load('image/bullet_right/bullet_7.png'),
                                  pygame.image.load('image/bullet_right/bullet_8.png'),
                                  pygame.image.load('image/bullet_right/bullet_9.png'),
                                  pygame.image.load('image/bullet_right/bullet_10.png')]
    animations['BulletsLeft'] = [pygame.image.load('image/bullet_left/bullet_1.png'),
                                 pygame.image.load('image/bullet_left/bullet_2.png'),
                                 pygame.image.load('image/bullet_left/bullet_3.png'),
                                 pygame.image.load('image/bullet_left/bullet_4.png'),
                                 pygame.image.load('image/bullet_left/bullet_5.png'),
                                 pygame.image.load('image/bullet_left/bullet_6.png'),
                                 pygame.image.load('image/bullet_left/bullet_7.png'),
                                 pygame.image.load('image/bullet_left/bullet_8.png'),
                                 pygame.image.load('image/bullet_left/bullet_9.png'),
                                 pygame.image.load('image/bullet_left/bullet_10.png')]
    animations['WalkRight'] = [pygame.image.load('image/walk_right/walk_1.png'), pygame.image.load('image/walk_right/walk_2.png'),
                               pygame.image.load('image/walk_right/walk_3.png'), pygame.image.load('image/walk_right/walk_4.png'),
                               pygame.image.load('image/walk_right/walk_5.png'), pygame.image.load('image/walk_right/walk_6.png'),
                               pygame.image.load('image/walk_right/walk_7.png'), pygame.image.load('image/walk_right/walk_8.png'),
                               pygame.image.load('image/walk_right/walk_9.png'), pygame.image.load('image/walk_right/walk_10.png')]
    animations['WalkLeft'] = [pygame.image.load('image/walk_left/walk_1.png'), pygame.image.load('image/walk_left/walk_2.png'),
                              pygame.image.load('image/walk_left/walk_3.png'), pygame.image.load('image/walk_left/walk_4.png'),
                              pygame.image.load('image/walk_left/walk_5.png'), pygame.image.load('image/walk_left/walk_6.png'),
                              pygame.image.load('image/walk_left/walk_7.png'), pygame.image.load('image/walk_left/walk_8.png'),
                              pygame.image.load('image/walk_left/walk_9.png'), pygame.image.load('image/walk_left/walk_10.png')]
    animations['StandRight'] = [pygame.image.load('image/idle_right/idle_1.png'), pygame.image.load('image/idle_right/idle_2.png'),
                                pygame.image.load('image/idle_right/idle_3.png'), pygame.image.load('image/idle_right/idle_4.png'),
                                pygame.image.load('image/idle_right/idle_5.png'), pygame.image.load('image/idle_right/idle_6.png'),
                                pygame.image.load('image/idle_right/idle_7.png'), pygame.image.load('image/idle_right/idle_8.png'),
                                pygame.image.load('image/idle_right/idle_9.png'), pygame.image.load('image/idle_right/idle_10.png')]
    animations['StandLeft'] = [pygame.image.load('image/idle_left/idle_1.png'), pygame.image.load('image/idle_left/idle_2.png'),
                               pygame.image.load('image/idle_left/idle_3.png'), pygame.image.load('image/idle_left/idle_4.png'),
                               pygame.image.load('image/idle_left/idle_5.png'), pygame.image.load('image/idle_left/idle_6.png'),
                               pygame.image.load('image/idle_left/idle_7.png'), pygame.image.load('image/idle_left/idle_8.png'),
                               pygame.image.load('image/idle_left/idle_9.png'), pygame.image.load('image/idle_left/idle_10.png')]
    animations['RunRight'] = [pygame.image.load('image/run_right/run_1.png'), pygame.image.load('image/run_right/run_2.png'),
                              pygame.image.load('image/run_right/run_3.png'), pygame.image.load('image/run_right/run_4.png'),
                              pygame.image.load('image/run_right/run_5.png'), pygame.image.load('image/run_right/run_6.png'),
                              pygame.image.load('image/run_right/run_7.png'), pygame.image.load('image/run_right/run_8.png'),
                              pygame.image.load('image/run_right/run_9.png'), pygame.image.load('image/run_right/run_10.png')]
    animations['RunLeft'] = [pygame.image.load('image/run_left/run_1.png'), pygame.image.load('image/run_left/run_2.png'),
                             pygame.image.load('image/run_left/run_3.png'), pygame.image.load('image/run_left/run_4.png'),
                             pygame.image.load('image/run_left/run_5.png'), pygame.image.load('image/run_left/run_6.png'),
                             pygame.image.load('image/run_left/run_7.png'), pygame.image.load('image/run_left/run_8.png'),
                             pygame.image.load('image/run_left/run_9.png'), pygame.image.load('image/run_left/run_10.png')]
    animations['JumpRight'] = [pygame.image.load('image/jump_right/jump_1.png'), pygame.image.load('image/jump_right/jump_2.png'),
                               pygame.image.load('image/jump_right/jump_3.png'), pygame.image.load('image/jump_right/jump_4.png'),
                               pygame.image.load('image/jump_right/jump_5.png'), pygame.image.load('image/jump_right/jump_6.png'),
                               pygame.image.load('image/jump_right/jump_7.png'), pygame.image.load('image/jump_right/jump_8.png'),
                               pygame.image.load('image/jump_right/jump_9.png'), pygame.image.load('image/jump_right/jump_10.png')]
    animations['JumpLeft'] = [pygame.image.load('image/jump_left/jump_1.png'), pygame.image.load('image/jump_left/jump_2.png'),
                              pygame.image.load('image/jump_left/jump_3.png'), pygame.image.load('image/jump_left/jump_4.png'),
                              pygame.image.load('image/jump_left/jump_5.png'), pygame.image.load('image/jump_left/jump_6.png'),
                              pygame.image.load('image/jump_left/jump_7.png'), pygame.image.load('image/jump_left/jump_8.png'),
                              pygame.image.load('image/jump_left/jump_9.png'), pygame.image.load('image/jump_left/jump_10.png')]
    animations['Worm_1'] = [pygame.image.load('image/worm_1/frame_1.png'), pygame.image.load('image/worm_1/frame_2.png'),
                            pygame.image.load('image/worm_1/frame_3.png'), pygame.image.load('image/worm_1/frame_4.png'),
                            pygame.image.load('image/worm_1/frame_5.png'), pygame.image.load('image/worm_1/frame_6.png'),
                            pygame.image.load('image/worm_1/frame_7.png'), pygame.image.load('image/worm_1/frame_8.png'),
                            pygame.image.load('image/worm_1/frame_9.png'), pygame.image.load('image/worm_1/frame_10.png')]

    for i in range(10):
        animations['JumpRight'][i] = pygame.transform.scale(animations['JumpRight'][i], (100, 70))
        animations['JumpLeft'][i] = pygame.transform.scale(animations['JumpLeft'][i], (100, 70))
        animations['RunLeft'][i] = pygame.transform.scale(animations['RunLeft'][i], (100, 70))
        animations['RunRight'][i] = pygame.transform.scale(animations['RunRight'][i], (100, 70))
        animations['StandRight'][i] = pygame.transform.scale(animations['StandRight'][i], (100, 70))
        animations['StandLeft'][i] = pygame.transform.scale(animations['StandLeft'][i], (100, 70))
        animations['WalkRight'][i] = pygame.transform.scale(animations['WalkRight'][i], (100, 70))
        animations['WalkLeft'][i] = pygame.transform.scale(animations['WalkLeft'][i], (100, 70))
        animations['BulletsRight'][i] = pygame.transform.scale(animations['BulletsRight'][i], (40, 40))
        animations['BulletsLeft'][i] = pygame.transform.scale(animations['BulletsLeft'][i], (40, 40))
        animations['Worm_1'][i] = pygame.transform.scale(animations['Worm_1'][i], (50, 70))
    for i in range(8):
        animations['DeadRight'][i] = pygame.transform.scale(animations['DeadRight'][i], (100, 70))
    for i in range(2):
        animations['MarkButton'][i] = pygame.transform.scale(animations['MarkButton'][i], (60, 60))
    animations['MenuBG'] = pygame.transform.scale(animations['MenuBG'], (1280, 720))

    animations['background_lvl_1.png'] = pygame.transform.scale(animations['background_lvl_1.png'], (1280, 720))

    return animations


def draw_window(window, bg, character, arr_bullets, arr_worms):
    window.blit(bg, (0, 0))
    window.blit(character.get_animation(), (character.x, character.y))
    for elem in arr_bullets:
        window.blit(elem.get_animation(), (elem.x, elem.y))
    for elem in arr_worms:
        window.blit(elem.get_animation(), (elem.x, elem.y))
    pygame.display.update()


def dino_logic(arr_keys, timer, arr):
    if arr_keys[pygame.K_j]:
        if len(arr) < 2 and timer > 10:
            timer = 0
            arr.append(Bullet(dino.x, dino.y, dino.facing_left))

    if arr_keys[pygame.K_h]:
        dino.run()
    else:
        dino.walk()

    if (arr_keys[pygame.K_a] or arr_keys[pygame.K_LEFT]) and dino.x > -dino.weight + 20:
        dino.facing_left = True
        dino.to_left()
        if not dino.isJump:
            if dino.isRun:
                dino.set_animation(animations['RunLeft'][count_animation // 3])
            else:
                dino.set_animation(animations['WalkLeft'][count_animation // 3])
    elif (arr_keys[pygame.K_d] or arr_keys[pygame.K_RIGHT]) and dino.x < 1280 - dino.weight:
        dino.facing_left = False
        dino.to_right()
        if not dino.isJump:
            if dino.isRun:
                dino.set_animation(animations['RunRight'][count_animation // 3])
            else:
                dino.set_animation(animations['WalkRight'][count_animation // 3])
    else:
        dino.staying()
        if dino.facing_left:
            if dino.x > 1240 - dino.weight:
                dino.x -= 10
            if not dino.isJump:
                dino.set_animation(animations['StandLeft'][count_animation // 3])
        else:
            if dino.x < 0:
                dino.x += 5
            if not dino.isJump:
                dino.set_animation(animations['StandRight'][count_animation // 3])

    if arr_keys[pygame.K_SPACE]:
        dino.isJump = True

    if dino.isJump:
        if dino.facing_left:
            dino.set_animation(animations['JumpLeft'][count_animation // 3])
        else:
            dino.set_animation(animations['JumpRight'][count_animation // 3])
        dino.jump()

    return arr, timer


def worms_logic(character, arr_worms, timer, animations_arr, count_animations):
    if timer == 100:
        if len(worms) < 10:
            arr_worms.append(Worm(character.x))
        else:
            arr_worms.pop(0)
            worms.append(Worm(character.x))
        timer = 0
    for elem in worms:
        elem.set_animation(animations_arr['Worm_1'][count_animations // 4])
        if ((elem.x < character.x and character.x - elem.x < 5) or (
                elem.x > character.x and elem.x - character.x < 50)) and (
            elem.y - character.y < 40):

            dino.isDie = True
        elif character.x < elem.x:
            elem.x -= elem.speed
        elif character.x > elem.x:
            elem.x += elem.speed

    return arr_worms, timer


def bullet_logic(arr_bullets, arr_worms, arr_animations, count_animations):
    for bullet in arr_bullets:
        if bullet.facing_left:
            bullet.set_animation(arr_animations['BulletsLeft'][count_animations // 3])
        else:
            bullet.set_animation(arr_animations['BulletsRight'][count_animations // 3])
        if bullet.x > 1280 or bullet.x < -30:
            bullets.pop(bullets.index(bullet))
        else:
            bullet.x += bullet.speed

    for worm in arr_worms:
        for elem in bullets:
            if abs(elem.x - worm.x) < 25 and worm.y - elem.y < 30:
                worms.pop(worms.index(worm))
                bullets.pop(bullets.index(elem))
    return arr_worms, arr_bullets


def menu(animation):
    keys_menu = pygame.key.get_pressed()
    flag_menu = 'MENU'

    win.blit(animation['MenuBG'], (0, 0))
    win.blit(animation['PlayButton'][0], (48, 35))
    win.blit(animation['SettingButton'][0], (35, 118))
    win.blit(animation['ExitButton'][0], (45, 201))
    win.blit(animation['MarkButton'][0], (1210, 650))

    for elem in pygame.event.get():
        if elem.type == pygame.QUIT or keys_menu[pygame.K_ESCAPE]:
            flag_menu = 'EXIT'
        if elem.type == pygame.MOUSEBUTTONDOWN:
            if abs(elem.pos[0] - 196.5) <= 148.5 and abs(elem.pos[1] - 74.5) <= 39:
                flag_menu = 'PLAY'
            elif abs(elem.pos[0] - 195) <= 160 and abs(elem.pos[1] - 156) <= 39:
                flag_menu = 'SETTINGS'
            elif abs(elem.pos[0] - 194) <= 149 and abs(elem.pos[1] - 239.5) <= 39:
                flag_menu = 'EXIT'
            elif abs(elem.pos[0] - 1240) < 30 and abs(elem.pos[1] - 680) <= 30:
                flag_menu = 'QUESTION'

    pos = pygame.mouse.get_pos()
    if abs(pos[0] - 196.5) <= 148.5 and abs(pos[1] - 74.5) <= 39:
        win.blit(animation['PlayButton'][1], (48, 35))
    elif abs(pos[0] - 195) <= 160 and abs(pos[1] - 156) <= 39:
        win.blit(animation['SettingButton'][1], (35, 118))
    elif abs(pos[0] - 194) <= 149 and abs(pos[1] - 239.5) <= 39:
        win.blit(animation['ExitButton'][1], (45, 201))
    elif abs(pos[0] - 1240) < 30 and abs(pos[1] - 680) <= 30:
        win.blit(animation['MarkButton'][1], (1210, 650))

    pygame.display.update()

    return flag_menu


class Dino:
    def __init__(self):
        self.height = 70
        self.weight = 60
        self.x = 300
        self.y = 590
        self.speedX = 5
        self.speedY = 7
        self.__animation = []
        self.facing_left = False
        self.left = False
        self.right = False
        self.isJump = False
        self.isRun = False
        self.isDie = False

    def set_animation(self, animation):
        if len(self.__animation) > 1:
            self.__animation.clear()
        self.__animation.append(animation)

    def get_animation(self):
        return self.__animation[0]

    def to_right(self):
        self.x += self.speedX
        self.left = False
        self.right = True

    def to_left(self):
        self.x -= self.speedX
        self.left = True
        self.right = False

    def run(self):
        self.speedX = 7
        self.isRun = True

    def walk(self):
        self.speedX = 3
        self.isRun = False

    def staying(self):
        self.isRun = False
        self.left = False
        self.right = False

    def jump(self):
        self.y -= self.speedY * 3
        self.speedY -= 0.5
        if self.y > 660 - self.height:
            self.speedY = 7
            self.y = 660 - self.height
            self.isJump = False


class Bullet:
    def __init__(self, x, y, facing_left):
        self.facing_left = facing_left
        self.x = x + 20
        self.y = y + 10
        if facing_left:
            self.speed = -11
        else:
            self.speed = 11
        self.__animation = []

    def set_animation(self, animation):
        if len(self.__animation) > 1:
            self.__animation.clear()
        self.__animation.append(animation)

    def get_animation(self):
        return self.__animation[0]


class Worm:
    def __init__(self, x):
        self.__animation = []
        self.speed = random.randrange(1, 4)
        self.x = random.randrange(0, 1230)
        while abs(self.x - x) < 50:
            self.x = random.randrange(0, 1230)
        self.y = 590

    def set_animation(self, animation):
        if len(self.__animation) > 1:
            self.__animation.clear()
        self.__animation.append(animation)

    def get_animation(self):
        return self.__animation[0]


pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dino Adventure")
animations = init_animations()
dino = Dino()
timerSpawn = timerShoot = count_animation = flagDie = score = die_animation_count = 0
bullets, worms = [], []
clock = pygame.time.Clock()
endGame = False
flag = 'MENU'

while not endGame:
    clock.tick(60)
    if flag == 'MENU':
        bullets, worms = [], []
        dino = Dino()
        timerSpawn = timerShoot = count_animation = flagDie = score = die_animation_count = 0
        flag = menu(animations)
    elif flag == 'PLAY':
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                endGame = True

        if count_animation == 30:
            count_animation = 0

        if not dino.isDie:
            worms, timerSpawn = worms_logic(dino, worms, timerSpawn, animations, count_animation)
            bullets, timerShoot = dino_logic(keys, timerShoot, bullets)
            worms, bullets = bullet_logic(bullets, worms, animations, count_animation)
        else:
            dino.set_animation(animations['DeadRight'][die_animation_count // 3])
            if len(worms) > 0:
                worms.pop()
            die_animation_count += 1
            if die_animation_count > 23:
                flag = 'MENU'

        draw_window(win, animations['background_lvl_1.png'], dino, bullets, worms)

        timerShoot += 1
        timerSpawn += 1
        count_animation += 1
    elif flag == 'EXIT':
        endGame = True

pygame.quit()
