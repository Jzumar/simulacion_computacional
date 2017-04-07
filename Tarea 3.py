import pygame,random
from math import sqrt

from pygame.locals import *

numpart = 5
particulas= list()
pegadas = list()
pygame.init()
screen = pygame.display.set_mode((800,400))
clock=pygame.time.Clock()
r = 20
sepx = list()
sepy = list()
mov = [666,666]


x = 0
y = 1

for k in range(numpart):
    partcord = [random.randint(000,400),random.randint(0,400)]
    particulas.append(partcord)
    sepx.append(partcord[0])
    sepy.append(partcord[1])


fuera= False
while not fuera:
    for event in pygame.event.get():
        if event.type == QUIT:
            fuera = True
            break
    screen.fill((0,0,255))


    #PARTICULAS
   #posicion
    salga= False
    for i in range(len(particulas)):
        for j in range(len(partcord)):
            salga= False
            partcord = particulas[i]
            if partcord[j] > 0 & partcord[j] < 400:
                partcord[j] = partcord[j] + (random.randint(-1,1)*20)
            if partcord[j] < 0:
                partcord[j] = partcord[j] + 20
            if partcord[j] > 400:
                partcord[j] = partcord[j] -20
                
            sepx[i]=partcord[x]
            sepy[i]=partcord[y]
        
        
  
    
    salga=False
    for k in range(len(particulas)):
        if salga:
            break
        for l in range(len(particulas)):
            if salga:
                break
            if k != l:  #K no es igual a L
                d= sqrt(((sepx[k] - sepx[l])**2)+((sepy[k] - sepy[l])**2) )
            #SE TOCAN *****************
                if d <= r*2:
                    pygame.draw.circle(screen, (255,255,255),(particulas[k]), r)
                    pygame.draw.circle(screen, (255,255,255),(particulas[l]), r)
                    salga = True
                if d > r*2:
                    pygame.draw.circle(screen, (255,0,0),(particulas[k]), r)
                    pygame.draw.circle(screen, (255,0,0),(particulas[l]), r)
    
        
            pygame.display.flip()
    clock.tick(10)
    
pygame.quit()
        
