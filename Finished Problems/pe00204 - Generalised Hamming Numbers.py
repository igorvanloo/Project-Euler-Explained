#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:39:43 2022

@author: igorvanloo
"""
'''
Project Euler Problem 204

I use my k_smooth_numbers function from problem 581

Anwser:
    2944730
--- 6.198620319366455 seconds ---
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

def k_smooth_numbers(max_prime, limit):
    k_s_n = [1]
    p = list_primes(max_prime)
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
    return len(k_s_n)

if __name__ == "__main__":
    print(k_smooth_numbers(100, 10**9))
    print("--- %s seconds ---" % (time.time() - start_time))
