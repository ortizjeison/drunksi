#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes

display_width = 1200
display_height = 710
white = (255,255,255)

#pintar todo de (white)
#gameDisplay.fill(white)

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
# -----------
 
# Funciones
# ------------
    #default para cargar imágenes
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
# ---------------------------------------------------------------------
def main():
    clock = pygame.time.Clock()
    #Window building
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Drunksi Driving Mode")
    background_image = load_image('images/white_back.png')

    #Loading sprites and images
    landscape = Landscape(30)
    cockpit = pygame.image.load("images/cockpit.png").convert_alpha()
    Swheel = pygame.image.load("images/s_wheel.png").convert_alpha()
    
    #Big bucle
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                finish = True;
            print(event)
        #pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #Setting tick(fps)
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        landscape.mover(time,keys)
        screen.blit(background_image, (0,0))
        screen.blit(landscape.image,landscape.rect)
        screen.blit(cockpit, (-50,0))
        screen.blit(Swheel,(300,500))
        #Refresh changes in window
        pygame.display.update()
pygame.quit()

if __name__ == '__main__':
    pygame.init()
    main()