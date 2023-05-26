# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:25:51 2023

@author: igorvanloo
"""
'''
Project Euler Problem 813

First thing to notice is that P(n) = P(n - x) ⊗ P(x), 1 <= x < n

P(8) = P(4) ⊗ P(4)

Not sure how to continue

Anwser:

'''
import time, math
from functools import cache
start_time = time.time()

def xorProduct(x, y):
    prod = 0
    while y != 0:
        if y % 2 == 1:
            prod ^= x
        x <<= 1
        y >>= 1
    return prod

@cache
def P(n, level):
    print("t", n, level)
    if n == 1:
        return 11
    a, b = P(n - n//2, level + 1), P(n//2, level + 1)
    return xorProduct(a, b)

def compute(g):
    mod = pow(10, 9) + 7
    return P(g, 0) % mod

if __name__ == "__main__":
    print(compute(pow(8, 6) * pow(12, 0)))
    print("--- %s seconds ---" % (time.time() - start_time))
