# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:59:22 2020
Modify the above program to produce a plot of the ratio of final kinetic energy to initial kinetic energy against lauch angle θ in the range 0∘→90∘. Your program should prompt for

Initial velocity v0.
Normalised drag coefficient β.
Timestep Δt.
and plot out, using Matplotlib, a graph of Kf/Ki against θ.
@author: RoselessThorn
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def set_initial(v_initial, theta):               #   Set inital conditions
    theta_in_radian = theta*math.pi/180             #  Change angle unit to radian
    vx = v_initial*math.cos(theta_in_radian)        # x component of velocity
    vy = v_initial*math.sin(theta_in_radian)
    x = 0                                   # Initial position(0,0)
    y = 0
    return x,y,vx,vy

def acceleration(vx, vy, beta):           #Calculate the acceleration 
    g = 9.81
    v = math.sqrt(vx**2+vy**2)
    ax = -beta*v*vx                     #Acceleration of x component with drag
    ay = -beta*v*vy-g
    return ax, ay

def step_forward(x, y, vx, vy, beta, delta_t,ax,ay):             #Do a forward step
    vx = vx + delta_t*ax
    vy = vy + delta_t*ay
    x = x + delta_t*vx
    y = y + delta_t*vy

    return x, y, vx, vy

def KineticEnergy(vx,vy):
    v = math.sqrt(vx**2 + vy**2)
    KE = v**2
    return KE
    
    
def main():
    v_initial = float(input("Input initial velocity in meter per second:"))  #Input of variables
    beta = float(input("Input beta:"))
    delta_t = float(input("Input time interval in seconds:"))
    theta = 0
    Theta = []
    ratio = []
    
    for theta in range(0,91):
        x,y,vx,vy = set_initial(v_initial,theta)    #Initial conditions
        #print(x,y,vx,vy)
        xi = x                              #Save them for Initial Kinetic Energy
        yi = y
        vxi = vx
        vyi = vy
        y = yi
        ax,ay = acceleration(vx, vy, beta)          #Initial acceleration
        #print(ax,ay)
        while y>= 0 :   
            #print(ax,ay)
            x,y,vx,vy = step_forward(x, y, vx, vy, beta, delta_t,ax,ay)     #Each step forward from last step
            #print(x,y,vx,vy)
            ax,ay = acceleration(vx, vy, beta)          #Changing acceleration
            vy = vy + delta_t*ay                    
            vx = vx + delta_t*ax
            y = y + vy*delta_t                      #Changeing of position after each step
            x = x + vx*delta_t
            #print(y)
        #print(vx,vy)                
        Ki = KineticEnergy(vxi,vyi)             #Calcuate the kinetic energy
        Kf = KineticEnergy(vx,vy)
        ratio.append(Kf/Ki)                 #Save each ratio into a list for plotting
        theta += 1    
    Theta = np.arange(0.0,91,1)
    plt.plot(Theta,ratio)   #plot the diagram with x and y axis with x and y
    plt.ylabel('ratio Kf/Ki',fontproperties='Kaiti',fontsize=14,color='red')       #labels
    plt.xlabel('theta(in degrees)',fontproperties='SimHei',fontsize=18,color='red')
    plt.title('Projectile Motion Diagram',fontproperties='SimHei',fontsize=18,color='green')  #title
    plt.grid(True)              #grid
    plt.show()
main()