#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:09:18 2021

@author: igorvanloo
"""

'''
Project Euler Problem 587

A square is drawn around a circle as shown in the diagram below on the left.
We shall call the blue shaded region the L-section.
A line is drawn from the bottom left of the square to the top right as shown in the diagram on the right.
We shall call the orange shaded region a concave triangle.

It should be clear that the concave triangle occupies exactly half of the L-section.

Two circles are placed next to each other horizontally, a rectangle is drawn around both circles, and a line is drawn 
from the bottom left to the top right as shown in the diagram below.

This time the concave triangle occupies approximately 36.46% of the L-section.

If n circles are placed next to each other horizontally, a rectangle is drawn around the n circles, and a line is 
drawn from the bottom left to the top right, then it can be shown that the least value of n for which the concave triangle 
occupies less than 10% of the L-section is n = 15.

What is the least value of n for which the concave triangle occupies less than 0.1% of the L-section?

Reasoning

We can form simple equations
if we define the bottom left corner to be (0,0) then the first circle is (y+1)^2 + (x+1)^2 = 1

so we have the botton of the circle is f(x) = -sqrt(1-(x-1)^2) + 1
The line cutting through the c circles is defined by g(x) = x/c

The total area of the L-section is (4-pi)/4 = 1 - pi/4, the concave triangle is simply the area enclosed by the region
g(x) and f(x)

So we find at what x, g(x) = f(x) , call this x0, then x0 * f(x0)/2 + integral from x0 to 1 of f(t) dt = concave region

Further reasoning

x0 for a given c is (c  - sqrt(2) c^(3/2) + c^2)/(1 + c^2)

The integral of f(x) is F(x) = x - 1/2 sqrt(2 - x) x^(3/2) + 1/2 sqrt(-(-2 + x) x) + sin^(-1)(sqrt(1 - x/2))
F(1) = 1 + pi/4

Anwser:
    2240
--- 0.004186868667602539 seconds ---
'''

import time, math

start_time = time.time()

def f(x):
    return -math.sqrt(1-(x-1)**2) + 1

def F(x):
    return x - (math.sqrt(2 - x)* x**(3/2))/2 + (math.sqrt(-(-2 + x)*x))/2 + math.asin(math.sqrt(1 - x/2))

def compute(percent):

    Lsection = 1 - math.pi/4
    c = 1
    while True:
        w = (c  - math.sqrt(2)* c**(3/2) + c**2)/(1 + c**2)
        
        ConcaveRegion = (w * f(w)) / 2 + (1+math.pi/4) - F(w)
        
        temp = (100*ConcaveRegion/Lsection)
        
        if temp < percent:
            break
        
        c += 1
    return c
    

if __name__ == "__main__":
    print(compute(10))
    print("--- %s seconds ---" % (time.time() - start_time))