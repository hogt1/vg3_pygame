import os
import sys
import pygame
from pygame.locals import *
from game_objects import HotAirBalloon

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

surface = pygame.Surface(screen.get_size())
surface.convert()

balloons = []
for n in range(10):
    balloons.append(HotAirBalloon(screen, surface))


while True:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((255, 255, 255))
    screen.blit(surface, (0,0))
    for balloon in balloons:
        balloon.draw()
    pygame.display.flip()
    pygame.display.update()