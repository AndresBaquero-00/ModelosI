from fabricas import *
from player import *

class Director():
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getHeroe(self):
        jugador = Personaje()
        jugador.set_sprites(self.__builder.get_sprites())
        return jugador


class Constructor():
    def get_sprites(self): 
        pass

class ConstructorZombis():
    def __init__(self):
        self.fabrica = FabricaZombis()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda()]

