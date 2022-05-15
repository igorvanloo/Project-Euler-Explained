#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:23:47 2022

@author: igorvanloo
"""
'''
Project Euler Problem 225

Anwser:
    2009
--- 0.7507858276367188 seconds ---
'''
import time
start_time = time.time()

def tribonnaci(mod):
    t0 = 1
    t1 = 1
    t2 = 1
    divisible = False
    
    while True:
        
        tn = (t0 + t1 + t2) % mod
        if tn == 0:
            break
        
        t0 = t1
        t1 = t2
        t2 = tn
        if (t0, t1, t2) == (1, 1, 1):
            divisible = True
            break
        
    return divisible
        
def compute(limit):
    nums = []
    i = 3
    while len(nums) != limit:
        if tribonnaci(i):
            nums.append(i)
        i += 2
    return nums[-1]
    
if __name__ == "__main__":
    print(compute(124))
    print("--- %s seconds ---" % (time.time() - start_time))
