from cmath import cos
from logging import PlaceHolder
from tkinter import NONE


import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.angle = angle
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bullet.png"), (15,10)), angle)
        self.rect = self.image.get_rect(topleft = (x ,y))
        self.speed = 10

    def update(self, screen):
        x_movement = 10 *  math.cos( math.radians(self.angle))
        y_movement = 10 * - math.sin(math.radians(self.angle))
        self.rect.x += x_movement
        self.rect.y += y_movement
        screen.blit(self.image, self.rect)
