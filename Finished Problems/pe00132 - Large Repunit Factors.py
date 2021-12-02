#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:26:57 2021

@author: igorvanloo
"""

'''
Project Euler Problem 132

Not very difficult, just use the fact that R(k) = (10^k - 1)/9, then if a prime, p, divides
R(k) then (10^k - 1)/9 = 0 mod(p) => (10^k - 1) = 0 mod(9p) => 10^k = 1 mod(9p), this is simple using the pow
function in python.

Anwser:
    843296
--- 0.3167259693145752 seconds ---
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
    return factors

def compute():
    potential_factors = []
    
    primes = list_primes(10**6)
    print("Primes Done")
    
    for x in primes:
        if pow(10,10**9,9*x) == 1:
            potential_factors.append(x)
    
    total = sum(potential_factors[0:40])

    return total

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))