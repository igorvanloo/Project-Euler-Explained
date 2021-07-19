#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:43:04 2021

@author: igorvanloo
"""

'''
Project Euler Problem 123

Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.

Slow but simple, just go through list of primes and check, only 10**6 numbers to check

Anwser:
    21035
--- 127.54350900650024 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    primes = eulerlib.primes(10**6)
    print("Done generating primes")
    
    for x in range(len(primes)):
        if ((primes[x]-1)**x + (primes[x]+1)**x) % (primes[x])**2 > 10**10:
            break
    return x

def compute1(limit):
    p = [0] + eulerlib.primes(10**6)
    print("Done generating primes")
    
    for n in range(1,len(p),2):
        if 2*p[n]*(n) > limit:
            break
    return n
            
if __name__ == "__main__":
    print(compute1(10**10))
    print("--- %s seconds ---" % (time.time() - start_time))