import random
import pygame
import pygame_menu
import sys
from player import Player
from cloud import Cloud

keepGameRunning = True

def playGame():
    keepGameRunning = True  
    player_1 = Player('plane1.png', 20,100)
    player_2 = Player('plane2.png', 20,400)
    BG_COLOR = pygame.Color(153, 217, 234)
    clock = pygame.time.Clock()
    cloud_group = pygame.sprite.Group()
    for i in range(5):
        cloud_group.add(Cloud(random.randint(0,840), random.randint(0,640)))
    while keepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGameRunning = False
        
        pressed_keys = pygame.key.get_pressed()
        if player_1.health > 0:
            if pressed_keys[pygame.K_w]:
                player_1.move_up()
            if pressed_keys[pygame.K_a]:
                player_1.move_left()
            if pressed_keys[pygame.K_s]:
                player_1.move_down()
            if pressed_keys[pygame.K_d]:
                player_1.move_right()
            if pressed_keys[pygame.K_e]:
                player_1.rotate(-5)
            if pressed_keys[pygame.K_q]:
                player_1.rotate(5)
            if pressed_keys[pygame.K_LSHIFT]:
                player_1.shoot()
        else:
            pygame.display.set_caption('Player 2 Wins!')
            
        if player_2.health > 0:
            if pressed_keys[pygame.K_i]:
                player_2.move_up()
            if pressed_keys[pygame.K_j]:
                player_2.move_left()
            if pressed_keys[pygame.K_k]:
                player_2.move_down()
            if pressed_keys[pygame.K_l]:
                player_2.move_right()
            if pressed_keys[pygame.K_o]:
                player_2.rotate(-5)
            if pressed_keys[pygame.K_u]:
                player_2.rotate(5)
            if pressed_keys[pygame.K_RSHIFT]:
                player_2.shoot()
        
        if not player_2.health and not player_1.health:
            pygame.display.set_caption('Crash!')
        elif not player_2.health:
            pygame.display.set_caption('Player 1 Wins!')
            menu.mainloop(screen)
        elif not player_1.health:
            pygame.display.set_caption('Player 2 Wins!')
        if player_2.rect.y > 640 or player_1.rect.y > 640:
            menu.mainloop(screen)
        screen.fill(BG_COLOR)
        player_1.update(screen, player_2)
        player_2.update(screen, player_1)
        for cloud in cloud_group:
            if cloud.rect.x < 0:
                cloud.kill()
                cloud_group.add(Cloud(850, random.randint(0,640)))
            cloud.update(screen)
        pygame.display.flip()
        clock.tick(60) 

pygame.init()
screen = pygame.display.set_mode((840, 640))
pygame.display.set_caption('Welcome to DogFight')
screen.fill((153, 217, 234))
menu = pygame_menu.Menu('DogFight', 840, 640,
                       theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', playGame)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
#playGame(screen=screen)
