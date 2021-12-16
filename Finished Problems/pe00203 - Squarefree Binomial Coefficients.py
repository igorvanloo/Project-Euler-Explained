#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:46:45 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

in a term C(n ,k) the largest prime must be less than n, so we only need primes till 47
Just generate square numbers and loop through, numbers are very small so no need for anything special

Anwser:
    34029210557338
--- 0.0015277862548828125 seconds ---
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

def n_choose_r(n, r): #nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
    
def compute(row):
    primes = list_primes(row)
    squares = [x*x for x in primes]
    nums = set()
    for x in range(1, row):
        for y in range(0, (x+1)//2 + 1):
            term = n_choose_r(x, y)
            nums.add(term)
            #print(term)
            for sq in squares:
                if term % sq == 0:
                    nums.remove(term)
                    break
    total = 0
    for x in nums:
        total += x
        
    return total

if __name__ == "__main__":
    print(compute(51))
    print("--- %s seconds ---" % (time.time() - start_time))