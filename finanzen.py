import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 30, 0.0000001)
def cash(n, t):
    dndt = - k * n * t
    return dndt
n0 = 1000
k = 0.08
solve_finanzen = odeint(cash, n0, t)
plt.plot(t, solve_finanzen)
plt.show()