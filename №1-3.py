import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

t= np.arange(0.01,16*np.pi,0.01)

x = (np.cos(t))**3
y = (np.sin(t))**3
z = np.cos(2*t)

ax.plot(x,y,z)
plt.show
