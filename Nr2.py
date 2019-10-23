from math import pi, sin, cos, tan, e, sqrt
from const import acceleration_of_gravity as g
from const import boltzmann_constant as k
from const import plank_const as ph

h = 100
β = pi/3
α = pi/5
t = 200
ε = 300

v = sqrt((g*h*(1/tan(β))**2)/(2*(cos(α))**2*(1-1/tan(β)*tan(α))))

print(v)

n = (2/sqrt(pi))*(ph/(k*t)**1.5)*(e**(-e/k*t))*(e**(t/2))

print(n)