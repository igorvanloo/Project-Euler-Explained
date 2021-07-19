#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:26:54 2020

@author: igorvanloo
"""

'''
Project Euler Problem 72

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a 
reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

We are looking for all he proper reduced fractions of all numbers from 1, 1000000, in short all numbers n/d
where gcd(n,d) = 1 and n<d. This is the exact definition of Eulers Totient Function

Anwser:
    303963552391
--- 37.85697412490845 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

#primes = eulerlib.primes(1000000)


def primefactorization(n, listofprimes):
    if is_prime(n) == True:
        return [n]
    else:
        factors = []
        while n != 1:
            for x in listofprimes:
                if n % x == 0:
                    factors.append(x)
                    n = n/x
                    break
        return set(factors)

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

def is_prime(x): #Test if giving value is a prime 
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True

def phi(n):
    total = n
    prime_factor = prime_factors(n)
    
    for p in prime_factor:
        total *= (1-1/p)
        
    return int(total)

def compute():
    total = 0
    for x in range(2,50000+1):
        if x % 10000 == 0:
            print(x)
        total += phi(x)
    return total

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))