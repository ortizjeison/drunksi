#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pygame
from pygame.locals import *
 
img_path = 'images'
display_width = 1200
display_height = 710

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

# Clases
# ---------------------------------------------------------------------
class Landscape(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/landscape_el.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = display_width/2
        self.rect.centery = display_height/2
        self.speed = 0.5

    def mover(self, time, keys):
        if self.rect.left + 700 >= 0:
            if keys[K_RIGHT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right - 700 <= display_width:
            if keys[K_LEFT]:
                self.rect.centerx += self.speed * time

    #métodos para perturbar ******************
    def set_speed(self, speed):
        self.speed = speed;


class Swheel(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/s_wheel.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 480
        self.rect.centery = 650
        self.speed = 0.5

    def rotar(self, time, keys):
        if keys[K_RIGHT]:
            #img_temp = rot_center(self.image,-1)
            self.image = rot_center(self.image,-1)
            print('tecla derecha')
        if keys[K_LEFT]:
            #img_temp = rot_center(self.image,1)
            self.image = rot_center(self.image,1)
            print('tecla izquierda')

    #métodos para perturbar ******************
    def set_speed(self, speed):
        self.speed = speed;

#Rotar IMG
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
 
# ---------------------------------------------------------------------
def main():
    clock = pygame.time.Clock()
    #Window building
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Drunksi Driving Mode")
    #background_image = load_image('images/white_back.png')

    #Loading sprites and images
    landscape = Landscape(30)
    swheel = Swheel(30)
    cockpit = pygame.image.load("images/cockpit.png").convert_alpha()
    pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    #Big bucle
    finish = False
    while not finish:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        #Quit
        for eventos in pygame.event.get():
            if eventos.type == QUIT or keys[K_ESCAPE]:
                finish = True
                sys.exit(0)                


        landscape.mover(time,keys)
        screen.blit(landscape.image,landscape.rect)
        screen.blit(cockpit, (0,0))
        screen.blit(swheel.image,swheel.rect)
        pygame.display.update()

pygame.quit()
if __name__ == '__main__':
    pygame.init()
    main()