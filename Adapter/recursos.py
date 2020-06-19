import pygame
import random
from pygame.locals import *

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    
    def actualizar(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        self.img = img
        self.x = x
        self.y = y
        self.rect = self.img.get_rect()
        self.rect.left,self.rect.top=(x,y)
    
    def actualizar(self,pantalla):
        pantalla.blit(self.img,self.rect)