#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 23:53:54 2021

@author: igorvanloo
"""
'''
Project Euler Problem 516

5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers.
Let S(L) be the sum of the numbers n not exceeding L such that Euler's totient function φ(n) is a Hamming number.
S(100)=3728.

Find S(10^12). Give your answer modulo 232.

Reasoning

Give a number n = p1^e1 * p2^e2 * ... * pk^ek
Euler totient function: phi(n) = p1^(e1-1) * (p1-1) * p2^(e2-1) * (p2-1) * ... * pk^(ek-1) * (pk-1)

A hamming number is of the form: 2^a * 3^b * 5^c

We are looking for all n from 1 till 10^12 such that phi(n) = 2^a * 3^b * 5^c

That is, phi(n) = p1^(e1-1)*(p1-1) * p2^(e2-1)*(p2-1) * ... * pk^(ek-1) * (pk-1) = 2^a * 3^b * 5^c

Now notice that if pk > 5 then phi(n) = 2^(e1+2) * 3^(e2-1) * 5^(e3-1) * ... * pk^(ek-1)*(pk-1)

Now phi(n) will only be a hamming number if pk^(ek-1)*(pk-1) is as well, but if ek > 0 then it will never be, so our only
possibility is that pk^1 is a factor of n => that if phi(n) is a hamming number then pk - 1 is a hamming number as well

We have deduced that a prime can only be a factor of n if p - 1 = 2^a * 3^b * 5^c => p = 2^a * 3^b * 5^c + 1

We can go through our list of hammining numbers add 1, and see if its a prime to find all of the remaining ones


Anwser:
    939087315
--- 162.62755703926086 seconds ---
'''

import time, math
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
    
def prime_factors_with_exponent(n):
    factors = []
    d = 2
    while n > 1:
        count = 0
        while n % d == 0:
            count += 1
            n /= d
        if count > 0:
            factors.append([d, count])
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append([int(n),1])
            break
    return factors
    
def phi(n):
    total = 1
    prime_factor = prime_factors_with_exponent(n)
    for p in prime_factor:
        total *= (p[0]**(p[1] - 1)) * (p[0] - 1)
    return int(total)

def HammingNumbers(uptillx):
    #all 5-smooth numbers are of the form 2^a * 3^b * 5^c
    numbers = []
    
    for a in range(int(math.log(uptillx, 2)) + 1):
        for b in range(int(math.log(uptillx, 3)) + 1):
            for c in range(int(math.log(uptillx, 5)) + 1):
                value = (2**a)*(3**b)*(5**c)
                if value <= uptillx:
                    numbers.append(value)
    return sorted(numbers)

def compute1(limit): #Used to test simple cases
    hamming_numbers = HammingNumbers(limit)
    total = []
    for x in range(1, limit+1):
        if phi(x) in hamming_numbers:
            total.append(x)
    return total, sum(total)
    
def compute(limit):
    hamming_numbers = HammingNumbers(limit)
    
    other_primes = [(x+1) for x in hamming_numbers if is_prime(x+1)]
    other_primes_2 = [(x+1) for x in hamming_numbers if is_prime(x+1)]
    all_numbers = set(HammingNumbers(limit))
    for x in other_primes:
        for y in other_primes_2:
            if x % y == 0:
                break
            t = x*y
            if t < limit:
                other_primes.append(t)

    for x in other_primes:
        for y in hamming_numbers:
            a = x*y
            if a > limit:
                break
            else:
                all_numbers.add(a)

    return sum(all_numbers) % 2**32

if __name__ == "__main__":
    print(compute(10**11))
    print("--- %s seconds ---" % (time.time() - start_time))
