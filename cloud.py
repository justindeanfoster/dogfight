import pygame
import random


class Cloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("cloud.png")
        self.rect = self.image.get_rect(center=(x,y))
        self.velocity = random.randint(1,4)


    def update(self, screen):
        self.rect.x -= self.velocity
        screen.blit(self.image, self.rect)