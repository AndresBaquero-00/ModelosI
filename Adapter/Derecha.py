import pygame
from pygame.locals import *

class Derecha():
    __derecha = list(range(10))
<<<<<<< HEAD
    
=======
>>>>>>> 20bfc67f3d171166613c7c64f445f53d16462ed6
    def getDerecha(self):
        for i in range(10):
            self.__derecha[i] = pygame.image.load("Ninja/Derecha/Run__00"+str(i)+".png")
        return self.__derecha
