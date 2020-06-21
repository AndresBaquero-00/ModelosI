import pygame
from tkinter import *
from Personaje import *

personaje = None
per=None
frame = 0
indice = 0
x = 360
y = 100
raiz=Tk()
raiz.title("Interface Ninja - Zombie")
fram=Frame()
fram.pack()
fram.config(width="300", height="150", bd=7, relief="groove", cursor="hand2")

def clien(personaje):
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

    lon = len(quieto)

    pygame.init()
     
    pantalla = pygame.display.set_mode((720,320),0,32)
    global x
    global y

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

def codbotn():
    nin=Ninja()
    clien(nin)

def codbotz():
    zom=Zombie()
    clien(zom)
    
botn=Button(fram, text="Ninja", command=codbotn)
botn.place(x=50, y=50)
botz=Button(fram, text="Zombie", command=codbotz)
botz.place(x=175, y=50)

raiz.mainloop()


