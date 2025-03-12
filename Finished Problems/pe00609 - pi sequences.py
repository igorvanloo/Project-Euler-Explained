#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:49:49 2021

@author: igorvanloo
"""

'''
Project Euler Problem 609

pi(n) = number of primes not exceeding n
u = (u_0, u_1, ..., u_n)

pi sequence if 
1. u_n ≥ 1 for all n
2. u_{n+1} = pi(u_n)
3. u has more than 2 elements

c(u) = number of elements in u that are not prime
p(n,k) = the number of pi sequence such that u_0 ≤ n and c(u) = k
P(n) = product of all p(n,k) ≥ 0

First thing to notice is u is deteremined by u_0, an array with all the pi(n) may be necessary


Anwser:
    742870469 ~ 10^7
--- 24.488229036331177 seconds ---

    172023848 ~ 10^8
--- 302.72959208488464 seconds ---
--- 13.172532558441162 seconds --- with pypy
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

def P(limit):
    prime_gen = list_primality(limit + 50)
    primes = [x for x in range(len(prime_gen)) if prime_gen[x]]
    
    print("Primes done")
    print("--- %s seconds ---" % (time.time() - start_time))
    array = [0]*(limit+1)
    p_index = 0
    for x in range(1, limit + 1):
        while True:
            if primes[p_index] > x:
                array[x] = p_index
                break
            p_index += 1
    print("Array done")
    print("--- %s seconds ---" % (time.time() - start_time))
    
    array2 = [0]*(limit+1)
    for x in range(1, limit+1):
        if x % 1000000 == 0:
            print(x)
        prime_non_count = 0
        if prime_gen[x] == False:
            prime_non_count += 1
        curr = x
        while True:
            temp = array[curr]
            if temp == 0:
                break
            else:
                if prime_gen[temp] == False:
                    prime_non_count += 1
                    
            array2[prime_non_count] += 1
            curr = temp

    print("array2 done") 
    print("--- %s seconds ---" % (time.time() - start_time))

    total = 1
    for x in array2:
        if x != 0:
            total *= x
            total %= 1000000007
    return total % 1000000007

if __name__ == "__main__":
    print(P(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))