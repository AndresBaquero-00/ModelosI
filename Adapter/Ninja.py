from Derecha import *
from Izquierda import *
from Quieto import *
import Personaje

class Ninja(Personaje):
    __derecha = None
    __izquierda = None
    __quieto = None
    
    def set_derecha(self):
        der = Derecha()
        self.__derecha = der.getDerecha()

    def set_izquierda(self):
        izq = Izquierda()
        self.__derecha = izq.getIzquierda()

    def set_quieto(self):
        qui = Quieto()
        self.__quieto = qui.getQuieto()

    def get_derecha(self):
        return self.__derecha

    def get_izquierda(self):
        return self.__izquierda

    def get_quieto(self):
        return self.__quieto
        
    
