#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:42:23 2021

@author: igorvanloo
"""

'''
Project Euler Problem 119

The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, 
and 8^3 = 512. Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two 
digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

a1 c= 81 = (8+1) ^2

Find a30.


Brute Force way, simple continue testing small numbers to the power of up to 50, and appending them to a list if the criteria
is correct, and continue till we get about 50 elements incase we skip over the intended solution, after that return the 30th
element


Anwser:
    248155780267521
--- 0.028444290161132812 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += x % 10
        x = x // 10
    return totalsum

def compute1():
    
    finallist = []
    for x in range(2,300):
        for i in range(2,50):
            if sum_digits(x**i) == x:
                finallist.append(x**i)
    final = sorted(finallist)
    return final

def compute():
    
    finallist = []
    x = 2
    while len(finallist) != 200:
        i = 2
        while i != 100:
            if sum_digits(x**i) == x:
                finallist.append((x**i))
            i += 1
        x += 1
    final = sorted(finallist)
    return final[199]
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))