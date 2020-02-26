import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from scipy.integrate import odeint
from matplotlib import animation

N = 100
t = np.linspace(0,5,N)

def move_func(s,t):
    x,vx,y,vy,z,vz = s
    dxdt = vx
    dvxdt = (x/a**2)*(g-((vx**2)/a**2)-(vy**2)/b**2)-(vz**2)/(c**2)/((x**2/a**4)+(y**2/b**4)+(z**2/c**4))
    dydt = vy
    dvydt = (y/b**2)*(g-((vx**2)/a**2)-(vy**2)/b**2)-(vz**2)/(c**2)/((x**2/a**4)+(y**2/b**4)+(z**2/c**4))
    dzdt = vz
    dvzdt = -g + (x/a**2)*(g-((vx**2)/a**2)-(vy**2)/b**2)-(vz**2)/(c**2)/((x**2/a**4)+(y**2/b**4)+(z**2/c**4))
    
    return dxdt, dvxdt, dydt, dvydt, dzdt, dvzdt

#l = (g-((dxdt**2)/a**2)-(dydt**2)/b**2)-(dzdt**2)/(c**2)/((x**2/a**4)+(y**2/b**4)+(z**2/c**4))

x0 = 1
vx0 = 0
y0 = 1
vy0 = 0
z0 = 1
vz0 = 0

a = 1
b = 1
c = 1

s0 = x0,vx0,y0,vy0,z0,vz0

g = 9,8

sol = odeint(move_func,s0,t)

fig = plt.figure
ax = p3.Axes3D(fig)

bodys = []

x = sol[:,0]
y = sol[:,2]
z = sol[:,4]



body1, = plt.plot(x,y,z,'or')
body1_line, = plt.plot(x,y,z,'-r')

def ani_func(i):
    body1.setdata(x[i],y[i])
    body1.set_3d_properties(z[i])
    
    body1_line.setdata(x[:i],y[:i])
    body1_line.set_3d_properties(z[:i])
    
    ax.setxlim3d([-10,10])
    ax.setylim3d([-10,10])
    ax.setzlim3d([-10,10])

ani = animation.FuncAnimation(fig, ani_func, N, interval = 50)
plt.show