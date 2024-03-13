#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 01:50:43 2021

@author: igorvanloo
"""

'''
Project Euler Problem 127

a, b, c = a + b

Key points

1. Note that gcd(a + b, a) = gcd(a, b), therefore if gcd(a, b) = 1 => gcd(a, c) = gcd(b, c) = 1
2. Since a, b, c are pairwise coprime so are rad(a), rad(b), rad(c), 
    that is rad(abc) = rad(a) * rad(b) * rad(c)
3. It is faster to check if rad(abc) > c first instead of gcd(a, b) = 1, switch in checks has great speedup

Answer:
    18407904
--- 763.6556217670441 seconds ---
'''

import time, math
start_time = time.time()

### Method 1 - Using smallest prime factor sieve
def spf_sieve(N):
    #smallest prime factor sieve
    spf = [i for i in range(N + 1)]
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if spf[i] == i:
            for j in range(i*i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf
    
def compute(limit):
    spf = spf_sieve(limit + 1)
    
    def get_rad(x):
        factors = set([])
        while x != 1:
            curr = spf[x]
            factors.add(curr)
            x //= curr
            
        rad = 1
        for x in factors:
            rad *= x
        return rad
    
    rad = [0] + [get_rad(x) for x in range(1, limit + 1)]
    total = 0
    for a in range(1, limit//2 + 1):
        for b in range(a + 1, limit - a):
            c = a + b
            rad_abc = rad[a] * rad[b] * rad[c]
            if rad_abc < c:
                if math.gcd(a,b) == 1:                
                    total += c
    return total

### Method 2 - Using sieve of Eratosthenes type function to generate rad
#For some reason it is slightly slower than previous method but code looks nicer so I keep it 

def gen_rad(n):
    rad = [1]*(n + 1)
    rad[0] = 0
    rad[1] = 1
    for i in range(2, n + 1):
        if rad[i] == 1: #This is a prime
            for j in range(i, n + 1, i):
                rad[j] *= i
    return rad

def compute1(limit):
    rad = gen_rad(limit + 1)
    total = 0
    for a in range(1, limit//2 + 1):
        for b in range(a + 1, limit - a):
            c = a + b
            rad_abc = rad[a] * rad[b] * rad[c]
            if rad_abc < c:   
                if math.gcd(a,b) == 1:
                    total += c
    return total

if __name__ == "__main__":
    print(compute(120000))
    print("--- %s seconds ---" % (time.time() - start_time))