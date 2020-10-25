# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:21:46 2020

@author: HP
"""
import math
def main(a,b,c):                    #define the main function
    d = b*b-4*a*c                   #set d as the discriminant
    if a == 0:                      #when a=0 it is a linear equation
        return -c/b
    elif d == 0:                    #when the discriminant=0 the equation has two equal real roots
        return -b/(2*a)
    elif d < 0:                     #when the discriminant<0 it has two imaginary roots
        return str((-b)/(2*a))+str((-math.sqrt(-d))/(2*a))+'i',str((-b)/(2*a))+'+'+str((math.sqrt(-d))/(2*a))+'i'
    else:                           #otherwise it has two different real roots
        return (-b-math.sqrt(d))/(2*a),(-b+math.sqrt(d))/(2*a)
a = float(input('input a:'))        #input of viarables
b = float(input('input b:'))
c = float(input('input c:'))
print (main(a,b,c))                 #output of result