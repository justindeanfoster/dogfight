import pygame
from bullet import Bullet
import math
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_group = pygame.sprite.Group()
        self.image = pygame.transform.scale(pygame.image.load(file_image), (100, 50))
        self.display_image = self.image
        #self.x, self.y = x,y
        self.angle = 0
        self.rect = self.image.get_rect(topleft=(x,y))
        self.health = 100
        self.shoot_timer = 0
        self.crash = False
        

    def shoot(self):
        if self.shoot_timer == 0:
            self.shoot_timer = 10
            self.bullet_group.add(Bullet(self.angle, self.rect.centerx, self.rect.centery))


    def rotate(self, degree):
        self.angle += degree
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center = self.rect.center)
        self.rect = new_rect
        self.display_image = rotated_image

    def move_up(self):
        if  640 > self.rect.top > 0:
            self.rect.y -= 5
        
    def move_down(self):
        if  640 > self.rect.bottom :
            self.rect.y  += 5
        
    def move_left(self):
        if  self.rect.left > 0:
            self.rect.x -= 5
        
    def move_right(self):
        if 820 > self.rect.right:
            self.rect.x += 5
        
    
    def damage(self, damage):
        self.health -= damage
        
    
    def healthbar(self, screen):
        pygame.draw.rect(screen, pygame.Color(255, 0, 0),pygame.Rect((self.rect.bottomleft), (70,5)))
        pygame.draw.rect(screen, pygame.Color(0, 255, 0),pygame.Rect((self.rect.bottomleft), (math.floor((self.health / 100) * 70),5)))


    def update(self, screen, opposing_player):
        #self.rect.topleft = (self.x, self.y)
        if self.shoot_timer != 0:
            self.shoot_timer -= 1
        if self.rect.colliderect(opposing_player.rect):
            self.health = 0
            self.crash = True
            opposing_player.crash = True
        if self.health <= 0 or self.crash:
            self.display_image = pygame.transform.scale(pygame.image.load("plane2_explode.png"), (100, 50))
            self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
            self.rect.y += 10
            if self.rect.y > 650:
                self.kill()
            
        for bullet in self.bullet_group:
            bullet.update(screen)
            if bullet.rect.colliderect(opposing_player.rect):
                opposing_player.damage(10)
                bullet.kill()
        screen.blit(self.display_image, self.rect)
        self.healthbar(screen)
        
        