#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 23:14:47 2021

@author: igorvanloo
"""

'''
Project Euler Problem 618

Given all primes < the 24th Fibonnaci number = 46368
We want to find all ways to construct the integer k

let d(k, p) = sum of numbers such that the sum of their prime facorization is = k and there is no larger prime factor than p

d(0,2) = 1              d(0,3) = 1
d(1,2) = 0              d(1,3) = 0
d(2,2) = 2 (2)          d(2,3) = 2
d(3,2) = 0              d(3,3) = 3 (3)
d(4,2) = 4 (2x2)        d(4,3) = 4
d(5,2) = 0              d(5,3) = 6 (2*3)    d(5,5) = 5 (5)
d(6,2) = 8 (2*2*2)      d(6,3) = 17 (3*3)

We need to find a relation between these number because clealy the anwser for each k is the sum of the rows

One thing to notice is that we only need to deal with primes p because otherwise d(k,p) = d(k,p-1)

So what about d(k,p) when p is a prime, we an see a pattern in the first column
d(k,2) = 2*d(k-2,2) and again in the second column d(k,3) = 3*d(k-3,3)
So we have found a general relation d(k,p) = p*(k-p,p) when p is a prime

Anwser:
    634212216
--- 27.353107929229736 seconds ---
'''

import time, math, eulerlib

def sieve(n):
    result = [0] * (n+1)
    for i in range(2, int(n)+1):
        if result[i] == 0:
            for j in range(i, len(result), i):
                result[j] += i
                remainder = j/i
                while remainder % i == 0:
                    result[j] += i
                    remainder //= i
    return result

def compute1(): #Method 1, tried to make a sieve with prime divisors but quickly realised it would never be fast enough
    numbers = sieve(5*10**6)    
    total = 0
    for x in range(len(numbers)):
        if numbers[x] == 4181:
            #print(x)
            total += (x % 10**9)
    return total 

def compute(limit):
    d = [1] + [0] * limit
    primes = eulerlib.primes(limit)
    mod = 10**9
    Fibonnaci_numbers = [2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368]

    for p in primes:
        for i in range(p,limit+1):
            d[i] += (p*d[i-p] % mod)
    
    total = 0
    for x in Fibonnaci_numbers:
        total += (d[x] % mod)
        
    return total % mod
        
if __name__ == "__main__":
    start_time = time.time()
    #print(compute1())
    print(compute(46368))
    print("--- %s seconds ---" % (time.time() - start_time))