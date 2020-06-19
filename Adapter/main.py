import pygame
import random
import player
from pygame.locals import *
import recursos 
from constuctores import *

class main():
    pygame.init()
    ventana = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Ventana Principal")
    clock = pygame.time.Clock()
    clock = pygame.time.Clock()
    cursor1 = recursos.Cursor()
    imgFondo = pygame.image.load("Img/FondoP.png").convert()
    img1 = pygame.image.load("Img/spritesZ/ZCD2.png")
    botonZ = recursos.Boton(img1,158,450)

    jugando = False
    ejecutando = True

    director = Director()

    while ejecutando == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botonZ.rect):
                    director.setBuilder(ConstructorZombis())
                    jugando = True
                player = director.getHeroe()
            if event.type == pygame.QUIT:
                ejecutando = False
            
        if jugando:
            pygame.mouse.set_visible(False)
            ventana.blit(imgFondo, [0, 0])
            player.dibujar(ventana)
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    player.CIzquierda()
                if event.key == K_RIGHT:
                    player.CDerecha()
            clock.tick(25)

        else:
            ventana.blit(imgFondo,[0,0])
            cursor1.actualizar()
            botonZ.actualizar(ventana)

        pygame.display.flip()

    pygame.quit ()


if __name__ == "__main__":
    main()

