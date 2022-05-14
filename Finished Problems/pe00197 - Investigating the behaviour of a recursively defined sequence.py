#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 22:17:29 2022

@author: igorvanloo
"""

'''
Project Euler Problem 197

Given is the function f(x) = ⌊2^(30.403243784-x^2)⌋ × 10^(-9) ( ⌊ ⌋ is the floor-function),
the sequence u_n is defined by u_0 = -1 and u_(n+1) = f(u_n).

Find u_n + u_n+1 for n = 1012.
Give your answer with 9 digits after the decimal point.

Just programmed the function after noticed that it will converge fairly quickly, it says on my program it only need 518 iterations
for the first 9 digits to become stable

Anwser:
    1.710637717
--- 0.0010340213775634766 seconds ---
'''
import time, math
start_time = time.time()

def f(x):
    return math.floor(pow(2, 30.403243784 - x*x)) * pow(10, -9)

def compute():
    u_0 = -1
    prev_sum = 0
    running = True
    while running:
        u_n = f(u_0)
        u_prev = u_0
        u_0 = u_n
        new_sum = u_n + u_prev
        if round(new_sum, 10) == round(prev_sum, 10):
            running = False 
        else:
            prev_sum = new_sum
    return round(new_sum, 9)
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))