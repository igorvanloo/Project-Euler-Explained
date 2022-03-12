#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:09:00 2022

@author: igorvanloo
"""
'''
Project Euler Problem 581

A number is p-smooth if it has no prime factors larger than p.
Let T be the sequence of triangular numbers, ie T(n)=n(n+1)/2.
Find the sum of all indices n such that T(n) is 47-smooth.

https://en.wikipedia.org/wiki/St%C3%B8rmer%27s_theorem tells us that there is an upper bound,
the largest 47 smooth number is 1109496723126, found from https://oeis.org/A117581

After that I just generate all 47-smooth numbers under this limit and I go through the list

Anwser:
    (2227616372734, 1502)
--- 24.79506015777588 seconds ---
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

def k_smooth_numbers(primes, limit):
    k_s_n = [1]
    p = primes
    while len(p) != 0:
        temp_k_s_n = []
        curr_p = p.pop(0)
        power_limit = int(math.log(limit, curr_p)) + 1
        curr_multiples = [curr_p**x for x in range(1, power_limit + 1)]
        for x in curr_multiples:
            for y in k_s_n:
                temp = x*y
                if temp <= limit:
                    temp_k_s_n.append(temp)
        k_s_n += temp_k_s_n
    return sorted(k_s_n)
    
def compute(max_prime):
    primes = list_primes(max_prime)
    limits = [2, 9, 81, 4375, 9801, 123201, 336141, 11859211, 11859211, 177182721, 1611308700, 3463200000, 63927525376, 421138799640, 1109496723126]
    if len(primes) == 15:
        limit = limits[-1]
    else:
        limit = limits[len(primes)]
        
    possib = k_smooth_numbers(primes, limit)
    print("Done generating " + str(max_prime) + "-smooth-numbers")
    total = 0
    count = 0
    for x in range(len(possib)-1):
        curr = possib[x]
        next_ = possib[x+1]
        if curr + 1 == next_:
            count += 1
            total += curr
    return total, count

if __name__ == "__main__":
    print(compute(47))
    print("--- %s seconds ---" % (time.time() - start_time))
