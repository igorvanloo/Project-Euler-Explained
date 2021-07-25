#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:21:24 2020

@author: igorvanloo
"""

'''
Project Euler Problem 53

How many, not necessarily distinct, values of N choose r
 for 1 <= n <= 100, are greater than one-million?

Anwser:
    4075
--- 0.009176015853881836 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def n_choose_r(n, r):
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
    
def compute():
    count = 0
    for n in range(1,101):
        for r in range(0,n):
            if n_choose_r(n, r) >= 1000000:
                count += 1
    return count
            
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))