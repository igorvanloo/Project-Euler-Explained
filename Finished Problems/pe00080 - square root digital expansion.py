#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:15:09 2020

@author: igorvanloo
"""

'''
Project Euler Problem 80

It is well known that if the square root of a natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 
475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal
 digits for all the irrational square roots.

reasoning:
    using decimal module I can get the anwser but it is not elegant 
    Instead going to use Frazer Jarvis method
    
    take n to be the number you want to find the square root of
    let a = 5n, b = 5
    now if a => b -> a = a-b, b = b+ 10
        if a < b - > a = a*100, b = b insert a 0 at the second position 
Anwser:
    40886
--- 0.03721499443054199 seconds ---
    
'''

import math, time
from decimal import *
start_time = time.time()

def is_quadratic(x):
    cube__root = (x**(1/2))
    if round(cube__root) ** 2 == x:
        return True
    return False

def frazermethod(n):
    a = 5*n
    b = 5
    while True:
        if a >= b:
            a = a-b
            b = b + 10
        else:
            a = a*100
            b = int(str(b)[0:len(str(b))-1] + str(0) + str(5))  
            
        if len(str(b)) == 110:
            break
    return str(b)[0:100]

def decimalanwser():
    total = 0
    for x in range(1,101):
        if is_quadratic(x) == False:
            temp_value = sum([int(y) for y in frazermethod(x)])
            total += temp_value
        else:
            total += 0
            
    return total
        
def frazeranwser():
    total = 0

    for x in range(1,101):
        if is_quadratic(x) == True:
            total += 0
        else:
            getcontext().prec = 105
            test = Decimal(x) ** Decimal(0.5)
            test = str(test)[0:101]
            test = test.replace(".", "0")
            
            total += sum([int(test[x]) for x in range(len(test))])
    
    return (total)

if __name__ == "__main__":
    print(frazeranwser())
    print("--- %s seconds ---" % (time.time() - start_time))