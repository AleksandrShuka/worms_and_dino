import pygame
import random
import time


def init_animations():
    animations = dict()
    animations['Bonus'] = pygame.image.load('image/bonus.png')
    animations['Live'] = pygame.image.load('image/live.png')
    animations['MenuBG'] = pygame.image.load('image/menu/background_menu.png')
    animations['background_lvl_1.png'] = pygame.image.load('image/background_lvl_1.png')
    animations['Died'] = pygame.image.load('image/died.png')

    animations['PlayButton'] = [pygame.image.load('image/menu/play.jpg'), pygame.image.load('image/menu/play1.jpg')]
    animations['SettingButton'] = [pygame.image.load('image/menu/settings.jpg'),
                                   pygame.image.load('image/menu/settings1.jpg')]
    animations['ExitButton'] = [pygame.image.load('image/menu/exit.jpg'), pygame.image.load('image/menu/exit1.jpg')]
    animations['MarkButton'] = [pygame.image.load('image/menu/znak.png'), pygame.image.load('image/menu/znak1.png')]

    animations['Blood'] = pygame.image.load('image/blood.png')
    animations['Blood'] = pygame.transform.scale(animations['Blood'], (1280, 720))

    animations['Platform'] = [pygame.image.load('image/platforms_lvl_1/platform_1.png'),
                              pygame.image.load('image/platforms_lvl_1/platform_2.png'),
                              pygame.image.load('image/platforms_lvl_1/platform_3.png')]
    animations['Platform'][0] = pygame.transform.scale(animations['Platform'][0], (1280, 50))
    animations['Platform'][1] = pygame.transform.scale(animations['Platform'][1], (230, 50))
    animations['Platform'][2] = pygame.transform.scale(animations['Platform'][2], (230, 50))


    animations['Worm_2_left'] = [pygame.image.load('image/worm_2_left/frame_1.png'), pygame.image.load('image/worm_2_left/frame_2.png'),
                                pygame.image.load('image/worm_2_left/frame_3.png'), pygame.image.load('image/worm_2_left/frame_4.png'),
                                pygame.image.load('image/worm_2_left/frame_5.png'), pygame.image.load('image/worm_2_left/frame_6.png'),
                                pygame.image.load('image/worm_2_left/frame_7.png'), pygame.image.load('image/worm_2_left/frame_8.png'),
                                pygame.image.load('image/worm_2_left/frame_9.png'), pygame.image.load('image/worm_2_left/frame_10.png')]
    animations['Worm_2_right'] = [pygame.image.load('image/worm_2_right/frame_1.png'), pygame.image.load('image/worm_2_right/frame_2.png'),
                                pygame.image.load('image/worm_2_right/frame_3.png'), pygame.image.load('image/worm_2_right/frame_4.png'),
                                pygame.image.load('image/worm_2_right/frame_5.png'), pygame.image.load('image/worm_2_right/frame_6.png'),
                                pygame.image.load('image/worm_2_right/frame_7.png'), pygame.image.load('image/worm_2_right/frame_8.png'),
                                pygame.image.load('image/worm_2_right/frame_9.png'), pygame.image.load('image/worm_2_right/frame_10.png')]
    animations['Bullets2Right'] = [pygame.image.load('image/bullets_2_right/frame_1.png'),
                                   pygame.image.load('image/bullets_2_right/frame_2.png'),
                                   pygame.image.load('image/bullets_2_right/frame_3.png'),
                                   pygame.image.load('image/bullets_2_right/frame_4.png'),
                                   pygame.image.load('image/bullets_2_right/frame_5.png'),
                                   pygame.image.load('image/bullets_2_right/frame_6.png'),
                                   pygame.image.load('image/bullets_2_right/frame_7.png'),
                                   pygame.image.load('image/bullets_2_right/frame_8.png'),
                                   pygame.image.load('image/bullets_2_right/frame_9.png'),
                                   pygame.image.load('image/bullets_2_right/frame_10.png')]
    animations['Bullets2Left'] = [pygame.image.load('image/bullets_2_left/frame_1.png'),
                                  pygame.image.load('image/bullets_2_left/frame_2.png'),
                                  pygame.image.load('image/bullets_2_left/frame_3.png'),
                                  pygame.image.load('image/bullets_2_left/frame_4.png'),
                                  pygame.image.load('image/bullets_2_left/frame_5.png'),
                                  pygame.image.load('image/bullets_2_left/frame_6.png'),
                                  pygame.image.load('image/bullets_2_left/frame_7.png'),
                                  pygame.image.load('image/bullets_2_left/frame_8.png'),
                                  pygame.image.load('image/bullets_2_left/frame_9.png'),
                                  pygame.image.load('image/bullets_2_left/frame_10.png')]
    animations['DeadLeft'] = [pygame.image.load('image/dead_left/dead_1.png'),
                              pygame.image.load('image/dead_left/dead_2.png'),
                              pygame.image.load('image/dead_left/dead_3.png'),
                              pygame.image.load('image/dead_left/dead_4.png'),
                              pygame.image.load('image/dead_left/dead_5.png'),
                              pygame.image.load('image/dead_left/dead_6.png'),
                              pygame.image.load('image/dead_left/dead_7.png'),
                              pygame.image.load('image/dead_left/dead_8.png')]
    animations['DeadRight'] = [pygame.image.load('image/dead_right/dead_1.png'),
                               pygame.image.load('image/dead_right/dead_2.png'),
                               pygame.image.load('image/dead_right/dead_3.png'),
                               pygame.image.load('image/dead_right/dead_4.png'),
                               pygame.image.load('image/dead_right/dead_5.png'),
                               pygame.image.load('image/dead_right/dead_6.png'),
                               pygame.image.load('image/dead_right/dead_7.png'),
                               pygame.image.load('image/dead_right/dead_8.png')]
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
    animations['WalkRight'] = [pygame.image.load('image/walk_right/walk_1.png'),
                               pygame.image.load('image/walk_right/walk_2.png'),
                               pygame.image.load('image/walk_right/walk_3.png'),
                               pygame.image.load('image/walk_right/walk_4.png'),
                               pygame.image.load('image/walk_right/walk_5.png'),
                               pygame.image.load('image/walk_right/walk_6.png'),
                               pygame.image.load('image/walk_right/walk_7.png'),
                               pygame.image.load('image/walk_right/walk_8.png'),
                               pygame.image.load('image/walk_right/walk_9.png'),
                               pygame.image.load('image/walk_right/walk_10.png')]
    animations['WalkLeft'] = [pygame.image.load('image/walk_left/walk_1.png'),
                              pygame.image.load('image/walk_left/walk_2.png'),
                              pygame.image.load('image/walk_left/walk_3.png'),
                              pygame.image.load('image/walk_left/walk_4.png'),
                              pygame.image.load('image/walk_left/walk_5.png'),
                              pygame.image.load('image/walk_left/walk_6.png'),
                              pygame.image.load('image/walk_left/walk_7.png'),
                              pygame.image.load('image/walk_left/walk_8.png'),
                              pygame.image.load('image/walk_left/walk_9.png'),
                              pygame.image.load('image/walk_left/walk_10.png')]
    animations['StandRight'] = [pygame.image.load('image/idle_right/idle_1.png'),
                                pygame.image.load('image/idle_right/idle_2.png'),
                                pygame.image.load('image/idle_right/idle_3.png'),
                                pygame.image.load('image/idle_right/idle_4.png'),
                                pygame.image.load('image/idle_right/idle_5.png'),
                                pygame.image.load('image/idle_right/idle_6.png'),
                                pygame.image.load('image/idle_right/idle_7.png'),
                                pygame.image.load('image/idle_right/idle_8.png'),
                                pygame.image.load('image/idle_right/idle_9.png'),
                                pygame.image.load('image/idle_right/idle_10.png')]
    animations['StandLeft'] = [pygame.image.load('image/idle_left/idle_1.png'),
                               pygame.image.load('image/idle_left/idle_2.png'),
                               pygame.image.load('image/idle_left/idle_3.png'),
                               pygame.image.load('image/idle_left/idle_4.png'),
                               pygame.image.load('image/idle_left/idle_5.png'),
                               pygame.image.load('image/idle_left/idle_6.png'),
                               pygame.image.load('image/idle_left/idle_7.png'),
                               pygame.image.load('image/idle_left/idle_8.png'),
                               pygame.image.load('image/idle_left/idle_9.png'),
                               pygame.image.load('image/idle_left/idle_10.png')]
    animations['RunRight'] = [pygame.image.load('image/run_right/run_1.png'),
                              pygame.image.load('image/run_right/run_2.png'),
                              pygame.image.load('image/run_right/run_3.png'),
                              pygame.image.load('image/run_right/run_4.png'),
                              pygame.image.load('image/run_right/run_5.png'),
                              pygame.image.load('image/run_right/run_6.png'),
                              pygame.image.load('image/run_right/run_7.png'),
                              pygame.image.load('image/run_right/run_8.png'),
                              pygame.image.load('image/run_right/run_9.png'),
                              pygame.image.load('image/run_right/run_10.png')]
    animations['RunLeft'] = [pygame.image.load('image/run_left/run_1.png'),
                             pygame.image.load('image/run_left/run_2.png'),
                             pygame.image.load('image/run_left/run_3.png'),
                             pygame.image.load('image/run_left/run_4.png'),
                             pygame.image.load('image/run_left/run_5.png'),
                             pygame.image.load('image/run_left/run_6.png'),
                             pygame.image.load('image/run_left/run_7.png'),
                             pygame.image.load('image/run_left/run_8.png'),
                             pygame.image.load('image/run_left/run_9.png'),
                             pygame.image.load('image/run_left/run_10.png')]
    animations['JumpRight'] = [pygame.image.load('image/jump_right/jump_1.png'),
                               pygame.image.load('image/jump_right/jump_2.png'),
                               pygame.image.load('image/jump_right/jump_3.png'),
                               pygame.image.load('image/jump_right/jump_4.png'),
                               pygame.image.load('image/jump_right/jump_5.png'),
                               pygame.image.load('image/jump_right/jump_6.png'),
                               pygame.image.load('image/jump_right/jump_7.png'),
                               pygame.image.load('image/jump_right/jump_8.png'),
                               pygame.image.load('image/jump_right/jump_9.png'),
                               pygame.image.load('image/jump_right/jump_10.png')]
    animations['JumpLeft'] = [pygame.image.load('image/jump_left/jump_1.png'),
                              pygame.image.load('image/jump_left/jump_2.png'),
                              pygame.image.load('image/jump_left/jump_3.png'),
                              pygame.image.load('image/jump_left/jump_4.png'),
                              pygame.image.load('image/jump_left/jump_5.png'),
                              pygame.image.load('image/jump_left/jump_6.png'),
                              pygame.image.load('image/jump_left/jump_7.png'),
                              pygame.image.load('image/jump_left/jump_8.png'),
                              pygame.image.load('image/jump_left/jump_9.png'),
                              pygame.image.load('image/jump_left/jump_10.png')]
    animations['Worm_1_left'] = [pygame.image.load('image/worm_1_left/frame_1.png'),
                                 pygame.image.load('image/worm_1_left/frame_2.png'),
                                 pygame.image.load('image/worm_1_left/frame_3.png'),
                                 pygame.image.load('image/worm_1_left/frame_4.png'),
                                 pygame.image.load('image/worm_1_left/frame_5.png'),
                                 pygame.image.load('image/worm_1_left/frame_6.png'),
                                 pygame.image.load('image/worm_1_left/frame_7.png'),
                                 pygame.image.load('image/worm_1_left/frame_8.png'),
                                 pygame.image.load('image/worm_1_left/frame_9.png'),
                                 pygame.image.load('image/worm_1_left/frame_10.png')]
    animations['Worm_1_right'] = [pygame.image.load('image/worm_1_right/frame_1.png'),
                                  pygame.image.load('image/worm_1_right/frame_2.png'),
                                  pygame.image.load('image/worm_1_right/frame_3.png'),
                                  pygame.image.load('image/worm_1_right/frame_4.png'),
                                  pygame.image.load('image/worm_1_right/frame_5.png'),
                                  pygame.image.load('image/worm_1_right/frame_6.png'),
                                  pygame.image.load('image/worm_1_right/frame_7.png'),
                                  pygame.image.load('image/worm_1_right/frame_8.png'),
                                  pygame.image.load('image/worm_1_right/frame_9.png'),
                                  pygame.image.load('image/worm_1_right/frame_10.png')]

    for i in range(10):
        animations['Worm_2_right'][i] =  pygame.transform.scale(animations['Worm_2_right'][i], (50, 70))
        animations['Worm_2_left'][i] = pygame.transform.scale(animations['Worm_2_left'][i], (50, 70))
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
        animations['Worm_1_left'][i] = pygame.transform.scale(animations['Worm_1_left'][i], (50, 70))
        animations['Worm_1_right'][i] = pygame.transform.scale(animations['Worm_1_right'][i], (50, 70))
        animations['Bullets2Right'][i] = pygame.transform.scale(animations['Bullets2Right'][i], (40, 40))
        animations['Bullets2Left'][i] = pygame.transform.scale(animations['Bullets2Left'][i], (40, 40))
    for i in range(8):
        animations['DeadRight'][i] = pygame.transform.scale(animations['DeadRight'][i], (100, 70))
        animations['DeadLeft'][i] = pygame.transform.scale(animations['DeadLeft'][i], (100, 70))
    for i in range(2):
        animations['MarkButton'][i] = pygame.transform.scale(animations['MarkButton'][i], (60, 60))
    animations['MenuBG'] = pygame.transform.scale(animations['MenuBG'], (1280, 720))

    animations['background_lvl_1.png'] = pygame.transform.scale(animations['background_lvl_1.png'], (1280, 720))

    return animations


