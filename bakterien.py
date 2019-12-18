import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 100, 1)
def bacteria(n, t):
    dndt = k * n
    return dndt
n0 = 1
k = 0.05
solve_bact = odeint(bacteria, n0, t)
plt.plot(t, solve_bact)
plt.show()