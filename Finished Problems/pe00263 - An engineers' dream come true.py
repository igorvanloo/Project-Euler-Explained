#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:20:03 2022

@author: igorvanloo
"""
'''
Project Euler Problem 263

Practical numbers are also called panarthmetic numbers - https://oeis.org/A005153

Anwser:
    2039506520.0
--- 437.64554023742676 seconds ---
'''
import time, math
from prime_sieve.array import PrimeArraySieve

start_time = time.time()

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
        if d * d > n:
            if n > 1:
                factors.append([int(n), 1])
            break
    return factors

def is_practical(x):
    pf = prime_factors_with_exponent(x)
    if pf[0][0] != 2: 
        #Start by checking is 2 is a prime factor for completeness
        return False
    if len(pf) == 1:
        #This means 2 is the only prime factor so x = 2^e => it is practical 
        return True
    for x in range(1, len(pf)):
        p1, e1 = pf[x]
        #print(p1)
        total = 1
        for y in range(x):
            p, e = pf[y]
            if p != p1:
                total *= ((pow(p, (e + 1)) - 1)//(p - 1))  
            #print(total)
        if p1 > total + 1:
            return False  
    return True

def compute():
    limit = 10**8
    sieve = PrimeArraySieve()
    primes = sieve.primes_in_range(1, limit)
    print("primes done")
    total = 0
    count = 0
    x = 1
    while True:
        p1, p2, p3, p4= primes[x], primes[x+1], primes[x+2], primes[x+3]
        x += 1
        if limit - p1 < 1000:
            #If we reach the end of our primes
            #Generate a new set of 10^8 primes
            limit += 10**8
            primes = sieve.primes_in_range(p1 + 1, limit)
            print("next set of primes done", limit)
            x = 0
            
        if (p4 - p3 == 6) and (p3 - p2 == 6) and (p2 - p1 == 6):
            n = p1 + 9
            #sexy prime triplet has been found
            if is_practical(n - 8):
                if is_practical(n - 4):
                    if is_practical(n):
                        if is_practical(n + 4):
                            if is_practical(n + 8):
                                #engineers' paradise has been found
                                count += 1
                                total += n
                                print(n)
                                if count == 4:
                                    return int(total)
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
