import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola Mundo")

Mi_imagen = pygame.image.load("imagenes/wolf.png")
posX, posY = randint(10,300), randint(10,200)
ventana.blit(Mi_imagen, (posX, posY))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()