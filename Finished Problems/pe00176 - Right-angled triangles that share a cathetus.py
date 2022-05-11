#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:24:16 2022

@author: igorvanloo
"""

'''
Project Euler Problem 176

2*47547 + 1 = 95095 = 5 * 7 * 11 * 13 * 19
Uisng formula (2e_1 - 1)(2e_2 + 1)... we get
n = 2^10 * 3^6 * 5^5 * 7^3 * 11^2 = 96818198400000

Anwser:
    96818198400000
'''
import time
start_time = time.time()

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

if __name__ == "__main__":
    print(2**10 * 3**6 * 5**5 * 7**3 * 11**2)
    print("--- %s seconds ---" % (time.time() - start_time))