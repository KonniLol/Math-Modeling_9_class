import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()
def circle_func(x_centre,y_centre,R,N):
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(0,N,1):
        alpha=np.linspace(0.2*np.pi,N)
        x[i]=x_centre+R*np.cos(alpha[i])
        y[i]=y_centre+R*np.sin(alpha[i])
    return x,y

t = np.linspace(0,4*np.pi,100)
R=1
N=100
cycloid_x=R*(t-np.sin(t))
cycloid_y=R*(1-np.cos(t))
x_centre_move=R*t
anim_list=[]
for i in range(0,N,1):
    x,y=circle_func(x_centre_move[i],R,R=R,N=N)
    circle,=plt.plot(x,y,'g-',lw=2)
    cycloid,=plt.plot(cycloid_x[:i+1],cycloid_y[:i+1],'r-',lw=2)
    point,=plt.plot(cycloid_x[i],cycloid_y[i],'bo')
    anim_list.append([circle,cycloid,point])
plt.axes().set_aspect('equal')
ani=ArtistAnimation(fig,anim_list,interval=50)
ani.save('cycloid.gif')