#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:22:15 2021

@author: igorvanloo
"""

'''
Project Euler Problem 148

Brute forced at first using a smart primality checking trick a^(p-1) = 1 mod p, we can use a = 2
because we know n must be even (otherwise you get an odd number)

In order to speed it up I made the following observations

n mod 2 = 0

n mod 3 ≠ 0
Because n^2 + 3 mod 3 = n^2 mod 3 , Therefore if n mod 3 = 0 => n^2 mod 3 = 0 => n^2 + 3 mod 3 = 0 => n^2 + 3 is not prime

n mod 5 = 0
If n mod 5 ≠ 0 then n^2 mod 5 = 1,2,3,4
n^2 + 9 mod 5 = 0 if n^2 mod 5 = 1
n^2 + 3 mod 5 = 0 if n^2 mod 5 = 2
n^2 + 7 mod 5 = 0 if n^2 mod 5 = 3
n^2 + 1 mod 5 = 0 if n^2 mod 5 = 4

n mod 7 ≠ 0

Anwser:
    676333270
--- 30.911648988723755 seconds ---
'''

import time
start_time = time.time()
    
def compute(limit):
    total = 0
    candidate = []
    for n in range(10,limit,10):
        if n % 7 == 3 or n % 7 == 4:
            if n % 3 != 0:
                if pow(2,n**2, n**2 + 1) == 1:
                    candidate.append(n)

       
    for n in candidate:
        if pow(2,n**2 + 2, n**2 + 3) == 1:
            if pow(2,n**2 + 6, n**2 + 7) == 1:
                if pow(2,n**2 + 8, n**2 + 9) == 1:
                    if pow(2,n**2 + 12, n**2 + 13) == 1:
                        if pow(2,n**2 + 26, n**2 + 27) == 1:
                            if pow(2,n**2 + 20, n**2 + 21) != 1:
                                total += n
    return total

if __name__ == "__main__":
    print(compute(150000000))
    print("--- %s seconds ---" % (time.time() - start_time))