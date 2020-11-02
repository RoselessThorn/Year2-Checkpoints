# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:57:00 2020
Write a Python program to plot out the trajectory of a projectile starting at position x→0=(0,0) for specified initial velocity and normalised drag coefficient. You program should prompt for

Magnitude of the initial velocity v0 in ms−1.
Angle θ from the horizontal of initial velocity in degrees.
β the normalised drag coefficient.
Δt the step interval in seconds.
The path should be traced and displayed using Matplotlib from the inital starting position until the particle re-crosses the x-axis. Your graph should have a suitable title and axis labels. Your program should also print the range of the projectile to the terminal.
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
    ay = (-beta*v*vy)-g
    return ax, ay

def step_forward(x, y, vx, vy, beta, delta_t,ax,ay):             #Do a forward step
    vx = vx + delta_t*ax
    vy = vy + delta_t*ay
    x = x + delta_t*vx
    y = y + delta_t*vy

    return x, y, vx, vy
    
def main():
    v_initial = float(input("Input initial velocity in meter per second:"))  #Input of variables
    theta = float(input("Input theta in degrees:"))
    beta = float(input("Input beta:"))
    delta_t = float(input("Input time interval in seconds:"))
    y_data = [0]                          #List with one 0 as step_forward function skips the first point    
    x_data = [0]
    #t = 0
    #time = [0]
    x,y,vx,vy = set_initial(v_initial,theta)        #Get all information needed from defined function
    
    while True:
        ax,ay = acceleration(vx, vy, beta)
        x,y,vx,vy = step_forward(x, y, vx, vy, beta, delta_t,ax,ay)
        vx = vx + delta_t*ax            #Keep adding each point to data list
        vy = vy + delta_t*ay
        y = y + vy*delta_t
        x = x + vx*delta_t
        y_data.append(y)            #Save data
        x_data.append(x)
        #t = t + delta_t
        #time.append(t)
        if y <= 0:              #Stop when the mass reaches the ground
            break
    plt.plot(x_data,y_data)   #plot the diagram with x and y axis with x and y
    plt.xlabel('x(in meters))',fontproperties='Kaiti',fontsize=14,color='red')       #labels
    plt.ylabel('y(in meters)',fontproperties='SimHei',fontsize=18,color='red')
    plt.title('Projectile Motion Diagram',fontproperties='SimHei',fontsize=18,color='green')  #title
    plt.grid(True)              #grid
    plt.show()
    range = x_data[-1]-x_data[0]
    print("Range is " + str(range) + "meters.")
main()

    

    
    