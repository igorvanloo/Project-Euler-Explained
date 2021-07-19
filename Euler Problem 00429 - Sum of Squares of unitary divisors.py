#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 21:04:17 2021

@author: igorvanloo
"""

'''
Project Euler Problem 429

A unitary divisor d of a number n is a divisor of n that has the property gcd(d, n/d) = 1.
The unitary divisors of 4! = 24 are 1, 3, 8 and 24.
The sum of their squares is 12 + 32 + 82 + 242 = 650.

Let S(n) represent the sum of the squares of the unitary divisors of n. Thus S(4!)=650.

Find S(100 000 000!) modulo 1 000 000 009.

Reasoning

sum of the kth unitary divisors function phi(k)(n) is computable
if n = p1^e1 * p2^e2 * ... * pn^en, then phi(2)(n) = (1 + p1^2e1)(1+p2^2e2)...(1+pn^2en)

So if we can find the prime factorization of 100 000 000! then we can solve this problem easily

To do this we use legendres formula denoted v(p)(n!) = sum from i = 1 to infinity of floor(n/p^i) 

Anwser:
    98792821
--- 52.17203211784363 seconds ---
'''

import time, math, eulerlib
start_time = time.time()

def LegendresFormula(number):
    primes = eulerlib.primes(number)
    print("Primes done")
    print("--- %s seconds ---" % (time.time() - start_time))
    primefac = []
    
    for p in primes:
        i = 1
        count = 0
        while p**i <= number:
            count += math.floor(number/(p**i))
            i += 1
        primefac.append([p,count])
    return primefac
    
def kthUnitaryDivisorFunction(k, number):
    total = 1
    factorization = LegendresFormula(number)
    print("Factors done")
    print("--- %s seconds ---" % (time.time() - start_time))
    
    for x in factorization:
        total *= (1 + pow(x[0],k*x[1],1000000009))
        total %= 1000000009
    return total
    

if __name__ == "__main__":
    print(kthUnitaryDivisorFunction(2, 10000000))
    print("--- %s seconds ---" % (time.time() - start_time))