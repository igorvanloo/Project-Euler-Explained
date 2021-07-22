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

upper bound is 10000000 as 6*9! < 10,000,000

answer:
numbers: 145, 40585
total: 40730
--- 48.246071100234985 seconds ---
'''

import time, math
start_time = time.time()

def factorial(x):
    total = 1
    if x == 0:
        return total
    else:
        for y in range(1,x+1):
            total *= y
        return total

def compute():
    
    overalltotal = []
    for x in range(3,1000000):
        str1 = str(x)
        total = 0
        for y in range(len(str1)):
            total += factorial(int(str1[y]))
        if total == x:
            overalltotal.append(x)
            print(x)
    return sum(overalltotal)
            

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))