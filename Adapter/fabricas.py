from productos import *

class FabricaAbstracta():
    def crear_derecha(self): pass
    def crear_izquierda(self): pass

class FabricaZombis(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaZombi()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaZombi()
        return derecha.get_sprites()
