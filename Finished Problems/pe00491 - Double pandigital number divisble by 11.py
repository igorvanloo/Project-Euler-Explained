#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:03:46 2021

@author: igorvanloo
"""

'''
Project Euler Problem 491

A number is divisble by 11 if the alternating sum is
Take 90908181727263635454 then we have 
9+9+8+8+7+7+6+6+5+5 = 70
4+4+3+3+2+2+1+1+0+0 = 20

The total sum is 90

If we have the sum of one set of the 10 numbers, say S, the then the other set has sum 90 - S
Therefore if 11|n => 11|S - (90-S) = 11|2S - 90

For each combination of 10, we can re-arrange the remaining numbers based on the number of zero's there are

Anwser:
    194505988824000
--- 0.03388333320617676 seconds ---
'''

import time, math, itertools
start_time = time.time()

def number_of_doubles(pand):
    doubles = 0
    for x in range(0,10):
        if pand.count(str(x)) == 2:
            doubles += 1
    return doubles
    
def compute():
    total = 0
    poss = set(itertools.combinations("00112233445566778899", 10))
    fac_9 = int(math.factorial(9))
    fac_10 = int(math.factorial(10))
    for x in poss:
        zero_count = x.count('0')
        x_count = sum([int(y) for y in x])
        
        if zero_count == 0:
            if (2*x_count - 90) % 11 == 0:
                num_doubles = number_of_doubles(x)
                total += (fac_10/(2**num_doubles))*(fac_10/(2**num_doubles))
        
        if zero_count == 1:
            if (2*x_count - 90) % 11 == 0:
                num_doubles = number_of_doubles(x)
                total += (9*fac_9/(2**num_doubles))*(fac_10/(2**num_doubles))
        
        if zero_count == 2:
            if (2*x_count - 90) % 11 == 0:
                num_doubles = number_of_doubles(x)
                total += (8*fac_9/(2**num_doubles))*(fac_10/(2**num_doubles))
    return int(total)
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))