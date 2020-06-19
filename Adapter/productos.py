import pygame

class Derechas():
    def get_sprites(self): 
        pass

class DerechaZombi(Derechas):
    def get_sprites(self): 
        return [pygame.image.load('Img/spritesZ/ZCD1.png'),
                pygame.image.load('Img/spritesZ/ZCD2.png'),
                pygame.image.load('Img/spritesZ/ZCD3.png'),
                pygame.image.load('Img/spritesZ/ZCD4.png'),
                pygame.image.load('Img/spritesZ/ZCD5.png'),
                pygame.image.load('Img/spritesZ/ZCD6.png'),
                pygame.image.load('Img/spritesZ/ZCD7.png'),
                pygame.image.load('Img/spritesZ/ZCD8.png')]


class Izquierdas():
    def get_sprites(self): 
        pass

class IzquierdaZombi(Izquierdas):
    def get_sprites(self): 
        return [pygame.image.load('Img/spritesZ/ZCI1.png'),
                pygame.image.load('Img/spritesZ/ZCI2.png'),
                pygame.image.load('Img/spritesZ/ZCI3.png'),
                pygame.image.load('Img/spritesZ/ZCI4.png'),
                pygame.image.load('Img/spritesZ/ZCI5.png'),
                pygame.image.load('Img/spritesZ/ZCI6.png'),
                pygame.image.load('Img/spritesZ/ZCI7.png'),
                pygame.image.load('Img/spritesZ/ZCI8.png')]

