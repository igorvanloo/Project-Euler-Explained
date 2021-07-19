#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:58:16 2021

@author: igorvanloo
"""

'''
Project Euler Problem 346

The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6
(i.e. 710 = 116 = 1112). In other words, 7 is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit. It can be verified that there are 8 strong 
repunits below 50: {1,7,13,15,21,31,40,43}.
Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 10**12.

Reasoning


10**12 = 0b1110100011010100101001010001000000000000
so we need not look for repunits longer than 1111111111111111111111111111111111111111

Simply look through strings 111, 1111, till 1111111111111111111111111111111111111111

We note that all repunits with base b are equal to (b**n - 1)/(b - 1), where n is the length of the base unit

So we iterate through bases till we have a base such that it exceeds our limit of 10^12

Anwser:
    336108797689259276
--- 1.0739467144012451 seconds ---
'''

import time, itertools
start_time = time.time()

def RepunitGen(base,limit):
    n = 1
    curr = 1
    reps = []
    while curr < limit:
        reps.append(int(curr))
        n += 1
        curr = (base**n - 1)/(base - 1)     
    return reps

def compute():
    overall = set()
    limit = 10**12
    for x in range(3,len("1111111111111111111111111111111111111111") + 1):
        
        value = 1
        base = 2
        while value < limit:
            overall.add(int(value))
            value = (base**x - 1)/(base - 1)
            base += 1

    total = sum((set(overall)))
    return str(total)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
