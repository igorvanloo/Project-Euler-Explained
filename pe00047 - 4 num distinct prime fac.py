#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:51:36 2020

@author: igorvanloo
"""

'''
Project Euler Problem 47 

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

Anwser:
    134043
    --- 1.868906021118164 seconds ---
'''

import time, math, eulerlib, itertools
start_time = time.time()

def npf(x):
    i = 2
    a = set()
    while i < x**0.5 or x == 1:
        if x % i == 0:
            x = x/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a) + 1)
    
def Prime_fac(x):
    i = 2
    a = []
    while i < x**0.5 or x == 1:
        if x % i == 0:
            x = x/i
            a.append(i)
            i -= 1
        i += 1
    a.append(int(x))
    return a

def prime_factorization(x):
    number = x
    prime_factors = []
    possible_prime_factors = eulerlib.primes(x)
    while number != 1:
        
        
        for y in range(len(possible_prime_factors)):
            if number % possible_prime_factors[y] == 0:
                prime_factors.append(possible_prime_factors[y])
                number = number / possible_prime_factors[y]
    return prime_factors
        
def compute():
    count = 0
    x = 2*3*5*7
    a = 1
    
    while count != 4:
        if npf(x) != 4:
            x += 1
            count = 0
        else:
            count += 1
            x += 1
    return x-4
    

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
    
    
    
    
    
    
    
    
    
    