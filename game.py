import os
import sys
import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

surface = pygame.Surface(screen.get_size())
surface.convert()

filename = os.path.join('resources', 'ballon_1.png')


object_rect = pygame.Rect(0,0, 100, 100)

ballon_1 = pygame.image.load(filename)
ballon_1.convert()

ballon_1_fit_rect = ballon_1.get_rect().fit(object_rect)
print(ballon_1_fit_rect.size)


step = 3
dir = 1
x = 0

while True:
    x += step*dir
    if x >= surface.get_rect().width - ballon_1_fit_rect.width:
        dir = -1
    elif x <= 0:
        dir = 1 
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((255, 255, 255))
    screen.blit(surface, (0,0))
    screen.blit(pygame.transform.smoothscale(ballon_1, ballon_1_fit_rect.size), (x,100))
    pygame.display.flip()
    pygame.display.update()