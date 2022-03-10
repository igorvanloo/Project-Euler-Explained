#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:43:32 2022

@author: igorvanloo
"""

'''
Project Euler Problem 779

In a range of n numbers
There are n/2 numbers whose smallest prime divisor is 2
There are n*(1 - 1/2)(1/3) numbers whose smallest prime divisor is 3
...
There are n*(1 - 1/2)(1 - 1/3)(1 - 1/5)...(1 - 1/(p_i - 1))(1/p_i) numbers whose smallest prime divisor is p_i


How to we get this?

Inclusion-exclusion principle, lets find the amount of numbers who have 7 as their smallest prime factor
Clearly there are n/7 numbers divisble by 7, but we need to remove numbers that are divisble by 2*7, 3*7, or 5*7
so we subtract n/14, n/21, n/35, but we may have double subtracted here, as in we may have removed numbers that are multiples of 2*3*7 twice
so we must add n/42, n/30, n/105, and finally we need to subtract numbers that are divisvle by 2*3*5*7
so we subtract n/210

In total we have n/7 - n/14 - n/21 - n/35 + n/42 + n/70 + n/105 - n/210 = n/7(1 - 1/2 - 1/3 - 1/5 + 1/6 + 7/30 + 1/15 - 1/30) = n/7(4/5)(2/3)(1/2)


Now given a p_i we know how many numbers have this p_i as their smallest prime factor, let x = n*(1 - 1/2)(1 - 1/3)(1 - 1/5)...(1 - 1/(p_i - 1))(1/p_i)
We want to find from these numbers each of their p adic orders

there are (p_i - 1)/p_i^k values which have p adic order k

now bar(f_K) = lim_{N -> inf} 1/N sum_{n = 2 -> N} (alpha(n) - 1)/p(n)^K)

we reformat this to group by primes

bar(f_K) = lim_{N -> inf} 1/N sum_{p_i in primes} N*(1 - 1/2)(1 - 1/3)(1 - 1/5)...(1 - 1/(p_i - 1))(1/p_i) * sum_{k = 1 to inf} (p_i - 1)/p_i^k * (k - 1)/(p_i^K)
because for each primes there are n*(1 - 1/2)(1 - 1/3)(1 - 1/5)...(1 - 1/(p_i - 1))(1/p_i) many that have p_i as their smallest factor, and each one
that has p adic order k, adds (k-1)/(p_i^k)

This can be simplifed to 
bar(f_K) = sum_{p_i in primes} (1 - 1/2)(1 - 1/3)(1 - 1/5)...(1 - 1/(p_i - 1))(1/p_i) * sum_{k = 1 to inf} (p_i - 1)/p_i^k * (k - 1)/(p_i^K)

and sum_{k = 1 to inf} (p_i - 1)/p_i^k * (k - 1)/(p_i^K) = sum_{k = 1 to inf} (p_i - 1)(k-1)/p_i^(K + k)
= 1/(p_i^K(p_i - 1))

therefore bar(f_K) =sum_{p_i in primes} (1 - 1/2)(1 - 1/3)(1 - 1/5)...(1 - 1/(p_i - 1)) * (1/(p_i^(K+1)(p_i - 1)))

then sum_{K = 1 -> inf} bar(f_K) = sum_{K = 1 -> inf} sum_{p_i in primes} (1 - 1/2)(1 - 1/3)(1 - 1/5)...(1 - 1/(p_i - 1)) * (1/(p_i^(K+1)(p_i - 1)))

and sum_{K = 1 -> inf} (1/(p_i^(K+1)) = 1/(p_i(p_i - 1)), therefore 

sum_{K = 1 -> inf} bar(f_K) = sum_{p_i in primes} (1 - 1/2)(1 - 1/3)(1 - 1/5)...(1 - 1/(p_i - 1)) * (1/(p_i(p_i - 1)^2))


Anwser:
    0.547326103833
--- 0.3669300079345703 seconds ---
'''

import time, math
start_time = time.time()

def min_prime_factor(n):
    result = [0]*(n+1)
    result[0] = [0,0]
    result[1] = [0,0]
    for x in range(2, n + 1):
        if result[x] == 0:
            for y in range(x, n + 1, x):
                if result[y] == 0:
                    
                    power = 1
                    while y % x**(power +1) == 0:
                        power += 1
                    
                    result[y] = [x, power]
    return result

def estimate(K, number):
    values = min_prime_factor(number)
    total = 0
    
    for x in range(2, number):
        smallest_prime, p_adic_order = values[x]
        total += (p_adic_order - 1)/(smallest_prime**K)
    
    return total/number

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

def f(K):
    primes = list_primes(10**6)
    total = 0
    curr = 1
    for p in primes:
        total += curr*(1/((p**(K+1))*(p-1)))
        curr *= (p - 1)/p
    return round(total, 12)    

def sum_f():
    primes = list_primes(10**6)
    total = 0
    curr = 1
    for p in primes:
        total += curr*(1/((p*(p-1)**2)))
        curr *= (p - 1)/p
    return round(total, 12) 

if __name__ == "__main__":
    print(sum_f())
    print("--- %s seconds ---" % (time.time() - start_time))