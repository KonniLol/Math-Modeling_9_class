import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from scipy.integrate import odeint
from matplotlib import animation
from sympy import *

f = Function('f')
x = Function('x')
y = Function('y')
z = Function('z')
t = Symbol('t')
R = Symbol('R')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

f = (x(t)**2/a**2)+(y(t)**2/b**2)+(z(t)**2/c**2) - R**2

print(diff(f, x(t)))
print(diff(f, y(t)))
print(diff(f, z(t)))
print(diff(f, t))
print()
print(diff(diff(f,t),t))

N = 200
t = np.linspace(0,50,N)

