#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:23:33 2022

@author: igorvanloo
"""
'''
Project Euler Problem 251

Simplifying using wolframalpha we get c = (a + 1)^2(8a - 1)/27b^2

Take note of the case b = 0.
If b = 0 => 2a^(1/3) = 1 => a = 1/8 which is not an integer. Therefore b > 0

Now note that b^2 | (a + 1)^2(8a - 1)/27 therefore we require
(a + 1)^2(8a - 1) = 0 (mod 27) which has solutions a = 3k + 2

Therefore, we have b^2 | 27(1 + k)^2 (5 + 8k) = (a + 1)^2(8a - 1)

Generate (a + 1)^2(8a - 1) and find all of its b^2 divisors

We want a + b + c <= limit

Fix k, a = 3k + 2 therefore b^2c = (1 + k)^2 (5 + 8k)

Anwser:
    18946051
--- 6404.355103492737 seconds ---
'''
import time

start_time = time.time()

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                factors[n] = 1
            break
    return factors

def gen_multiples(primes, multiplicities, limit):
    if len(primes) == 0:
        return []
    p = 1
    multiples = []
    for i in range(multiplicities[0] + 1):
        if p > 1:
            multiples.append(p)
            
        if len(primes) > 1:
            for x in gen_multiples(primes[1:], multiplicities[1:], limit//p):
                if p*x < limit:
                    multiples.append(p*x)
        
        p *= primes[0]
        
    return multiples

def get_sq_divisors(a, limit):
    pf1 = prime_factors((a + 1)//3)
    pf2 = prime_factors((8*a - 1)//3)
    
    pf = {}
    for p in pf1:
        pf[p] = 2*pf1[p]
    for p in pf2:
        pf[p] = pf2[p] + pf.get(p, 0)
    
    primes = []
    multiplicities = []
    for p, e in pf.items():
        mult = e//2
        if mult > 0:
            primes.append(p)
            multiplicities.append(mult)
    
    return [x for x in gen_multiples(primes, multiplicities, limit)]

def compute(limit):
    total = 0
    klimit = int((limit - 2)/6.77)
    for k in range(klimit + 1):
        a = 3*k + 2
        t = ((a + 1)*(a + 1)*(8*a - 1))//27
        for b in [1] + get_sq_divisors(a, t):
            c = t//(b*b)
            v = a + b + c
            if v <= limit:
                total += 1
    return total
        
if __name__ == "__main__":
    print(compute(1000000))
    print("--- %s seconds ---" % (time.time() - start_time))