def draw_window(window, animation, character, arr_bullets, arr_worms, score_kills, arr_platforms, f_bonus):
    window.blit(animation['background_lvl_1.png'], (0, 0))
    for elem in arr_platforms[1:]:
        if elem.isBe:
            window.blit(elem.image, (elem.x, elem.y))
    window.blit(character.get_animation(), (character.x, character.y))
    for elem in arr_bullets:
        window.blit(elem.get_animation(), (elem.x, elem.y))
    for elem in arr_worms:
        window.blit(elem.get_animation(), (elem.x, elem.y))
    if dino.isHurt:
        window.blit(animations['Blood'], (0, 0))
    if f_bonus.isBe:
        window.blit(f_bonus.image, (f_bonus.x, f_bonus.y))
    for i in range(dino.lives):
        window.blit(dino.live_image, dino.arr_lives[i])
    win.blit(score_kills, (530, 40))
    pygame.draw.rect(window, (0, 0, 0), (1000, 45, 150, 25), 3)
    pygame.draw.rect(window, (150, 255, 40), (1148 - dino.run_fuel / 2, 47, dino.run_fuel / 2, 21))
    pygame.display.update()


def bonus_logic(elem, character):
    if abs(elem.x - character.x) < 30 and abs(elem.y - character.y) < 30 and elem.isBe:
        elem.isBe = False
        character.Bonus = True
        character.run_fuel = 146 * 2
        character.lives = 3
    if not elem.isBe:
        elem.timerBonus -= 1
        elem.timerSpawn -= 1
    if not elem.timerBonus:
        character.Bonus = False
        elem.timerBonus = 500
    if not elem.timerSpawn:
        elem.isBe = True
        elem.timerSpawn = 3000
    return elem, character





