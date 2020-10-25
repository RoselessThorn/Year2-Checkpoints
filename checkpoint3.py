# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 19:55:10 2020

@author: HP
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def shm(omega_zero,gamma,t):          #def the function to calculate the displacement of SHM
    if gamma > 2*omega_zero:            #over damped condition
        p = math.sqrt((gamma*gamma/4)-omega_zero*omega_zero)
        a = 1
        b = gamma/(2*p)
        return np.exp(-gamma*t/2)*(a*np.cosh(p*t)+b*np.sinh(p*t))   #solution for displacement
    elif gamma < 2*omega_zero:          #critially damped condition
        omega = (omega_zero*omega_zero)-math.sqrt(gamma*gamma/4)
        a = 1
        b = gamma/(2*omega)
        return np.exp(-gamma*t/2)*(a*np.cos(omega*t)+b*np.sin(omega*t))
    else:                           #otherwise under damped condition
        a = 1
        b = gamma/2
        return np.exp(-gamma*t/2)*(a + b*t)
#print (shm(omega_zero,gamma,t))
#print (t)
def main():                         #define the main function
    print("For the simple harmonic equation mẍ +bẋ +kx=0,gamma = b/m and omega_zero = math.sqrt(k/m)") #show the user question
    gamma = float(input('input gamma:'))        #input of viarables
    omega_zero = float(input('input omega_zero:'))
    p = 5*np.pi/omega_zero/(float(input('input number of plots:'))) #p is the step used in the new line
    t = np.arange(0.0,5*np.pi/omega_zero,p)          #length divided by step length can get the number of plots
    plt.plot(t,shm(omega_zero,gamma,t))   #plot the diagram with x and y axis with time and displacement
    plt.xlabel('Time',fontproperties='Kaiti',fontsize=14,color='red')       #labels
    plt.ylabel('Displacement',fontproperties='SimHei',fontsize=18,color='red')
    plt.title('Simple Harmonic Motion',fontproperties='SimHei',fontsize=18,color='green')  #title
    plt.grid(True)
    plt.axis([-1,5*np.pi/omega_zero,-1.5,1.5])   #size of the diagram
    plt.show()
    
main()