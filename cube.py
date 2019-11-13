import numpy as np
import matplotlib.pyplot as plt

def lense(h=1,F=1):
    plt.plot([0],[-2])
    plt.plot([0],[2])
    plt.plot([0,0],[-2,2])
    plt.plot([-5,5],[0,0])
    plt.plot([-5,0],[h,h])
    plt.plot([0,h],[F,0])
    plt.plot([F],[0],marker="o")
    
    
    plt.axis('equal')
    
lense()