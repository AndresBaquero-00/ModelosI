import pygame
from pygame.locals import *

class Derecha():
    __derecha = list(range(10))

    def getDerecha(self):
        for i in range(10):
            self.__derecha[i] = pygame.image.load("Ninja/Derecha/Run__00"+str(i)+".png")
        return self.__derecha
