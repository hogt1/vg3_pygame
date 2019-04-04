import os
import sys
import random
import pygame
from pygame.locals import *
import settings
from sprites import HotAirBalloon

pygame.init()
pygame.font.init() # Initaliserer fonter
clock = pygame.time.Clock()



#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE) 
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)) 
surface = pygame.Surface(screen.get_size())
surface.convert()

balloons = []
for n in range(10):
    speed = random.randint(settings.HOTAIR_BALLON_MIN_SPEED,settings.HOTAIR_BALLON_MAX_SPEED)
    # Starter i tilfeldig retning
    direction = random.randint(-180, 180)
    balloons.append(HotAirBalloon(speed, direction))


while True:
    pygame.event.pump()
    for event in pygame.event.get():
        # Avslutter ved Window X eller Q tast
        if (event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_q)):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_p: # + Oppretter en ny ballong
                speed = random.randint(settings.HOTAIR_BALLON_MIN_SPEED,settings.HOTAIR_BALLON_MAX_SPEED)
                # Starter i tilfeldig retning
                direction = random.randint(-180, 180)
                balloons.append(HotAirBalloon(speed, direction))
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
        balloon.draw(surface)
    screen.blit(surface, (0,0))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(settings.FPS)