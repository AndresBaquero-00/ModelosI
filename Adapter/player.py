import pygame
from pygame.sprite import Sprite
from pygame import *

class Personaje(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.cont = 0
        self.state = 0
    
    def set_sprites(self, sprites):
        self.sprites = sprites
        self.image = self.sprites[self.state][self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 50)


    def CDerecha(self):
        self.state = 0
        self.rect.x += 5
        self.image = self.animar_state(self.sprites[self.state])

    def CIzquierda(self):
        self.state = 1
        self.rect.x -= 5
        self.image = self.animar_state(self.sprites[self.state])

    def dibujar(self, ventana):
        ventana.blit(self.image, self.rect)

    def animar_state(self, state):
        self.cont += 1
        if self.cont > (len(state) - 1):
            self.cont = 0
        return state[self.cont]
        

        
            


