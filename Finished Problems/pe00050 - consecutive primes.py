#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:37:42 2020

@author: igorvanloo
"""

'''
Project Euler Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Reasoning 

After 546 primes we go over million therefore this is out limit

Anwser:
    [543, 997651]
--- 0.5129101276397705 seconds ---
'''

import time, math, eulerlib, itertools
start_time = time.time()

def is_prime(x):
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

def maximum(): #To find limit
    primes = eulerlib.primes(10**7 * (9/16))
    maximum = 0
    for x in range(len(primes)):
        maximum += primes[x]
        if maximum > 10**12:
            return x
    
def compute(limit):
    primes = eulerlib.primes(4000)
    consecutive_primes = []
    for y in range(546):
        total = 0
        count = 0
        for x in range(y+1,546):
            total += primes[x]
            count += 1
            if total > limit:
                break
            elif is_prime(total) == True:
                consecutive_primes.append([count, total])
    return max(sorted(consecutive_primes))
            

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))