import os
import sys
import random
import pygame
from pygame.locals import *

class HotAirBalloon:
    def __init__(self, screen, surface):
        self.screen = screen
        self.surface = surface
        filename = os.path.join('resources', 'ballon_1.png')
        self.image = pygame.image.load(filename)
        self.image.convert()
        self.speed = 3
        self.direction = 1
        self.rect =  self.image.get_rect().fit(pygame.Rect(0,0,100,100))
        x = random.randint(0, self.surface.get_rect().width - self.rect.width)
        y = random.randint(0, self.surface.get_rect().height - self.rect.height)
        self.rect.left = x
        self.rect.top = y
    
    def update(self):
        self.rect.left += self.speed * self.direction
        if self.rect.left >= self.surface.get_rect().width - self.rect.width:
            self.direction = -1
        elif self.rect.left <= 0:
            self.direction = 1

    def draw(self):
        self.update()
        self.screen.blit(pygame.transform.smoothscale(self.image, self.rect.size), self.rect.topleft)
    


#balloon_1 = HotAirBalloon(screen)


