import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()
a = 0.5
anim_list=[]
x_coord = np.linspace(-5, 5, 100)
y_coord = a*x_coord**2

def circle_func(x_centre,y_centre,R=1,N=len(x_coord)):
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(0,N,1):
        alpha = np.linspace(0,2*np.pi,N)
        x[i]=x_centre+R*np.cos(alpha[i])
        y[i]=y_centre+R*np.sin(alpha[i])
    return x,y
        
for i in range(len(x_coord)):
   # parabola,=plt.plot(x_coord[:i],y_coord[:i])
   x,y = circle_func(x_coord[i],y_coord[i])
   point, =plt.plot(x_coord[i], y_coord[i], 'o', ms=0.5)
   tail, =plt.plot(x_coord[:i],y_coord[:i], 'o-', lw=0.125)
   circle, =plt.plot(x,y,'go-', lw=0.125)
   anim_list.append([point,tail,circle])

plt.axes().set_aspect('equal')
ani=ArtistAnimation(fig, anim_list, interval=20)
ani.save('parab.gif')