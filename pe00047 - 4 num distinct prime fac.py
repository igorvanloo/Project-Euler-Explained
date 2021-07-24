#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:51:36 2020

@author: igorvanloo
"""

'''
Project Euler Problem 47 

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

Anwser:
    134043
--- 1.868906021118164 seconds ---
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
    return len(set(factors))

def list_primality_modified(n):
	result = [0] * (n + 1)
	result[0] = result[1] = 1
	for i in range(int((n)) + 1):
		if result[i] == 0:
			for j in range(2 * i, len(result), i):
				result[j] += 1
    
	return result
        
def compute(N, K):
    result = list_primality_modified(N)
    for x in range(1, len(result)-K):
        count = 0
        for y in range(K):
            if result[x+y] == K:
                count += 1
        if count == K:
            return x
        
if __name__ == "__main__":
    print(compute(10**6, 4))
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
    
    
    
    
    
    
    
    
    
    