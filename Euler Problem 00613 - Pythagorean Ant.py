#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:53:25 2021

@author: igorvanloo
"""

'''
Project Euler Problem 613

Dave is doing his homework on the balcony and, preparing a presentation about Pythagorean triangles, has just cut 
out a triangle with side lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind blows the triangle down 
into the garden.
Another gust blows a small ant straight onto this triangle. The poor ant is completely disoriented and starts to crawl 
straight ahead in random direction in order to get back into the grass.

Assuming that all possible positions of the ant within the triangle and all possible directions of moving on are 
equiprobable, what is the probability that the ant leaves the triangle along its longest side?
Give your answer rounded to 10 digits after the decimal point.

Anwser:
    0.3916721504
'''

import time, math, eulerlib
import matplotlib.pyplot as plt
start_time = time.time()

def compute(a,b):
    total = 0
    count = 0
    for y in range(0,4*a):
        for x in range(0,3*b):
            if y >= (-4*x)/3 + 4*a:
                break
            
            gamma = math.pi/2 + math.atan(x/(4*a-y)) + math.atan(y/(3*b-x))
            total += gamma/(2*math.pi)
            count += 1
      
    return total/count
    
if __name__ == "__main__":
    print(compute(1000,1000))
    print("--- %s seconds ---" % (time.time() - start_time))