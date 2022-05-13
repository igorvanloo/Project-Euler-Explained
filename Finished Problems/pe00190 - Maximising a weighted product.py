#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:39:17 2022

@author: igorvanloo
"""
'''
Project Euler Problem 190

We use lagrange multipliers

[P_m] = floor(prod_{i = 1 to m} (2i/(m+1)^i))

Anwser:
    371048281
--- 0.00016617774963378906 seconds ---
'''

import time, math
start_time = time.time()

def P(m):
    total = 1
    for i in range(1, m + 1):
        total *= pow((2*i)/(m+1), i)
    return math.floor(total)

def compute(limit):
    total = 0
    for m in range(2, limit + 1):
        total += P(m)
    return total

if __name__ == "__main__":
    print(compute(15))
    print("--- %s seconds ---" % (time.time() - start_time))