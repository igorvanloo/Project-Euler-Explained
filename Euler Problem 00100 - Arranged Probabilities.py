#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:45:51 2021

@author: igorvanloo
"""

'''
Project Euler Problem 100

Arranged Probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were 
taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box 
containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of 
blue discs that the box would contain.

blue = b
red = r
n = b + r
1/2 = b/n * (b-1)/(n-1))
1/2 = b(b-1)/(n)(n-1)
2b^2 - b - n^2 + n = 0

Anwser:
    (756872327473, 1070379110497)
--- 0.00057220458984375 seconds ---
        
'''

import time
start_time = time.time()

def compute(limit):
    b = 15
    n = 21
    while n < limit:
        btemp = 3*b + 2*n -2
        ntemp = 4*b + 3*n -3
        #print(btemp, ntemp)
        b = btemp
        n = ntemp
    return b, n
        
if __name__ == "__main__":
    print(compute(10**3))
    print("--- %s seconds ---" % (time.time() - start_time))