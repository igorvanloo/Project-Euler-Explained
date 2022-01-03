#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:46:35 2020

@author: igorvanloo
"""

'''
Project euler problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

Reasoning

9! = 362880 is the largest one digit can contribute => 8*9! = 2903040 is the largest possible because this is a 7 digit number

Answer:
Numbers: 145, 40585
    40730
--- 2.839172124862671 seconds ---
'''

import time, math
start_time = time.time()

def sum_digits_mod(x):
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    totalsum = 0
    while x != 0:
        totalsum += facts[x % 10]
        x = x // 10
    return totalsum

def compute():
    overalltotal = 0
    for x in range(3,2903040):
        if sum_digits_mod(x) == x:
            overalltotal += x
    return (overalltotal)
            
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))