#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:02:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 668

A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
Including the number 1, there are 29 square root smooth numbers not exceeding 100.

How many square root smooth numbers are there not exceeding 10 000 000 000?

Reasoning

If we find the greatest prime factor of a number we can easily decide whether it is square root smooth, The essence of the
problem is to do it efficiently as 10**10 is too large

I believe a quadratic sieve is the way too go but I dont know how to do it

Anwser:
    2719288 ~ 10^7
--- 8.855929136276245 seconds ---
Exprapolating this timing, it would take me ~ 9000 sec for 10^10 This is much to slow
'''

import time, math, eulerlib
start_time = time.time()

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(n)
                break
    return max(factors)

def sieve(n):
    result = [1]*(n+1)
    result[0] = result[1] = 0
    for x in range(2, n + 1):
        if result[x] == 1:
            for y in range(x, n, x):
                result[y] = max(result[y], x)
    return result
        
    
def compute(n):
    Sieve = sieve(10**n)
    return sum([1 for x in range(len(Sieve)) if Sieve[x]*Sieve[x] < x])


    
if __name__ == "__main__":
    print(compute(7))
    print("--- %s seconds ---" % (time.time() - start_time))