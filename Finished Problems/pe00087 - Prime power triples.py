#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 22:32:51 2021

@author: igorvanloo
"""

'''
Project Euler Problem 87

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

Reasoning:
    First ill test to see which primes number is the closest when squared, cubed, and 4th powered
    7069^2 = 49970761
    367^3 = 49430863
    83^4 = 47458321
    
    so we can create a simple loop and add up all the numbers that are less than 50,000,000
    
Anwser:
    1097343
--- 1.5371170043945312 seconds ---
    
'''

import time
from eulerlib import primes
start_time = time.time()

def compute():
    squared_prime_numbers = primes(7070)
    cubed_prime_numbers = primes(368)
    fourth_prime_numbers = primes(84)
    numbers = []
    
    for x in squared_prime_numbers:
        for y in cubed_prime_numbers:
            for z in fourth_prime_numbers:
                anw = x**2 + y**3 + z**4
                if anw < 40000000:
                    numbers.append(anw)
                    
    return len(set(numbers))
                

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))