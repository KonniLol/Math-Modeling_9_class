import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax=plt.subplots()
anim_object, = plt.plot([],[],marker='o')
def Cycloida_m(r, t):
    x=r*(t-np.sin(t))
    y=r*(1-np.cos(t))
    return x, y
edge=20
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(i):
    anim_object.set_data(Cycloida_m(r=10, t=i))
ani=animation.FuncAnimation(fig, animate, frames=np.arange(-4, 2*np.pi, 0.1), interval=20)

ani.save('Cycloida.gif')