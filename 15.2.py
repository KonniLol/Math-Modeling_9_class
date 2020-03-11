import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from scipy.integrate import odeint
from matplotlib import animation

N = 200
t = np.linspace(0,50,N)

def move_func(s,t):
    x,vx,y,vy,z,vz = s
    dxdt = vx
    dvxdt = ((3*g * z)/(z**2 + x**2)) * x
    dydt = vy
    dvydt = 0
    dzdt = vz
    dvzdt = -g + ((3*g * z)/(z**2 + x**2)) * z
    
    return dxdt, dvxdt, dydt, dvydt, dzdt, dvzdt

#l = -(3*g * z)/(z**2 + x**2)

x0 = 1
vx0 = 0
y0 = 0
vy0 = 1
z0 = 0
vz0 = 0

s0 = x0,vx0,y0,vy0,z0,vz0

g = 9.8

sol = odeint(move_func,s0,t)

fig = plt.figure()
ax = p3.Axes3D(fig)

bodys = []

x = sol[:,0]
y = sol[:,2]
z = sol[:,4]

Phi = np.linspace(1,2*np.pi)
r = np.linspace(0,50,1000)

x_pipe = np.outer(np.ones(np.size(r)),np.cos(Phi))
y_pipe = 
z_pipe = np.sin(Phi)

dot, = plt.plot(x,y,z,'or')
line, = plt.plot(x,y,z,'-r')

def ani_func(i):
    dot.set_data(x[i],y[i])
    dot.set_3d_properties(z[i])
    
    line.set_data(x[:i],y[:i])
    line.set_3d_properties(z[:i])
    
    ax.set_xlim3d([-10,10])
    ax.set_xlabel('X')
    ax.set_ylim3d([-10,10])
    ax.set_ylabel('Y')
    ax.set_zlim3d([-10,10])
    ax.set_zlabel('Z')
    
ax.plot_surface(x_pipe,y_pipe,z_pipe,color='b')

ani = animation.FuncAnimation(fig, ani_func, N, interval = 50)
plt.show
ani.save('ani.gif')