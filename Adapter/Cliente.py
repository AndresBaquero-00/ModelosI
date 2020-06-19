import pygame
from Personaje import *

personaje = Ninja()

derecha = personaje.get_derecha()
izquierda = personaje.get_izquierda()
quieto = personaje.get_quieto()


matriz = []


for i in range(3):
    matriz.append([])
    for j in range(10):
        matriz[i].append(None)

for j in range(len(quieto)):
    matriz[0][j] = quieto[j]

for j in range(len(derecha)):
    matriz[1][j] = derecha[j]

for j in range(len(izquierda)):
    matriz[2][j] = izquierda[j]

frame = 0
indice = 0
lon = len(quieto)

pygame.init()
 
pantalla = pygame.display.set_mode((720,320),0,32)
x = 360
y = 100

def cargar(indice, lon):
    global frame, x, y
    frame = (frame+1) % lon;
    pantalla.blit(matriz[indice][frame], (x, y));
     
reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pulsada = pygame.key.get_pressed()
 
    if(pygame.key.get_pressed()):
        if pulsada[K_a]:
            x -= 5
            indice = 2
            lon = len(izquierda)
        elif pulsada[K_d]:
            indice = 1
            x += 5
            lon = len(derecha)
        else:
            lon = len(quieto)
            indice = 0
        
    reloj.tick(25)
    pantalla.fill((255,255,255))
    cargar(indice, lon)
    pygame.display.update()
