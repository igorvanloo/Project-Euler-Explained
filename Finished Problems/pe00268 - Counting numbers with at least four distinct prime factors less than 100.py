#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 10:33:38 2022

@author: igorvanloo
"""
'''
Project Euler Problem 268

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

We take any 4 or more primes say we have a product N of k ≥ 4 primes

Then there are 10^16/N numbers which are divisble by these k primes

However there will be overlaps,

For example 2*3*5*7 divides 2*3*5*7*11, 2*3*5*7*11*13 ...
and 2*3*5*11 divides 2*3*5*7*11, 2*3*5*7*11*13 ...

By Inclusion-exclusion principle we deduce the following

We want to find A_0 = set of all numbers ≤ 10^16 that are divisble by atleast 4 primes

    1. Let S_1 = sum of all 10**16/N such that N is a product of 4 primes
    1. Then A_1 = set of all numbers that are divisble by 4 primes = S_1 but we have overcounted numbers divisble by 5,6,7,... primes 
        so we must subtract

    2. Let S_2 = sum of all 10**16/N such that N is a product of 5 primes
    2. note that each product of 4 primes contributed the same product of 5 primes, 5C4 = 5 times, so we need to remove it 4 times
    2. Therefore we are currently at A_0 = S_1 - 4S_2
    
    3. Let S_3 = sum of all 10**16/N such that N is a product of 6 primes
    3. note that each product of 4 primes contributed the same product of 6 primes, 6C4 = 15 times
    3. note that each product of 5 primes contributed the same product of 6 primes, 6C5 = 6 times and we subtracted this 4 times
    3. Therefore we are at + 15 - 24 = -9 so we need to add this set 10 times
    3. A_0 = S_1 - 4S_2 + 10S_3
    
    3. Let S_4 = sum of all 10**16/N such that N is a product of 7 primes
    3. note that each product of 4 primes contributed the same product of 7 primes, 7C4 = 35 times
    3. note that each product of 5 primes contributed the same product of 7 primes, 7C5 = 21 times and we subtracted this 4 times
    3. note that each product of 6 primes contributed the same product of 7 primes, 7C6 = 7 times and we added this 10 times
    3. Therefore we are at + 35 - 84 + 70 = 21 so we need to subtract this set 20 times
    3. A_0 = S_1 - 4S_2 + 10S_3 - 20S_4
    
This sequence is the tetrahedral numbers with switching signs (-1)^(n + 1) * (n*(n+1)*(n+2))//6

Anwser:
    785478606870985
--- 26.579608917236328 seconds ---
'''
import time, math
from itertools import combinations
start_time = time.time()

def prod(alist):
    total = 1
    for x in alist:
        total *= x
    return total

def n_choose_r(n, r):  # nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))

def tetra(n):
    return (n*(n+1)*(n+2))//6

def compute(limit):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    total = 0
    
    for x in range(4, len(primes) + 1):
        print(x)
        curr_sum = 0
        possib = combinations(primes, x)
        for y in possib:
            curr_sum += limit//prod(y)
        
        if curr_sum == 0:
            break
        
        total += pow(-1, x - 4)*tetra(x - 3)*curr_sum
    
    return total

if __name__ == "__main__":
    print(compute(10**16))
    print("--- %s seconds ---" % (time.time() - start_time))