def logic_platform(arr_plat):
    for elem in arr_plat[1:]:
        if elem.DinoOnPlatform:
            platforms[platforms.index(elem)].timer += 1
        else:
            platforms[platforms.index(elem)].timer = 0

        if elem.timer == 40:
            platforms[platforms.index(elem)].isBe = False

        if not elem.isBe:
            platforms[platforms.index(elem)].timerSpawn += 1

        if elem.timerSpawn == 100:
            platforms[platforms.index(elem)].isBe = True
            platforms[platforms.index(elem)].timerSpawn = 0


def dino_logic(arr_keys, timer, arr, platform):
    if arr_keys[pygame.K_j]:
        if timer > 8:
            timer = 0
            if dino.run_fuel > 11 and dino.Bonus:
                dino.run_fuel -= 11
                arr.append(Bullet2(dino.x, dino.y, dino.facing_left))
            elif dino.run_fuel > 21 and not dino.Bonus:
                dino.run_fuel -= 21
                arr.append(Bullet(dino.x, dino.y, dino.facing_left))

    if arr_keys[pygame.K_h]:
        if dino.run_fuel > 1:
            dino.run_fuel -= 1
        if dino.run_fuel > 2:
            dino.run()
        else:
            dino.walk()
    else:
        dino.walk()

    if (arr_keys[pygame.K_a] or arr_keys[pygame.K_LEFT]) and dino.x > -dino.weight + 20:
        if not dino.facing_left:
            dino.x -= 30
            dino.facing_left = True
        dino.to_left()
        if not dino.isJump:
            if dino.isRun:
                dino.set_animation(animations['RunLeft'][count_animation // 2])
            else:
                dino.set_animation(animations['WalkLeft'][count_animation // 2])
    elif (arr_keys[pygame.K_d] or arr_keys[pygame.K_RIGHT]) and dino.x < 1280 - dino.weight:
        if dino.facing_left:
            dino.x += 30
            dino.facing_left = False
        dino.to_right()
        if not dino.isJump:
            if dino.isRun:
                dino.set_animation(animations['RunRight'][count_animation // 2])
            else:
                dino.set_animation(animations['WalkRight'][count_animation // 2])
    else:
        dino.staying()
        if dino.facing_left:
            if dino.x > 1240 - dino.weight:
                dino.x -= 10
            if not dino.isJump:
                dino.set_animation(animations['StandLeft'][count_animation // 2])
        else:
            if dino.x < 0:
                dino.x += 5
            if not dino.isJump:
                dino.set_animation(animations['StandRight'][count_animation // 2])

    if dino.facing_left:
        dino.x_foot = dino.x + 21
    else:
        dino.x_foot = dino.x - 12

    if arr_keys[pygame.K_SPACE] and not dino.down and dino.run_fuel >= 11:
        dino.run_fuel -= 10
        dino.isJump = True

    dino.gravity(platform)

    if dino.run_fuel < 146 * 2:
        dino.run_fuel += 0.5

    return arr, timer


def worms_logic(character, arr_worms, timer, arr_animations, count_animations):
    global speedSpawn
    spawn = random.randrange(1, 10)
    if timer > speedSpawn:
        if speedSpawn > 10:
            speedSpawn -= 0.1
        if len(arr_worms) < 100:
            if spawn > 7:
                arr_worms.append(Worm2(character.x))
            else:
                arr_worms.append(Worm(character.x))
        else:
            arr_worms.pop(0)
            if spawn > 7:
                arr_worms.append(Worm2(character.x))
            else:
                arr_worms.append(Worm(character.x))
        timer = 0
    for elem in arr_worms:
        if ((elem.x < character.x and character.x - elem.x < 5) or (
                elem.x > character.x and elem.x - character.x < 50)) and (
                elem.y - character.y < 40):
            dino.lives -= 1
            dino.isHurt = True
            arr_worms.pop(arr_worms.index(elem))
            if not dino.lives:
                dino.isDie = True
        elif character.x < elem.x:
            if elem.lvl == 1:
                elem.set_animation(arr_animations['Worm_1_left'][count_animations // 2])
            else:
                elem.set_animation(arr_animations['Worm_2_left'][count_animations // 2])
            elem.x -= elem.speed
        elif character.x > elem.x:
            if elem.lvl == 1:
                elem.set_animation(arr_animations['Worm_1_right'][count_animations // 2])
            else:
                elem.set_animation(arr_animations['Worm_2_right'][count_animations // 2])
            elem.x += elem.speed

    return arr_worms, timer


def bullet_logic(arr_bullets, arr_worms, arr_animations, count_animations):
    for bullet in arr_bullets:
        if bullet.facing_left:
            if bullet.lvl == 1:
                bullet.set_animation(arr_animations['BulletsLeft'][count_animations // 2])
            else:
                bullet.set_animation(arr_animations['Bullets2Left'][count_animations // 2])
        else:
            if bullet.lvl == 1:
                bullet.set_animation(arr_animations['BulletsRight'][count_animations // 2])
            else:
                bullet.set_animation(arr_animations['Bullets2Right'][count_animations // 2])

        if bullet.x > 1280 or bullet.x < -30:
            arr_bullets.pop(arr_bullets.index(bullet))
        else:
            bullet.x += bullet.speed

    for worm in arr_worms:
        for elem in arr_bullets:
            if abs(elem.x - worm.x) < 25 and worm.y - elem.y < 30:
                if elem.lvl == 2:
                    worm.lives -= 3
                else:
                    worm.lives -= 1
                arr_bullets.pop(arr_bullets.index(elem))
                if worm.lives <= 0:
                    arr_worms.pop(arr_worms.index(worm))
                    dino.score += 1
                    dino.run_fuel += 5
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


class Bonus:
    def __init__(self, x, y, image):
        self.isBe = True
        self.timerBonus = 500
        self.timerSpawn = 3000
        self.x = x
        self.y = y
        self.image = image


class Dino:
    def __init__(self, image):
        self.Bonus = False
        self.isHurt = False
        self.run_fuel = 146 * 2
        self.live_image = image
        self.arr_lives = [(20, 35), (60, 35), (100, 35)]
        self.lives = 3
        self.score = 0
        self.height = 70
        self.weight = 60
        self.x = 1150
        self.y = 300
        self.x_foot = self.x - 10
        self.speedX = 3
        self.speedY = 15
        self.__animation = []
        self.facing_left = False
        self.left = False
        self.right = False
        self.isJump = False
        self.isRun = False
        self.isDie = False
        self.down = True

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
        if self.Bonus:
            self.speedX = 11
        else:
            self.speedX = 7
        self.isRun = True

    def walk(self):
        self.speedX = 3
        self.isRun = False

    def staying(self):
        self.isRun = False
        self.left = False
        self.right = False

    def gravity(self, arr_platforms):
        self.down = True
        for platform in arr_platforms:
            if platform.isBe and not self.isJump and abs(platform.y - platform.height - self.y - 5) < 18 and abs(
                    self.x_foot + 45 - platform.x - platform.weight / 2) <= platform.weight / 2:
                platforms[arr_platforms.index(platform)].DinoOnPlatform = True
                self.y = platform.y - platform.height
                self.speedY = 13
                self.down = False
            else:
                platforms[arr_platforms.index(platform)].DinoOnPlatform = False

        if self.isJump:
            if dino.facing_left:
                dino.set_animation(animations['JumpLeft'][count_animation // 2])
            else:
                dino.set_animation(animations['JumpRight'][count_animation // 2])
            self.y -= self.speedY
            self.speedY -= 0.7
            if abs(self.speedY) < 0.3:
                self.down = True
                self.isJump = False
                self.speedY = 13
        elif self.down:
            if dino.facing_left:
                dino.set_animation(animations['JumpLeft'][count_animation // 2])
            else:
                dino.set_animation(animations['JumpRight'][count_animation // 2])
            self.y += (self.speedY - 12)
            if self.speedY < 35:
                self.speedY += 1


class Bullet:
    def __init__(self, x, y, facing_left):
        self.lvl = 1
        self.damage = 1
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


class Bullet2(Bullet):
    def __init__(self, x, y, facing_left):
        Bullet.__init__(self, x, y, facing_left)
        self.lvl = 2
        self.damage = 3


class Platform:
    def __init__(self, x, y, image, weight, height):
        self.timerSpawn = 0
        self.DinoOnPlatform = False
        self.isBe = True
        self.timer = 0
        self.x = x
        self.y = y
        self.image = image
        self.weight = weight
        self.height = height


class Worm:
    def __init__(self, x):
        self.lvl = 1
        self.lives = 2
        self.time_spawn = 100
        self.__animation = []
        self.speed = random.randrange(2, 5)
        self.x = random.randrange(-150, 1400)
        while abs(self.x - x) < 100:
            self.x = random.randrange(-150, 1400)
        self.y = 590

    def set_animation(self, animation):
        if len(self.__animation) > 1:
            self.__animation.clear()
        self.__animation.append(animation)

    def get_animation(self):
        return self.__animation[0]


class Worm2(Worm):
    def __init__(self, x):
        Worm.__init__(self, x)
        self.lvl = 2
        self.lives = 3


pygame.init()
speedSpawn = 100
font = pygame.font.Font(None, 50)
text_score = font.render('Score: 0', True, (255, 255, 255))
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dino Adventure")
animations = init_animations()
dino = Dino(animations['Live'])
timerSpawn = timerShoot = count_animation = flagDie = score = die_animation_count = timerHurt = 0
bullets, worms = [], []
bonus = Bonus(1200, 120, animations['Bonus'])
clock = pygame.time.Clock()
endGame = False
flag = 'MENU'
platforms = [Platform(0, 645, animations['Platform'][0], 1280, 50),
             Platform(1040, 520, animations['Platform'][2], 230, 50),
             Platform(750, 450, animations['Platform'][1], 230, 50),
             Platform(520, 450, animations['Platform'][1], 230, 50),
             Platform(1020, 160, animations['Platform'][1], 230, 50),
             Platform(900, 260, animations['Platform'][2], 230, 50),
             Platform(340, 350, animations['Platform'][1], 230, 50),
             Platform(190, 540, animations['Platform'][2], 230, 50),
             Platform(130, 240, animations['Platform'][2], 230, 50),
             Platform(374, 110, animations['Platform'][1], 230, 50)]

while not endGame:
    clock.tick(30)
    if flag == 'MENU':
        speedSpawn = 100
        bullets, worms = [], []
        dino = Dino(animations['Live'])
        timerSpawn = timerShoot = count_animation = flagDie = score = die_animation_count = 0
        flag = menu(animations)
    elif flag == 'PLAY':
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                endGame = True

        if count_animation == 20:
            count_animation = 0

        if not dino.isDie:
            worms, timerSpawn = worms_logic(dino, worms, timerSpawn, animations, count_animation)
            logic_platform(platforms)
            bullets, timerShoot = dino_logic(keys, timerShoot, bullets, platforms)
            worms, bullets = bullet_logic(bullets, worms, animations, count_animation)
            bonus, dino = bonus_logic(bonus, dino)
            text_score = font.render('Score: ' + str(dino.score), True, (255, 255, 255))
            if timerHurt > 20:
                timerHurt = 0
                dino.isHurt = False
            if dino.isHurt:
                timerHurt += 1
        else:
            if dino.facing_left:
                dino.set_animation(animations['DeadLeft'][die_animation_count // 3])
            else:
                dino.set_animation(animations['DeadRight'][die_animation_count // 3])
            if len(worms) > 0:
                worms.pop()
            die_animation_count += 1
            if die_animation_count > 23:
                win.blit(animations['Died'], (460, 300))
                pygame.display.update()
                time.sleep(3)
                flag = 'MENU'
        draw_window(win, animations, dino, bullets, worms, text_score, platforms, bonus)

        timerShoot += 1
        timerSpawn += 1
        count_animation += 1
    elif flag == 'EXIT':
        endGame = True

pygame.quit()
