#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:49:49 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

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
    369967776 ~ 10^6 Best I could make, theoretically my code could finish in < 10 mins I think but the memory usage is way too high
--- 17.419255018234253 seconds ---
'''

import time, math
from collections import Counter

start_time = time.time()

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
    primes = list_primes(limit + 50)
    
    print("Primes done")
    print("--- %s seconds ---" % (time.time() - start_time))
    array = [0]*(limit+1)
    count = 0
    p_index = 0
    for x in range(1, limit + 1):
        
        while True:
            count += 1
            if primes[p_index] > x:
                array[x] = p_index
                break
            p_index += 1
    print("Array done")
    print("--- %s seconds ---" % (time.time() - start_time))
    
    def c(u):
        count = len(u)
        for x in u:
            if prime_gen[x]:
                count -= 1
        return count
    
    sequences = []
    
    for x in range(1, limit+1):
        if x % 100000 == 0:
            print(x)
        u = [x]
        
        while True:
            temp = array[u[-1]]
            if temp == 0:
                break
            else:
                u.append(temp)
                t = [x for x in u]
                sequences.append(t)
    print("Sequences done", len(sequences)) 
    print("--- %s seconds ---" % (time.time() - start_time))
    array2 = []
    total = 1
    for seq in sequences:
        array2.append(c(seq))
        
    print("array2 done") 
    print("--- %s seconds ---" % (time.time() - start_time))

    temp = Counter(array2)
    temp1 = list(temp.values())
    total = 1
    for x in temp1:
        total *= x
        total %= 1000000007
        
    return total % 1000000007
    
if __name__ == "__main__":
    print(P(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))