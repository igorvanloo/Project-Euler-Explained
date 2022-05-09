#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:50:58 2022

@author: igorvanloo
"""

'''
Project Euler Problem 160

Clearly trailing zeroes is deteremined by number of 5s and 2s but there are way more 2s than 5s
so we only need to consider number of 5s.

16576 is the answer accoridng to wolframalpha

Anwser:

'''
import time, math
start_time = time.time()

def trailing_zeros(x):
    total = 0
    for i in range(1, int(math.floor(math.log(x, 5))) + 1):
        total += int(math.floor(x / (5 ** i)))
    return total

def fact_mod(n, mod):
    total = 1
    for x in range(2, n + 1):
        total *= x
        total %= mod
    return str(total % mod)

def compute(n):
    zeroes = trailing_zeros(n)
    return fact_mod(n, 10**(5 + zeroes))[:-zeroes]

if __name__ == "__main__":
    print(compute(20))
    print("--- %s seconds ---" % (time.time() - start_time))