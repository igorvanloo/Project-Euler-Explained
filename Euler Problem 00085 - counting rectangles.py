#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:25:31 2021

@author: igorvanloo
"""
'''
Project Euler Problem 85
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the 
grid with the nearest solution.

Reasoning:
    A rectangle is simply a set of 2 parralel lines, if we split it up into h horizontal and v vertical lines
    we have that there h-1 and v-1 parts, so we need all the combinations of these. Hence we get 
    h choose 2 * v choose 2 = number of rectangles in a rectangle
    or hv(h-1)(v-1)/4
    
    if h = 2, 2v(1)(v-1)/4 = 2000000 occurs when v^2 - v - 4000000 = 0 so v = 2001
    if v = 2 by symmetry h = 2001 so we are looking for a combination for h,v 2 < h,v < 2001 such that 
    it is closest to 2000000

Anwser:
    (2.0, 78, 37, 2772)
--- 0.6558127403259277 seconds ---
    
'''

import time
start_time = time.time()

def number_of_rectangles(h,v):
    return (h*v*(h+1)*(v+1))/4
    
def compute():
    smallest_difference = 10000
    test_list = []
    for h in range(1,2000):
        for v in range(1,2000):
            test = abs(number_of_rectangles(h, v) - 2000000)
            if test <= smallest_difference:
                smallest_difference = test
                test_list.append((h)*(v))
                
    return test_list[-1]
            

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
