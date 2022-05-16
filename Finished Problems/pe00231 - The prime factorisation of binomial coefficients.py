#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:55:31 2022

@author: igorvanloo
"""
'''
Project Euler Problem 231

A choose b = a!/b!(a-b)!

We find prime factorisation of a, b and a-b, and we divide

Anwser:
    7526965179680
--- 9.060504913330078 seconds ---
'''

import time, math
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def compute(a, b):
    primes = list_primes(a)
    
    def legendre_factorial(x):
        prime_fac = {}
        for y in primes:
            total = 0
            for i in range(1, int(math.floor(math.log(x, y))) + 1):
                total += int(math.floor(x / (y ** i)))
            prime_fac[y] = total
        return prime_fac
    
    prime_fac_a = legendre_factorial(a)
    prime_fac_b = legendre_factorial(b)
    prime_fac_ab = legendre_factorial(a-b)
    
    for x in prime_fac_b:
        prime_fac_a[x] -= prime_fac_b[x]
        
    for y in prime_fac_ab:
        prime_fac_a[y] -= prime_fac_ab[y]
    
    return sum(prime_fac_a[x]*x for x in prime_fac_a)
        
if __name__ == "__main__":
    print(compute(20000000, 15000000))
    print("--- %s seconds ---" % (time.time() - start_time))


