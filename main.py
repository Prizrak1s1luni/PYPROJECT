import pygame
import random

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618, 359))     # flags=pygame.NOFRAME
pygame.display.set_caption("Mi Game")
icon = pygame.image.load('images/icon.1.png').convert_alpha()
pygame.display.set_icon(icon)
ghost_iventys = random.uniform(1500, 1700)

forest = pygame.image.load('images/forest.png').convert_alpha()
walk_left = [
    pygame.image.load('images/player left/1.png').convert_alpha(),
    pygame.image.load('images/player left/2.png').convert_alpha(),
    pygame.image.load('images/player left/3.png').convert_alpha(),
    pygame.image.load('images/player left/4.png').convert_alpha(),
]
walk_right = [
    pygame.image.load('images/player right/1.png').convert_alpha(),
    pygame.image.load('images/player right/2.png').convert_alpha(),
    pygame.image.load('images/player right/3.png').convert_alpha(),
    pygame.image.load('images/player right/4.png').convert_alpha(),
]

ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list_in_game =[]

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 250

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
#bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 1500)

label = pygame.font.Font('fonts/ofont.ru_Cornerita.ttf', 40)
lose_label = label.render('Вы проиграли!', False, (88, 232, 205))
restart_label = label.render('Начать заново', False, (88, 232, 205))
restart_label_rect = restart_label.get_rect(topleft=(180, 200))

gameplay = True

running = True
while running:



    screen.blit(forest, (bg_x, 0))
    screen.blit(forest, (bg_x + 618, 0))

    if gameplay:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost,el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < 575:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 7

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -618:
            bg_x = 0
    else:
        screen.fill((74, 13, 99))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620, 260)))
    clock.tick(15)
