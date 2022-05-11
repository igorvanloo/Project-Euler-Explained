#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:27:51 2022

@author: igorvanloo
"""
'''
Project Euler Problem 178

Anwser:
    126461847755
--- 0.17633914947509766 seconds ---
'''
import time
from functools import cache
start_time = time.time()

@cache
def rec(goal, pos, prev, mask):
    
    total = 0
    if pos == goal:
        if mask == (1 << 11) - 1:
            return 1
        else:
            return 0
    
    if pos == 0:
        for x in range(1, 10):
            total += rec(goal, pos + 1, x, mask | 2**(x))
    else:
        if prev > 0:
            total += rec(goal, pos + 1, prev - 1, mask | 2**(prev - 1))
            
        if prev < 9:
            total += rec(goal, pos + 1, prev + 1, mask | 2**(prev + 1))
    
    return total

def compute(limit):
    total = 0
    for x in range(10, limit + 1):
        total += rec(x, 0, 0, 1 << 10)
    return total

if __name__ == "__main__":
    print(compute(40))
    print("--- %s seconds ---" % (time.time() - start_time))
