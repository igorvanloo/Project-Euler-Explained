#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:02:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 668

A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
Including the number 1, there are 29 square root smooth numbers not exceeding 100.

How many square root smooth numbers are there not exceeding 10 000 000 000?

Reasoning

If we find the greatest prime factor of a number we can easily decide whether it is square root smooth, The essence of the
problem is to do it efficiently as 10**10 is too large

I believe a quadratic sieve is the way too go but I dont know how to do it

https://oeis.org/A063539
https://oeis.org/A064775 - I found something interesting from this one

Theorem: a(n) = n - Sum_{i=1..floor(sqrt(n))} (pi(floor(n/i)) - pi(i)), which isn't too difficult 

x is not square-root-smooth iff x = py where p is a prime and y ≤ p
Reason: x = py ≤ p^2 => sqrt(x) ≤ p 

Now we want to find all non-square-root-smooth numbers x ≤ n
The range for y is 1 ≤ y ≤ sqrt(n) because if y > sqrt(n) then p ≥ sqrt(n) => py = n > n which is absurd

Now given a y, then p = x/y therefore there are π(n/y) primes that are possible, however there are π(y-1) primes
that are not allowed because these primes would be less than y, which is not allowed

So therefore we have the number of non-square-root-smooth numbers x ≤ n = sum_{y=1 to sqrt(n)} π(n/y) - π(y-1)

Anwser:
    2811077773
--- 412.0572929382324 seconds ---
'''

import time, math
from sympy import primepi
start_time = time.time()

def max_prime_factor(n): #https://oeis.org/A006530
    result = [1]*(n+1)
    result[0] = result[1] = 0
    for x in range(2, n + 1):
        if result[x] == 1:
            for y in range(x, n + 1, x):
                result[y] = max(result[y], x)
    return result

def compute1(limit): #Worked up to 10^7 then became too slow
    Sieve = max_prime_factor(limit)
    total = 0
    for x in range(len(Sieve)):
        y = Sieve[x]
        if y*y < x:
            total += 1
    return total
            
def compute(n):
    total = 0
    for i in range(1, int(math.sqrt(n))):
        total += (primepi(int(math.floor(n/i))) - primepi(i-1))
    return n - total

if __name__ == "__main__":
    print(compute(10**9))
    print("--- %s seconds ---" % (time.time() - start_time))