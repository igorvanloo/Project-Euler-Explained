#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:17:22 2021

@author: igorvanloo
"""

'''
Project Euler Problem 120

Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, 
but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.

(a+1)^n = ∑nCk * 1^(k) * a^n-k = 1 + nC1 * a + nC2 * a^2 + ... = 1 + nC1*a mod a^2 = 1 + an mod a^2

(a-1)^n = ∑nCk * (-1)^(k) * a^n-k = (-1)^n + (-1)^n-1 * nC1 * a + (-1)^n-2 * nC2 * a^2 + ... = (-1)^n + (-1)^n-1 * nC1*a mod a^2
= (-1)^n + (-1)^n-1 * na mod a^2

therefore (a+1)^n + (a-1)^n mod a^2 = 

if n is even: 1 + an + 1 - an = 2 mod a^2
if n is odd: 1 + an - 1 + an = 2an mod a^2

if a is even, then we need an odd n such that 2an is maximised and < a^2 take n = floor(a/2) -1
if a is odd, then we need an odd n such that 2an is maximised and < a^2 take n = floor(a/2)

Anwser:
    333082500
--- 0.0003962516784667969 seconds ---
    
'''

import time, math
start_time = time.time()

def compute():
    total = 0
    for a in range(3,1000):
        if a % 2 == 0:
            total += (math.floor(a/2) - 1)* 2 * a
        else:
            total += (math.floor(a/2)) * 2 * a
            
    return total
        
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))