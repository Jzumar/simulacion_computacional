import pygame,random
from pygame.locals import *
from math import sqrt

def mueve(x, y, dx, dy, xm, ym):
    x += dx
    y += dy
    if x < 0: #Si sale de pantalla entra del otro lado
        x += xm
    elif x > xm:
        x -= xm
    if y < 0:
        y += ym
    elif y > ym:
        y -= ym    
    return (x, y)

def main():
    xmax = 800
    ymax = 600
    pygame.init()
    screen = pygame.display.set_mode((xmax, ymax))
    white = (255, 255, 255) 
    clock=pygame.time.Clock()
    d = dict()
    velX = dict()
    velY = dict()
    tam = dict()
    umbral = dict()
    pos = dict()
    masa = dict()
    color = dict()
    grupo = dict()
    n = 20
    grav = 10
    for p in range(n):
        color[p] = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        pos[p] = (random.randint(0, xmax), random.randint(0, ymax))
        grupo[p] = p
        velX[p] = 0
        velY[p] = 0
        d[p] = random.randint(10,25)
        masa[p] = d[p]
        tam[p] = d[p] // 2 - 2
        umbral[p] = 4 * tam[p] + 2

    exitflag = False
    while n > 1 and not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True
                    
        screen.fill(white)

        lideres = set(grupo.values())
        n = len(lideres)
        for lider in lideres:
            dx = round(velX[lider])
            dy = round(velY[lider])
            for p in pos:
                if grupo[p] == lider:
                    pos[p] = mueve(pos[p][0], pos[p][1], dx, dy, xmax, ymax)

        for p in pos:
            pygame.draw.circle(screen, color[p], pos[p], d[p])
           # pygame.draw.circle(VENTANA, self.color, (int(self.x), int(PANTALLA['ALTO'] - self.y)), int(round(self.radio)))
        pygame.display.flip()
        clock.tick(50) 

        #if random.random() < 0.2:
         #   v += 1
            
        for p1 in pos:
            x = pos[p1][0]
            y = pos[p1][1]
            for p2 in pos:
                if grupo[p1] != grupo[p2]:
                    distX = x - pos[p2][0]
                    distY = y - pos[p2][1]
                    distPS = sqrt((x - pos[p2][0])**2 + (y - pos[p2][1])**2)
                    #fuerza = (G*M1*M2)/(R^2)
                    fuerza = grav*(masa[p1]*masa[p2]) / (distPS**2)
                    #aceleracion = F/M
                    acel = fuerza / masa[p1]
                    Xcomp = distX / distPS
                    Ycomp = distY / distPS
                    velX[p1] -= acel * Xcomp
                    velY[p1] -= acel * Ycomp
                    if distPS < umbral[p1]:
                        nuevo = grupo[p1]
                        c = color[p1]
                        for p in pos:
                            if grupo[p] == p2:
                                grupo[p] = nuevo
                                color[p] = c
                                masa[p] = masa[p2]
            
    pygame.quit()

if __name__ == "__main__":
    main()


    
