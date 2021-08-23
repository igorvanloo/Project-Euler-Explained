#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:59:00 2020

@author: igorvanloo
"""

'''
Porject Euler Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

x = ak*10^k +...+ a1*10^1 + a0*10^0
we need to find when ak^5 + ... + a1^5 + a0^5 = x

Notice that 7 * 9^5 = 413343 which is a 6 digit number => any 7 digit number can never have a fifth power digit sum

We can further reduce our search because the greatest number possible to have a fifth power digit sum is 6 * 9^5 = 354294

Answer:
    443839
--- 0.6351161003112793 seconds ---
'''
import math, time

def sum_digits_mod(x, b):
    totalsum = 0
    while x != 0:
        totalsum += (x % 10)**b
        x = x // 10
    return totalsum
    
def compute(x):
    totalsum = []
    for n in range(2,354294):
        if sum_digits_mod(n, x) == n:
            totalsum.append(n)
    return totalsum
    
if __name__ == "__main__":
    start_time = time.time()
    print(compute(5))
    print("--- %s seconds ---" % (time.time() - start_time))

    
    


