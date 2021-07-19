#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:19:49 2020

@author: igorvanloo
"""

'''
Project Euler Problem 97

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of 
the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, 
have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.

Anwser:
    8739992577
--- 0.0001800060272216797 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    return ((28433 * (2**7830457)) % 10**10 + 1)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))