#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:11:28 2022

@author: igorvanloo
"""
'''
Project Euler Problem 226

I(1) = 1/2
blanc(x) = blanc(2x)/2 + s(x)
I(x) = integral{0 to x} blanc(y) dx

I(x) = I(2x)/4 + x^2/2 if 0 < x ≤ 1/2
       1/2 - I(1 - x) if 1/2 < x ≤ 1
       n/2 + I(x - n) if n ≤ x ≤ n + 1
       
Intersection at 0.0789, and 0.5

Circle is (x - 1/4)^2 + (y - 1/2)^2 = 1/16
bottom half is y = (1 - √(2x - 4x^2))/2

Anwser:
    0.11316017
--- 0.00037598609924316406 seconds ---
'''
import time, math
from scipy.integrate import quad

start_time = time.time()

def f(x):
    return (1 - math.sqrt(2*x - 4*x*x))/2

def I(x):
    if x == 1:
        return 1/2
    
    if 0 < x <= 1/2:
        return I(2*x)/4 + (x*x)/2
    if 1/2 < x <= 1:
        return 1/2 - I(1 - x)

def compute():
    area_under_blancmange = I(1/2) - I(0.0789)
    area_under_circle = quad(f, 0.0789, 1/2)[0]
    return round(area_under_blancmange - area_under_circle, 8)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))