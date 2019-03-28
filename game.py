import sys
import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

surface = pygame.Surface(screen.get_size())
surface.convert()


while True:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((255, 255, 255))
    screen.blit(surface, (0,0))

    #pygame.display.flip()
    pygame.display.update()