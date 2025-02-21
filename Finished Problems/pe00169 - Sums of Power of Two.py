# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:36:28 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 169

https://oeis.org/A002487

Answer:
    178653872807
--- 0.0 seconds ---
'''
import time
from functools import cache
start_time = time.time()

@cache
def a(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    if n % 2 == 0:
        return a(n//2)
    else:
        return a((n - 1)//2) + a((n - 1)//2 + 1)

def f(n):
    return a(n + 1)

if __name__ == "__main__":
    print(f(10**25))
    print("--- %s seconds ---" % (time.time() - start_time))
