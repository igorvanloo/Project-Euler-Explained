#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:06:59 2021

@author: igorvanloo
"""
'''
Project Euler Problem 124

Very simple, just create a function to find prime factors and to find rad, append them to a list, sort it and return the 9999th element

Update: After solving 127 much faster method. From 2.5s to 0.44s

Answer:
    (1947, 21417)
--- 0.4394040107727051 seconds ---
'''

import time
start_time = time.time()

### Method 1 - Original Method ###
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(n)
            break
    return list(set(factors))

def rad(factors):
    totalsum = 1
    for x in factors:
        totalsum *= x
    return totalsum
    
def compute(limit_n, goal):
    finallist = []
    for x in range(1, limit_n + 1):
        finallist.append([rad(prime_factors(x)), x])
    final = sorted(finallist)
    return final[goal - 1]

### Method 2 - After solving 127 ###
#[1947, 21417]
#--- 0.4394040107727051 seconds ---
def gen_rad(n):
    rad = [1]*(n + 1)
    rad[0] = 0
    rad[1] = 1
    for i in range(2, n + 1):
        if rad[i] == 1: #This is a prime
            for j in range(i, n + 1, i):
                rad[j] *= i
    return rad

def compute1(limit_n, goal):
    finallist = []
    rad = gen_rad(limit_n)
    for x in range(1, limit_n + 1):
        finallist.append([rad[x], x])
    final = sorted(finallist)
    return final[goal - 1]


if __name__ == "__main__":
    print(compute(100000, 10000))
    print("--- %s seconds ---" % (time.time() - start_time))