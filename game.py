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
print(filename)
ballon_1 = pygame.image.load(filename)
ballon_1.convert()

while True:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((255, 255, 255))
    screen.blit(surface, (0,0))
    screen.blit(ballon_1, (0,0))

    pygame.display.flip()
    pygame.display.update()