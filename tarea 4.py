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
    d = 8
    v = 2
    tam = d // 2 - 2
    umbral = 4 * tam + 2
    pos = dict()
    color = dict()
    grupos = list()
    n = 150
    for p in range(n):
        color[p] = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        pos[p] = (random.randint(0, xmax), random.randint(0, ymax))
        grupos.append({p})

    exitflag = False
    while n > 1 and not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True
                    
        screen.fill(white)

        n = len(grupos)
        for grupo in grupos:
            dx = random.randint(-v, v)
            dy = random.randint(-v, v)
            for p in grupo:
                pos[p] = mueve(pos[p][0], pos[p][1], dx, dy, xmax, ymax)

        for p in pos:
            pygame.draw.circle(screen, color[p], pos[p], d)
        pygame.display.flip()
        clock.tick(50) 

        if random.random() < 0.2:
            v += 1
            
        for p1 in pos:
            x = pos[p1][0]
            y = pos[p1][1]
            for p2 in pos:
                    if sqrt((x - pos[p2][0])**2 + (y - pos[p2][1])**2) < umbral:
                        eliminar = None
                        agregar = None
                        for g1 in grupos:
                            if p1 in g1:
                                if not p2 in g1:
                                    for g2 in grupos:
                                        if p2 in g2:
                                            eliminar = [g1, g2]
                                            agregar = g1.union(g2)
                                            break
                                else:
                                    break
                            if agregar is not None:
                                break
                        if agregar is not None:
                            grupos.remove(eliminar[0])
                            grupos.remove(eliminar[1])
                            grupos.append(agregar)
                            c = color[min(agregar)]
                            for p in agregar:
                                color[p] = c
            
    pygame.quit()

if __name__ == "__main__":
    main()


    
