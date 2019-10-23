import numpy as np
from const import acceleration_of_gravity as g

x0 = 0
y0 = 0
vx0 = 1

t = np.arange(0,5,0.1)
n = len(t)
txy = np.ndarray(shape=(n,3))

for i in range(0,n,1):
    txy[i,0] = x0 + t[i]*vx0
    txy[i,1] = y0 + t[i]*vx0 - (g*t[i]**2)/2
    txy[i,2] = t[i]
    
print(txy)