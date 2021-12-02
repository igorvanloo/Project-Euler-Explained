#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:09:59 2021

@author: igorvanloo
"""

'''
Project Euler Problem 132

we want all p such that p|R(10^k) => p|(10^(10^k) - 1)/9 => (10^(10^k) - 1)/9 = 0 mod p

=> 10^(10^k) = 1 mod 9p, for every prime I just test the first 100 cases, not really fully understood.

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

def compute(n):
    potential_factors = set()
    
    primes = list_primes(10**n)    
    print("Primes Done")
    
    for x in primes:
        for y in range(1, 100):
            if pow(10,10**y,9*x) == 1:
                potential_factors.add(x)
                break

    return sum(primes) - sum(potential_factors)

if __name__ == "__main__":
    print(compute(5))
    print("--- %s seconds ---" % (time.time() - start_time))