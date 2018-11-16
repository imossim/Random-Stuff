#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:38:19 2018

@author: imossim
"""
import numpy.random as random
import math

#Monte Carlo style method to approximate pi

#Equation of semicircle is y = sqrt(r-x^2)
# should points on the line be included?
def in_quadrant(rad,x,y):
    if(pow(y,2)+pow(x,2)<pow(rad,2)):
        return True
    else:
        return False
    
iterations = 100000
inside_quad = 0
outside_quad = 0
radius = 1

#generate coordinates
for i in range(iterations):
    x = random.uniform(0,radius)
    y = random.uniform(0,radius)
    if (in_quadrant(radius,x,y)):
        inside_quad += 1
        #print([x,y,1])
    else:
        outside_quad +=1
        #print([x,y,0])

#value of Pi generated
print ((inside_quad/iterations)*4)
#error
print (((inside_quad/iterations)*4-math.pi)/math.pi)