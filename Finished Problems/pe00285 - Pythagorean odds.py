#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 23:29:01 2022

@author: igorvanloo
"""
'''
Project Euler Problem 

The probability we win can be mapped inside a torus

(sqrt((k - 0.5)^2 - (k*x + 1)^2) - 1)/k ≤ y ≤ (sqrt((k + 0.5)^2 - (k*x + 1)^2) - 1)/k

Anwser:
    157055.80999
--- 50.01282095909119 seconds ---
'''
import time, math
from scipy.integrate import quad
start_time = time.time()
    
def compute(limit):
    
    def f_upper1(x):
        return (math.sqrt((1.5)*(1.5) - (x + 1)*(x + 1)) - 1)
    
    total = quad(f_upper1, 0, f_upper1(0))[0]
    
    for k in range(2, limit + 1):
        f_lower = lambda x: (math.sqrt((k - 0.5)*(k - 0.5) - (k*x + 1)*(k*x + 1)) - 1)/k
        f_upper = lambda x: (math.sqrt((k + 0.5)*(k + 0.5) - (k*x + 1)*(k*x + 1)) - 1)/k
        
        area_under_upper_circle = quad(f_upper, 0, f_upper(0))[0]
        area_under_lower_circle = quad(f_lower, 0, f_lower(0))[0]
        
        total += k*(area_under_upper_circle - area_under_lower_circle)
    return round(total, 5)

if __name__ == "__main__":
    print(compute(10**5))
    print("--- %s seconds ---" % (time.time() - start_time))
