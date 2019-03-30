import os
import sys
import pygame
from pygame.locals import *
from game_objects import HotAirBalloon

pygame.init()
pygame.font.init() # Initaliserer fonter

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE) 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
surface = pygame.Surface(screen.get_size())
surface.convert()

balloons = []
for n in range(1):
    balloons.append(HotAirBalloon(surface))


while True:
    pygame.event.pump()
    for event in pygame.event.get():
        # Avslutter ved Window X eller Q tast
        if (event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_q)):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_PLUS: # + Oppretter en ny ballong
                balloons.append(HotAirBalloon(surface))
            elif event.key == K_UP:
                for ballon in balloons:
                    ballon.speed += 1
            elif event.key == K_DOWN:
                for ballon in balloons:
                    ballon.speed -= 1
            elif event.key == K_LEFT:
                for ballon in balloons:
                    ballon.direction -= 1
            elif event.key == K_RIGHT:
                for ballon in balloons:
                    ballon.direction += 1
        

            
    surface.fill((255, 255, 255))
    for balloon in balloons:
        balloon.draw()
    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.display.update()