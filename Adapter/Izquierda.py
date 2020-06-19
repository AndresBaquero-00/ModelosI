import pygame
from pygame.locals import *

class Izquierda():
    __izquierda = list(range(10))
    def getIzquierda(self):
        for i in range(10):
            self.__izquierda[i] = pygame.image.load("Ninja/Izquierda/Run__00"+str(i)+".png")
        return self.__izquierda
