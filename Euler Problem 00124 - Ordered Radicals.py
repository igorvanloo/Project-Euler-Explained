#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:06:59 2021

@author: igorvanloo
"""

'''
Project Euler Problem 124

Very simple, just create a function to find prime factors and to find rad, append them to a list, sort it and return the 9999th element
Anwser:
    (1947, 21417)
--- 2.7997658252716064 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

primes = eulerlib.primes(10**5)

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
    
def primefactorization(n, listofprimes): #Requires a preloaded list of primes
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
        return list(set(factors))

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

def rad(factors):
    totalsum = 1
    for x in factors:
        totalsum *= x
    return totalsum
    
def compute():
    finallist = []
    for x in range(1, 100000 + 1):
        finallist.append([rad(prime_factors(x)), x])
    final = sorted(finallist)
    return final[9999]
        

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))