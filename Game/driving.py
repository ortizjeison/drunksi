#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pygame
from pygame.locals import *
#change pc
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
    def __init__(self):
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

class Button(pygame.sprite.Sprite):
    def __init__(self,static,over,x,y):
        self.image_static=static
        self.image_over=over
        self.image_current=self.image_static
        self.rect=self.image_current.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,screen,cursor):
        if cursor.colliderect(self.rect):
            self.image_current=self.image_over
        else: self.image_current=self.image_static
        
        screen.blit(self.image_current,self.rect)

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

# -----------
def main():
    #Initial settings
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Drunksi Driving Mode")
    pygame.display.set_mode((0,0),pygame.FULLSCREEN)

    #Sprites and images
    landscape = Landscape()    
    cockpit = pygame.image.load("images/cockpit.png").convert_alpha()
    swheel = pygame.image.load("images/s_wheel.png").convert_alpha()
    intro  = pygame.image.load("images/load.png").convert_alpha();
    swheel_copy = swheel.copy()
    
    #Steering wheel initial settings
    angle = 0
    landscape.set_angle(3,120)

    #intro
    import time
    screen.blit(intro,(0,0))
    pygame.display.flip()
    time.sleep(2)

    white = (0,0,0)
    screen.fill(white)


######################### Menu ################################
    #Menu Backgound
    menu  = pygame.image.load("images/menu.png").convert_alpha();
    screen.blit(menu,(0,0))
    pygame.display.flip()

    running = False

    #imagenes botones
    plays=pygame.image.load("images/buttons/play_s.png")
    playo=pygame.image.load("images/buttons/play_o.png")
    exits=pygame.image.load("images/buttons/exit_s.png")
    exito=pygame.image.load("images/buttons/exit_o.png") 
    
    play=Button(plays,playo,480,300)
    exit=Button(exits,exito,480,400)
    cursor1=Cursor()

    #Menu while
    while running ==False :
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(play.rect):
                    running = True
                if cursor1.colliderect(exit.rect):
                    sys.exit(0)

            if event.type == QUIT or keys[K_ESCAPE]:
                running = True
                sys.exit(0)

        time = clock.tick(60)
        cursor1.update()
        play.update(screen,cursor1)
        exit.update(screen,cursor1)
        pygame.display.flip()

    #Game while
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
