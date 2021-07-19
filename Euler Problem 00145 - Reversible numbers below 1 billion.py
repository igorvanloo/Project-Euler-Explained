#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:16:44 2021

@author: igorvanloo
"""

'''
Project Euler Problem 145

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?

  A B C D E F G H I
+ I H G F E D C B A

2E is always even => F+D > 10nto carry a 1 over such that 2E + 1 is odd => C+G+1 is odd therefore C+G is even

A+I must be odd as it is the first digit => B+H < 10

We have now concluded that C+G is even and B+H < 10 => C+G in the second space can never be odd
Anwser:
    608720
--- 72.97345614433289 seconds ---
'''

import time
start_time = time.time()

def is_reversible(x):
    while x != 0:
        if (x % 10) % 2 != 0:
            x = x // 10
        else:
            return False
            break
    return True
            
def compute(limit):
    count = 0
    for x in range(1,(limit) + 1):
        if is_reversible(x + int(str(x)[::-1])) == True and x % 10 != 0:
            count += 1
    return count
        

if __name__ == "__main__":
    print(compute(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))