#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:45:47 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

π_2(n) = sum_{k = 1 to π(sqrt(n))} π(n/p_k) - k + 1

Anwser:
    17427258
--- 15.902875900268555 seconds ---
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

def primepi(limit): #Returns an array such that array[x] = number of primes < x
    prime_gen = list_primality(limit + 50)
    primes = [x for x in range(len(prime_gen)) if prime_gen[x]]
    array = [0]*(limit+1)
    p_index = 0
    for x in range(1, limit + 1):
        while True:
            if primes[p_index] > x:
                array[x] = p_index
                break
            p_index += 1
    return array, primes

def compute(limit):
    pi, p = primepi(int(limit/2))
    sum_limit = pi[int(math.floor(math.sqrt(limit))) + 1]
    total = 0
    
    for k in range(1, sum_limit + 1):
        total += pi[int(math.floor(limit/p[k-1]))] - k + 1
    return total

if __name__ == "__main__":
    print(compute(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))