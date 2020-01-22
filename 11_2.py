import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

t=np.arange(0,25,0.1)
def func(z,t):
    x,v_x,y,v_y=z
    dxdt=v_x
    dv_xdt=0#(F1+F2*np.cos(A))/m
    dydt=v_y
    dv_ydt=-10
    return dxdt,  dv_xdt, dydt,  dv_ydt

F1=10
F2=10
m=100
alpha = 1
A=alpha
V=250
x0=0
v_x0=V*np.cos(A)
y0=0
v_y0=V*np.sin(A)
z0=x0, v_x0, y0, v_y0


sol=odeint(func,z0,t)

fig=plt.figure()
sili=[]

for i in range(0,len(t),1):
    Fas,=plt.plot(sol[:i,0],sol[:i,2],'-',color='r')
    Fas_line,=plt.plot(sol[i,0],sol[i,2],'o',color='r')
    sili.append([Fas,Fas_line])
ani=ArtistAnimation(fig,sili,interval=30)
plt.axis('equal')
ani.save('kanone.gif')    
