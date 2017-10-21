#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pygame
from pygame.locals import *

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

# Classes---------
class Landscape(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/landscape_el.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = display_width/2
        self.rect.centery = display_height/2
        self.speed = 0.5
        #steering wheel
        self.sw_angle = 0
        self.bounds = 0

    def mover(self, time, keys):
        if self.rect.left + 700 >= 0:
            if keys[K_RIGHT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right - 700 <= display_width:
            if keys[K_LEFT]:
                self.rect.centerx += self.speed * time

    #perturbation methods ******************
    #turn speed
    def set_speed(self, speed):
        self.speed = speed;
    #steering wheel angle and bounds
    def set_angle(self, angle, bounds):
        self.sw_angle  = angle
        self.bounds = bounds

# -----------
def main():
    #Initial settings
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Drunksi Driving Mode")
    pygame.display.set_mode((0,0),pygame.FULLSCREEN)


    #Sprites and images
    landscape = Landscape(30)    
    cockpit = pygame.image.load("images/cockpit.png").convert_alpha()
    swheel = pygame.image.load("images/s_wheel.png").convert_alpha()
    swheel_copy = swheel.copy()
    
    #Steering wheel initial settings
    angle = 0
    landscape.set_angle(3,120)

    running = True
    while running:
        keys = pygame.key.get_pressed()
        time = clock.tick(60)  
        #Quit or esc
        for eventos in pygame.event.get():
            if eventos.type == QUIT or keys[K_ESCAPE]:
                running = False
                sys.exit(0)
        
        landscape.mover(time,keys)

        #Steering wheel
        if keys[K_LEFT] and angle <landscape.bounds:
            angle += landscape.sw_angle
            swheel_copy = pygame.transform.rotate(swheel, angle)
        if keys[K_RIGHT] and angle >-landscape.bounds:
            angle -= landscape.sw_angle
            swheel_copy = pygame.transform.rotate(swheel,angle)

        #Show stuff
        swheel_rect = swheel_copy.get_rect()
        swheel_rect.center = (480,650)
        screen.blit(landscape.image,landscape.rect)
        screen.blit(cockpit, (0,0))
        screen.blit(swheel_copy, swheel_rect)
        pygame.display.flip()

pygame.quit()
if __name__ == '__main__':
    pygame.init()
    main()
