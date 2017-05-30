import pygame,random
from pygame.locals import *
from math import sqrt

def mueve(x, y, dx, dy,pegadas):
    
    if x > 212: 
        x += dx
        y += dy
    else:
        pegadas = 1 
    return (x, y,pegadas)

def main():
    
    xmax = 800
    ymax = 600
    pygame.init()
    myfont = pygame.font.SysFont("calibri", 30)
    labelmas = myfont.render("+", 1, (0,0,0))
    labelmenos = myfont.render("-", 1, (0,0,0))
    screen = pygame.display.set_mode((xmax, ymax))
    white = (255, 255, 255) 
    clock=pygame.time.Clock()
    pegadas = 0
    contpega = dict()
    d = dict()
    move = dict()
    velX = dict()
    velY = dict()
    tam = dict()
    umbral = dict()
    pos = dict()
    carga = dict()
    color = dict()
    grupo = dict()
    n = 150
    K = 78.54
    contador = 0
    for p in range(n):
        color[p] = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        grupo[p] = p
        contpega[p] = 0
        velX[p] = 0
        velY[p] = 0
        d[p] = 12
        if p == 0:
            carga[p] = -500
            pos[p] = [176,300]
            d[p] = 20
            color[p] = (0,0,0)
        else:
            carga[p] = d[p]
            pos[p] = [random.randint(212, xmax), random.randint(0, ymax)]
        tam[p] = d[p] // 2
        umbral[p] = 4 * tam[p] 

    exitflag = False
    while n > 1 and not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True
                    for L in range(n):
                        if contpega[L] == 1:
                            contador += 1
                    print(contpega)
                    print(contador*100/n,"%")
                    
        screen.fill(white)
        pygame.draw.rect(screen, (125,125,125), (0,0,(188),600))
        for u in range(20):
            screen.blit(labelmenos,( 150, 20+u*50) )
        iones = set(grupo.values())
        n = len(iones)#######################################################################################3
        for ion in iones:
            dx = velX[ion]
            dy = velY[ion]
            for p in pos:
                if grupo[p] == ion:
                    move = mueve(pos[p][0], pos[p][1], dx, dy,pegadas)
                    contpega[p] = move[2]                            
                    pos[p] = (move[0],move[1])

        for p in pos:
            if p != 0:
                pygame.draw.circle(screen, color[p], (int(pos[p][0]),int(ymax-pos[p][1])), d[p])
                screen.blit(labelmas, (int(pos[p][0]-7),int(ymax-pos[p][1]-14)))
        pygame.display.flip()
        clock.tick(50) 
                 
        for p1 in pos:
            x = pos[p1][0]
            y = pos[p1][1]
            for p2 in pos:
                if grupo[p1] != grupo[p2]:                    
                    if p1 == 0:
                        y = pos[p2][1]
                    if p2 == 0:
                        pos[p2] = (pos[p2][0], pos[p1][1])

                    distX = x - pos[p2][0]
                    distY = y - pos[p2][1]
                    distPS = sqrt((x - pos[p2][0])**2 + (y - pos[p2][1])**2)
                    #LEY DE COULOMB fuerza = (K*Q1*Q2)/(D^2)
                    fuerza = K*(carga[p1]*carga[p2]) / (distPS**2)
                    #aceleracion = F/M
                    acel = fuerza / carga[p1]
                    Xcomp = distX / distPS
                    Ycomp = distY / distPS
                    velX[p1] += acel * Xcomp
                    velY[p1] += acel * Ycomp
                    if distPS < umbral[p1]:
                        velX[p1] = 0
                        velY[p1] /= 2
                                
    pygame.quit()

if __name__ == "__main__":
    main()


    
