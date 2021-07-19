#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:32:54 2020

@author: igorvanloo
"""

'''
Project Euler Problem 69

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

we use the following formula φ(n) = n * product of all primes (p) that divide n (1 - 1/p)
so n /φ(n) = product of all primes (p) that divide n (1 - 1/p) so we simply need to look for the number with the most
distinct primes factors less than 1 million

Anwser:
    (5.539388020833333, 510510)
--- 198.11307215690613 seconds --- Brute force
--- 0.2077789306640625 seconds --- Using logic
     
'''

import time, math, eulerlib, itertools
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
    return list(set(factors))

def phi(n):
    total = n
    prime_factor = prime_factors(n)
    
    for p in prime_factor:
        total *= (1-1/p)
        
    return (total)

def maxprimefactors():
    total = 1
    primes = eulerlib.primes(1000)
    for i in primes:
        if total * i > 1000000:
            break
        else:
            total *= i
    return total

if __name__ == "__main__":
    print(maxprimefactors())
    print("--- %s seconds ---" % (time.time() - start_time))