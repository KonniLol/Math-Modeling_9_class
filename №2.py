import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

t = np.arange(10**(-7),1.1*10**(-7),10**(-11))

def mf(s,t):
    x, vx, y, vy, z, vz = s
    dxdt = vx
    dvxdt = q/m*(Ex+vy*Bz-By*vz)
    dydt = vy
    dvydt = q/m*(Ey+vz*Bx-Bz*vx)
    dzdt = vz
    dvzdt = q/m*(Ez+vx*By-Bx*vy)
    return dxdt,dvxdt,dydt,dvydt,dzdt,dvzdt

x0 = 0
vx0 = 10**7
y0 = 0
vy0 = 10**6
z0 = 0
vz0 = 0

s0 = x0,vx0,y0,vy0,z0,vz0

m = 1.6*10**(-31)
q = 1.6*10**(-19)

Ex = 0
Ey = 10**(-3)
Ez = 0

Bx = 10**(-3)
By = 10**(-3)
Bz = 10**(-3)

sol = odeint(mf,s0,t)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(sol[:,0],sol[:,2],sol[:,4],label='e traject')

ax.quiver(x0,y0,z0,Bx,By,Bz,length=(sol[len(t)-1,4] - sol[0,4]),normalize=True, color='r', label='B')
ax.quiver(x0,y0,z0,Ex,Ey,Ez,length=(sol[len(t)-1,4] - sol[0,4]),normalize=True, color='g', label='E')
ax.quiver(x0,y0,z0,vx0,vy0,vz0,length=(sol[len(t)-100,4] - sol[0,4]),normalize=True, color='k', label='V')

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show