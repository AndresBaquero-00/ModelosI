import pygame
<<<<<<< HEAD
from Personaje import *

personaje = Zombie()

derecha = personaje.get_derecha()
izquierda = personaje.get_izquierda()
quieto = personaje.get_quieto()

matriz = []

=======
from Derecha import *
from Izquierda import *
from Quieto import *
from pygame.locals import *

der = Derecha()
izq = Izquierda()
qui = Quieto()

derecha = der.getDerecha()
izquierda = izq.getIzquierda()
quieto = qui.getQuieto()

matriz = []

#Inicializar la matriz de inecuaciones
>>>>>>> 20bfc67f3d171166613c7c64f445f53d16462ed6
for i in range(3):
    matriz.append([])
    for j in range(10):
        matriz[i].append(None)

<<<<<<< HEAD
for j in range(len(quieto)):
    matriz[0][j] = quieto[j]

for j in range(len(derecha)):
    matriz[1][j] = derecha[j]

for j in range(len(izquierda)):
=======
for j in range(10):
    matriz[0][j] = quieto[j]

for j in range(10):
    matriz[1][j] = derecha[j]

for j in range(10):
>>>>>>> 20bfc67f3d171166613c7c64f445f53d16462ed6
    matriz[2][j] = izquierda[j]

frame = 0
indice = 0
<<<<<<< HEAD
lon = len(quieto)
=======
>>>>>>> 20bfc67f3d171166613c7c64f445f53d16462ed6

pygame.init()
 
pantalla = pygame.display.set_mode((720,320),0,32)
x = 360
y = 100

<<<<<<< HEAD
def cargar(indice, lon):
    global frame, x, y
    frame = (frame+1) % lon;
=======
def cargar(indice):
    global frame, x, y
    frame = (frame+1) % 10;
>>>>>>> 20bfc67f3d171166613c7c64f445f53d16462ed6
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
<<<<<<< HEAD
            lon = len(izquierda)
        elif pulsada[K_d]:
            indice = 1
            x += 5
            lon = len(derecha)
        else:
            lon = len(quieto)
=======
        elif pulsada[K_d]:
            indice = 1
            x += 5
        else:
>>>>>>> 20bfc67f3d171166613c7c64f445f53d16462ed6
            indice = 0
        
    reloj.tick(25)
    pantalla.fill((255,255,255))
<<<<<<< HEAD
    cargar(indice, lon)
=======
    cargar(indice)
>>>>>>> 20bfc67f3d171166613c7c64f445f53d16462ed6
    pygame.display.update()
