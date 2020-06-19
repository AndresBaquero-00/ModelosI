import pygame
from pygame.locals import *

class Quieto():
    __quieto = list(range(10))
    def getQuieto(self):
        for i in range(10):
            self.__quieto[i] = pygame.image.load("Ninja/Quieto/Idle__00"+str(i)+".png")
        return self.__quieto
