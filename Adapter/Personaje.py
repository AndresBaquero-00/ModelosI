import Constructores

from Derecha import *
from Izquierda import *
from Quieto import *
from fabricas import *
from player import *
from Constructores import *

class Personajes:
    __derecha = None
    __izquierda = None
    __quieto = None
    
    def get_derecha(self):
        pass

    def get_izquierda(self):
        pass

    def get_quieto(self):
        pass


class Ninja(Personajes):
    __derecha = None
    __izquierda = None
    __quieto = None

    def __init__(self):
        der = Derecha()
        self.__derecha = der.getDerecha()
        
        izq = Izquierda()
        self.__izquierda = izq.getIzquierda()

        qui = Quieto()
        self.__quieto = qui.getQuieto()

    def get_derecha(self):
        return self.__derecha

    def get_izquierda(self):
        return self.__izquierda

    def get_quieto(self):
        return self.__quieto

class Zombie(Personajes, ConstructorZombis):
    __derecha = None
    __izquierda = None
    __quieto = None

    def __init__(self):

        super(Zombie, self).__init__()
        sprites = super(Zombie, self).get_sprites()
        
        self.__derecha = sprites[0]

        self.__izquierda = sprites[1]

        self.__quieto = [pygame.image.load('Img/spritesZ/ZCD1.png')]

    def get_derecha(self):
        return self.__derecha

    def get_izquierda(self):
        return self.__izquierda

    def get_quieto(self):
        return self.__quieto


    
        
    
