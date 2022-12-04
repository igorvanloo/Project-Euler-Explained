#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 00:37:34 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

n is Cube full means that if for every prime, p, that divides n then p^3 also divides n

=> n = p_1^(3e_1) * p_2^(3e_2) * ...

Note that (2*3*5*7*11*13*17*19)**3 > 10**18 so we have a maximum of 8 prime factors

The largest p must be less than 10^6 for all of our numbers

https://oeis.org/A036966

It is clear that S(n)/n converges as the answer if n = 10**x then S(10**x) = 1.339 * 10**x why is this so?

S(n) = sum_{1 <= cube full i <= n} floor(n/i)
lim as n goes to inf S(n)/n = lim n goes to inf 1/n sum_{1 <= cube full i <= n} floor(n/i) we interchange 
the summation and lim as the sequence is bounded above by their limit therefore we have

lim n goes to inf S(n)/n = sum_{1 <= cube full i} lim n goes to inf 1/n * floor(n/i) = 
 = sum_{1 <= cube full i} 1/i = prod_{primes p} (1 + 1/p^3 + 1/p^4 + ...) = prod_{primes p} (1 + 1/(p^2(p-1)))
which converges!!
 

Anwser:
    1339784153569958487
--- 128.59608364105225 seconds ---
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

def S(n):
    primes = list_primes(int(n**(1/3)) + 1)
    pp = [1] # Prime Powers: p^3 ,p^4, ... up till limit for all primes
    for p in primes:
        x = pow(p, 3)
        while x <= n:
            pp.append(x)
            x *= p
    
    pp = sorted(pp)
    d = []
    l = len(pp)
    for x in range(l):
        for y in range(l):
            v = pp[x]*pp[y]
            if v > n:
                break
            else:
                d.append(pp[x]*pp[y])
                
    d = sorted(set(d))
    d1 = []
    for x in range(len(d)):
        for y in range(len(d)):
            v = d[x]*d[y]
            if v > n:
                break
            else:
                d1.append(d[x]*d[y])
                
    d1 = sorted(set(d1))
    d2 = []
    for x in range(len(d1)):
        for y in range(len(d1)):
            v = d1[x]*d1[y]
            if v > n:
                break
            else:
                d2.append(d1[x]*d1[y])
    d2 = set(d2)
    
    total = 0
    for x in d2:
        total += n//x
    
    return total

def S_estimate(n):
    primes = list_primes(n)
    total = 1
    for p in primes:
        total *= (1 + 1/(pow(p,3) - pow(p, 2)))
    
    return total
    
if __name__ == "__main__":
    print(S(10**18))
    print("--- %s seconds ---" % (time.time() - start_time))