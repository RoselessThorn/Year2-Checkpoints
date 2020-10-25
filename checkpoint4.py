# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:49:39 2020

@author: HP
"""

import math
import numpy as np
import matplotlib.pyplot as plt
def main():                         #main function
    path = "F:\\" + input('enter the file name:')        #path of the file
    result=[]                   #empty list for input
    with open(path,'r') as f:       #input each element into the list divided by coma
        for line in f:
            result.append(list(line.strip('\n').split(',')))
    #print(len(result))
    #print(result)
    for i in range(len(result)):    #to determine from which element the comment stops
        f = str((result[i])[0]).startswith('#')
        if f == False:
            break
            return i             #return the index of the last comment
    #print(i)
    voltage = []                #define two new empty lists for voltage and current data
    current = []
    for o in range(i,len(result)):      #to input data from the first datum, skip the comment
        voltage.append((result[o])[0])
        current.append((result[o])[1])
    #print(voltage)
    p = []              #set up a empty list for P(t)
    #print((len(result)-i))
    for k in range((len(result)-i)):        #each P(t) value is calculated from the corresponding V and I value
        p.append(math.log(float(voltage[k])*float(current[k])))
        #print(p)
        step = 25e3/(len(result)-i)         #step up the corresponding data for t
        t = np.arange(0.0,25E3,step) 
    #print (p)
    plt.plot(t,p)   #plot the diagram with x and y axis with t and p(t)
    plt.xlabel('t',fontproperties='Kaiti',fontsize=14,color='red')       #labels
    plt.ylabel('P(t)',fontproperties='SimHei',fontsize=18,color='red')
    plt.title('p(t)=log(V(t)I(t))',fontproperties='SimHei',fontsize=18,color='green')  #title
    plt.grid(True)              #grid
    plt.show()
main()