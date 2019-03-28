import os
import sys
import random
import pygame
import math
from pygame.locals import *

class HotAirBalloon:
    def __init__(self, screen, surface):
        self.screen = screen
        self.surface = surface
        self.MIN_SPEED = 5
        self.MAX_SPEED = 5
        filename = os.path.join('resources', 'ballon_1.png')
        self.image = pygame.image.load(filename)
        self.image.convert()
        self.speed = random.randint(self.MIN_SPEED,self.MAX_SPEED)
        self.direction = 135
        self.rect =  self.image.get_rect().fit(pygame.Rect(0,0,100,100))
        x = random.randint(0, self.surface.get_rect().width - self.rect.width)
        y = random.randint(0, self.surface.get_rect().height - self.rect.height)
        x = self.surface.get_rect().width / 2
        y = self.surface.get_rect().height / 2
        self.rect.left = x
        self.rect.top = y
    
    def update(self):
        self.rect.left += (self.speed*1000 * math.cos(math.radians(self.direction))) // 1000
        self.rect.top  += (self.speed*1000 * math.sin(math.radians(self.direction))) // 1000

        if self.rect.bottom >= self.surface.get_rect().height:
            self.direction *= -1
        elif self.rect.top <= 0:
            self.direction *= -1

        '''
        if self.rect.left >= self.surface.get_rect().width - self.rect.width:
            self.direction = -1
            self.speed = random.randint(self.MIN_SPEED,self.MAX_SPEED)
            self.speed += 1
        elif self.rect.left <= 0:
            self.direction = 1
            self.speed = random.randint(self.MIN_SPEED,self.MAX_SPEED)
        '''

    def draw(self):
        self.update()
        self.screen.blit(pygame.transform.smoothscale(self.image, self.rect.size), self.rect.topleft)
    


#balloon_1 = HotAirBalloon(screen)


