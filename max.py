import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig=plt.figure
R = 100
N=1000
x_coord=np.zeros(N)
y_coord=np.zeros(N)

x=np.zeros(N)
y=np.zeros(N)
alpha=np.linspace(0,2*np.pi,N)
for i in range(0,N,1):
    x[i]=R*np.cos(alpha[i])**3
    y[i]=R*np.cos(alpha[i])**3

def circle_func(x_centre,y_centre,R=1,N=len(x_coord)):
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(0,N,1):
        alpha = np.linspace(0,2*np.pi,N)
        x[i]=x_centre+R*np.cos(alpha[i])
        y[i]=y_centre+R*np.sin(alpha[i])
    return x,y

point, =plt.plot(x[i], y[i], 'o')
tail, =plt.plot(x[:i],y[:i], 'o-')
anim_list=[]
anim_list.append([point,tail])
plt.axes().set_aspect('equal')
ani=ArtistAnimation(fig, anim_list, interval=20)
ani.save('astroid.gif')