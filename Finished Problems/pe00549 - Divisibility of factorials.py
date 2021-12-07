#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:25:50 2021

@author: igorvanloo
"""

'''
Project Euler Problem 549

s(n) is the smallest number m such that n divides m!

now n = p_1^e_1 * p_2^e_2 * ...
m! = 1*2*3*...*m = 2*3*(2^2)*5*(2*3)...

so the smallest m! that is divisible by n is the first m! that contains the same number of prime factors as n

Legendres formula states that m! has sum from i = 1 to inf floor(m/x) x's in it's prime decomposition
see: https://en.wikipedia.org/wiki/Legendre%27s_formula

This means if we have an n say 10, then 10 = 2*5
=> m/2 ≥ 1 and m/5 ≥ 1 => m = 5

n = 25 = 5*5
=> m/5 ≥ 2 => m = 10

In general I notice that the largest prime usually dominates the rest of the other terms but not always
For example 6720 = 2*2*2*2*2*2*3*5*7 and the first m for which 6720/m! is 8

The 7 tells us that m ≥ 7, however the key here is 2*2*2*2*2*2 = 2^6 using legendres again this means 
floor(m/2) + floor(m/4) + floor(m/8) ≥ 6 (note we do not include floor(m/16) becuase then m ≥ 16 which is far too large)
if floor(m/4) = 1 => floor(m/2) = 2
if floor(m/4) = 2 => floor(m/4) = 4 this sum is 6 but we also have floor(m/8) = 1 because if floor(m/4) = 2 => m ≥ 8
There 8 is the first number which satisifies the required number of 2's

So we can deduce that s(n) = max{s(p_1^e_1), s(p_2^e_2), ...} where n = p_1^e_1 * p_2^e_2 * ...

Essentially if we can quickly compute s(p^e), this problem should become easier 
if e = 1 then s(p) = p
if e = 2 then m! has 2 p's in it, first one will be at position p iteself and the next will definietly be at a multiple of p
so we can quickly search like that

Anwser:
    476001479068717
--- 234.5322027206421 seconds ---
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

def prime_factors_with_exponent(n): #Returns all the prime factors along with their exponent
    factors = []
    d = 2
    while n > 1:
        count = 0
        while n % d == 0:
            count += 1
            n /= d
        if count > 0:
            factors.append([d,count])
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append([int(n),1])
            break
    return factors

def legendre_factorial(x): #Coded this but in the end was not very useful
    primes = list_primes(x)
    
    prime_fac = []
    exponent = []

    for y in primes:
        total = 0
        for i in range(1, int(math.floor(math.log(x,y))) + 1):
            total += int(math.floor(x/(y**i)))
            
        prime_fac.append(y)
        exponent.append(total)
    return prime_fac, exponent


def s(alist,limit): #A quick function for calculating s(p^e)
    p, e = alist
    if e == 1:
        return p
    
    c = 0
    while math.factorial(c*p) % (p**e) != 0:
        c += 1
    return c*p

def compute2(limit): #First draft of the function, went up to 10^5 in 50 seconds
    total = 0
    array = [0]*(limit + 1)
    
    for x in range(2, limit +1):
        fac = prime_factors_with_exponent(x)
        temp = []
        for y in fac:
            p, e = y
            if array[p**e] == 0:
                array[p**e] = s(y, limit)
            temp.append(array[p**e])
        total += max(temp)
    return total

def compute1(limit): #Second draft, got up to 10**6 in 30 seconds it cuts out a lot of useless calculations and tries
                     #to re-use a lot of already calculated stuff
    primes = list_primes(limit)
    array = [0]*(limit + 1)
    for a in range(len(primes)):
        p = primes[a]
        for e in range(1, int(math.floor(math.log(limit, p))) + 1):
            array[p**e] = s([p,e], limit)
    
    for x in range(2, limit + 1):
        if array[x] == 0:
            fac = prime_factors_with_exponent(x)
            temp = []
            for y in fac:
                temp.append(s(y, limit))
            array[x] = max(temp)
            
    return sum(array)

def compute(limit): #Final version, essentially a sieve, first I calculate all the primes and their powers and then I sieve all the remaining values
                    #I could definitely increase the speed by making the entire program a sieve, mabye another time
    primes = list_primes(limit)
    prime_power_array = [0]*(limit + 1)
    for a in range(len(primes)):
        p = primes[a]
        for e in range(1, int(math.floor(math.log(limit, p))) + 1):
            prime_power_array[p**e] = s([p,e], limit)
    
    array = [0]*(limit + 1)
    
    for x in range(len(prime_power_array)):
        if prime_power_array[x] != 0:
            for y in range(1, int(limit/x) + 1):
                
                array[y*x] = max(array[y*x], prime_power_array[x])
    
    return sum(array)
    
if __name__ == "__main__":
    print(compute(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))