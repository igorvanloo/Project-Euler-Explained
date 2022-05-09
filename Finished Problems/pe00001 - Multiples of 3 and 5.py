#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:42:57 2021

@author: igorvanloo
"""

'''
Project Euler Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer:
    233168
--- 0.00019812583923339844 seconds ---
    
'''

import time, math
start_time = time.time()

def compute(limit):
    total = 0
    for x in range(1,limit):
        if x % 3 == 0:
            total += x
        if x % 5 == 0:
            total += x
        if x % 15 == 0:
            total -= x
    return total

if __name__ == "__main__":
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))