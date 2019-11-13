import numpy as np
from const import acceleration_of_gravity as g
import matplotlib.pyplot as plt


def schaltjahr(y):
    """JO DIGGA!!!"""
    if y % 400 == 0:
        print("Schaltjahr")
    elif y % 100 == 0:
        print("Kein Schaltjahr")
    elif y % 4 == 0:
        print("Schaltjahr")
    else:
        print("Kein Schaltjahr")

def massive(m):
    """Querprodukt eines numpy massives"""
    result = 1
    for x in m: 
        result = result * x
    print(result)

def energie(m,h,v):
    """Gesamte mechanische energie"""
    energy = ((m * v**2)/2) + (m * g * h)
    print(energy)
    
def parabola(a=1,b=0,c=0,title='parabola'):
    """рисует параболу"""
    x = np.arange(-500,500,0.001)
    y = a*x**2+b*x+c
    plt.plot(x,y)
    plt.title(title)
    plt.show

def hyperbola(a=1,title='hyperbola'):
    """рисует гиперболу"""
    x = np.arange(-500,500,0.001)
    y = a*x**(-1)
    plt.plot(x,y)
    plt.title(title)
    plt.show

def circle(R=1,title='circle'):
    """рисует окружность"""
    x = np.arange(-5,5,0.01)
    y = np.arange(-5,5,0.01)
    X,Y = np.meshgrid(x,y)
    fxy = X**2 + Y**2
    plt.contour(X,Y,fxy,levels=[R])
    plt.axis('equal')
    plt.show()

def cube(a=1,title='cube'):
    """очень хорошое описание"""
    plt.plot([a,a,a+a,a+a,a],[a,a+a,a+a,a,a],color='k')
    plt.plot([2*a,2.5*a,2.5*a,1.5*a,a],[a,1.5*a,2.5*a,2.5*a,2*a],color='k')
    plt.plot([2*a,2.5*a],[2*a,2.5*a],color='k')
    plt.plot([1.5*a,1.5*a,2.5*a],[2.5*a,1.5*a,1.5*a],linestyle='--',color='k')
    plt.plot([1.5*a,a],[1.5*a,a],linestyle='--',color='k')
    plt.title(title)
    plt.axis('equal')
    plt.show()