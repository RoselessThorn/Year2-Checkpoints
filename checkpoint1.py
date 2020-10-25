# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:13:16 2020

@author: HP
"""
#Write a Python program to calculate and print to the terminal the radius and surface area of a sphere from its volume.

#Your program should:

#Prompt for the volume of a sphere in mm3.
#Calculate and print out to the terminal the radius and the surface area of the sphere in m and m2 respectively in an understandable format.
#Check your program works for a range of volumes, both large and small and that you have the output units correct.
import math
v=input("PLease enter the volumn in mm^3：") #input the volumn as string
v=float(v)                                  #change the string into float
radius=pow((3*v/(4*math.pi)),1/3)             #calcuate the radius
sarea=4*math.pi*radius*radius                #calcuate the surface area
radius = radius/1000
sarea  = sarea/1000000
print  ("Surface area of the sphere in m^2:%.10f"% sarea)   #output of surface area
print ("Radius of the sphere in m: %.10f"% radius)          #output of radius
