import random
from turtle import *



title("Ejemplo particula")
hideturtle()

setup(600,600,0,0)
penup()
goto(-265,265)
pendown()
goto(265,265)
goto(265,-265)
goto(-265,-265)
goto(-265,265)
penup()

parti=[]
dist=[]
n = 1 
d = 2
x = 0
y = 0

while(1):
    opcion=random.randrange(0,2,1)
    pos = random.randrange(0,2,1)
    r = (random.randrange(0,10,1))/10  
    g = (random.randrange(0,10,1))/10  
    b = (random.randrange(0,10,1))/10  
    
    print(opcion,'\n')
    if opcion == 0:
        
        if pos == 0:
            if x >= 250:
                x = x - 50
            else:
                x = x + 50
            
        else:
            if x <= -250:
                x = x + 50
            else:
                x = x - 50
    if opcion == 1:
       
        if pos == 0:
            if y >= 250:
                y = y-50
            else:
                y = y + 50
        else:
            if y <= -250:
                y = y+50
            else:
                y = y - 50
            
           
   # r = (random.randrange(0,10,1))/10    
    
    print(x)
    print(y)
    
    penup()
    
    x2 = x
    y2 = y
    goto(x,y)
    dot(30,0,0,0)
    goto(x2,y2)
    dot(30,r,g,b)    
    





    






