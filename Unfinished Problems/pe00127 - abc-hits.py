#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 01:50:43 2021

@author: igorvanloo
"""

'''
Project Euler Problem 127

Got correct answer for test case, but it is too slow to finish


Anwser:
    12523 ~ 1000
--- 3.4965250492095947 seconds ---
'''

import time, math, eulerlib

def prime_factors(n):
    factors = set()
    d = 2
    while n > 1:
        while n % d == 0:
            factors.add(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.add(n)
            break
    total = 1
    for x in factors:
        total *= x
    return int(total)

def compute(limit):
    total = 0
    for a in range(1, limit):
        for b in range(a+1, limit):
            if a + b > limit:
                break            
            else:
                if math.gcd(a,b) == 1:
                    c = a + b
                    if math.gcd(a,c) == 1:
                        if math.gcd(b,c) == 1:
                            if prime_factors(a*b*c) < c:
                                total += c
    return total

if __name__ == "__main__":
    start_time = time.time()
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))