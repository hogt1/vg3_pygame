import os
import sys
import random
import pygame
import math
from pygame.locals import *

DEBUG = True
RESOURCE_DIR = 'resources'
HOTAIR_BALLON_FILE = 'ballon_1.png'
HOTAIR_BALLON_FILE_2 = 'ballon_2.png'

HOTAIR_BALLON_SIZE = (100,100)

CANNONBALL_FILE = 'cannonball.png'
CANNONBALL_SIZE = (20, 20)


class HotAirBalloon:
    def __init__(self,surface):
        self.surface = surface
        self.MIN_SPEED = 3
        self.MAX_SPEED = 10
        filename = os.path.join(RESOURCE_DIR, HOTAIR_BALLON_FILE)
        self.image_desc = load_image(filename, HOTAIR_BALLON_SIZE)
        filename = os.path.join(RESOURCE_DIR, HOTAIR_BALLON_FILE_2)
        self.image_asc = load_image(filename, HOTAIR_BALLON_SIZE)

        self.image = self.image_desc
        self.rect = self.image.get_rect()

        self.speed = random.randint(self.MIN_SPEED,self.MAX_SPEED)
        # Starter i tilfeldig retning
        self.direction = random.randint(-180, 180)

        # Tilfeldig posisjon
        #x = random.randint(0, self.surface.get_rect().width - self.rect.width)
        #y = random.randint(0, self.surface.get_rect().height - self.rect.height)
        
        # Starter på midten av skjermen
        self.rect.left = (self.surface.get_rect().width / 2) - (self.rect.width / 2)
        self.rect.top = self.surface.get_rect().height / 2 - (self.rect.height / 2)
    
    def update(self):
        # Python operere med radianer og ikke grader
        rad = math.radians(self.direction)

        # Regner ut x og y komponenten fra vektoren "speed*direction"
        x = math.cos(rad) * self.speed
        y = math.sin(rad) * self.speed

        # Regner ut ny posisjon
        self.rect.left += x
        self.rect.top  += y
        if y >= 0:
            self.image = self.image_desc
        else:
            self.image = self.image_asc

        hit = False
        # Sjekker om vi går over topp eller bunn    
        if (self.rect.bottom >= self.surface.get_rect().bottom) or (self.rect.top <= 0):
            # Reverserer y om vi er utenfor elle på topp/bunn
            y *= -1
            hit = True

        # Sjekker om vi går over høyre eller venstre kant
        if (self.rect.right >= self.surface.get_rect().right) or (self.rect.left <= 0):
            # Reverserer x om vi er utenfor elle på topp/bunn
            x *= -1
            hit = True
        
        if hit:
            # Kalkulerer direction ut i fra x og y. atan2 håndterer fortegn
            rad = math.atan2(y/self.speed, x/self.speed) # Vinkel i radianer
            self.direction = math.degrees(rad) # Kalkulerer om radianer til grader
            # Random justering direction
            self.direction += random.randint(-5, 5)

    def draw(self):
        self.update()
        self.surface.blit(self.image, self.rect.topleft)
        if DEBUG:
            self.surface.blit(
                debug_text('{:.0f}° {}'.format(self.direction, self.speed)),
                (self.rect.left,self.rect.top-20))


class Cannonball:
    def __init__(self,surface):
        self.surface = surface
        filename = os.path.join(RESOURCE_DIR, CANNONBALL_FILE)
        self.image = load_image(filename, CANNONBALL_SIZE)
        self.rect = self.image.get_rect()
        self.speed = 5
        
        # Starter random på toppen utenfor skjermen
        self.rect.left = random.randint(0, self.surface.get_rect().width - self.rect.width)
        self.rect.top = -self.rect.height
    
    def update(self):
        self.rect.top += self.speed
        # Sjekker om vi går over topp eller bunn    
        if (self.rect.top > self.surface.get_rect().bottom):
            self.rect.left = random.randint(0, self.surface.get_rect().width - self.rect.width)
            self.rect.top = -self.rect.height

    def draw(self):
        self.update()
        self.surface.blit(self.image, self.rect.topleft)

    
def debug_text(text):
    font = pygame.font.SysFont('', 20)
    # font.render returnerer et surface
    return font.render(text, False, (0, 0, 0))


def load_image(filename, size = (100, 100)):
    ''' Returnerer en surface med det skalerte bilde
    '''
    img = pygame.image.load(filename)
    img.convert()
    # Skalerer størrelsen på bilde til det som  passer best innenfor målet
    rect =  img.get_rect().fit(pygame.Rect((0, 0), size))
    # Lager en surface med samme størrelse som ønsket bilde (Likk mikk for at den skal bli transparent)
    image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
    image = image.convert_alpha()
    # Tegner skalert bilde på Surface
    image.blit(pygame.transform.smoothscale(img, rect.size), (0,0))
    return image



