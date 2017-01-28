import random
from math import sqrt
from matplotlib.pylab import hist, show
parti=[]
dist=[]
n = 100 
d = 3
p = 2
l = 50

for x in range(n):
    part = [random.randrange(-l,l,p) for y in range(d)]
    parti.append(part)

print(parti)
    
for part in parti:
    dist.append(sqrt(sum([x**2 for x in part])))

print(dist)

hist(dist,n,(0,100))
show()
