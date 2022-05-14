#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 21:10:05 2022

@author: igorvanloo
"""
'''
Project Euler Problem 211

For a positive integer n, let σ2(n) be the sum of the squares of its divisors. For example,

σ2(10) = 1 + 4 + 25 + 100 = 130.

Find the sum of all n, 0 < n < 64,000,000 such that σ2(n) is a perfect square

Anwser:
    1922364685
--- 607.2159321308136 seconds ---
'''
import time
start_time = time.time()

def is_quadratic(x):
    sqrt_root = (x ** (1 / 2))
    if round(sqrt_root) ** 2 == x:
        return True
    return False
    
def compute(limit):
    array = [0]+[1]*(limit - 1)
    
    for x in range(2, limit):
        if x % 1000000 == 0:
            print(x)
        for y in range(x, limit, x):
            array[y] += x*x
    return sum([x for x in range(len(array)) if is_quadratic(array[x])])

if __name__ == "__main__":
    print(compute(640000))
    print("--- %s seconds ---" % (time.time() - start_time))
