#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 23:26:58 2021

@author: igorvanloo
"""

'''
Project Euler Problem 371

E(Z) = sum_{0 to inf} of x*p_z(x) dx

P{Z = 1} = 0
P{Z = 2} = 1/(1000)
P{Z = 3} = 999/1000 * 2/1000
P{Z = 4} = 999/1000 * 998/1000 * 3/1000
P{Z = j} = (999 P 1001-j * (j-1))/1000^{j-1}

This doesn't account for if we see the 0 plate first!!

P{Z = 2} = 999/1000 * 1/1000
P{Z = 3} = 2 * 1/1000 * 1/1000 (Get a 0 then any number then matching plate or any number then 0 then maching plate) + 999/1000 * 2/1000
P{Z = 4} = 3 * 1/1000 * 999/1000 * 1/1000 + 999/1000 * 998/1000 * 3/1000
P{Z = j} = (j-1)*1/1000^2* 999 P 

Using this we can get a reaonsable estimate of 40.06429769686301

Anwser:

'''

import time, math
start_time = time.time()

def compute(n):
    total = 2/n
    
    for x in range(3, 1000):
        temp = x*(x - 1)/(n**(x-1))
        for y in range(n-1, n+1 - x, -1):
            temp *= y
        
        total += temp
    return total
        
if __name__ == "__main__":
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))