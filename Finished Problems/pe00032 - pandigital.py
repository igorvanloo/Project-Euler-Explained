#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:41:51 2020

@author: igorvanloo
"""

'''
Project Euler problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

99*99 = 9801 < 10000 therefore must be atleast 2 digit times 3 digit or 1 digit times 4 digit

anwser:
    [5796, 5346, 4396, 7254, 7632, 6952, 7852]
45228
--- 0.1733839511871338 seconds ---

'''
import time
start_time = time.time()

def compute():
    testlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    values = set()
    for x in range(9,99):
        for y in range(99,999):
            answer = x*y
            if answer < 10000:
                testingvalue = sorted(str(x) + str(y) + str(answer))
                if testingvalue == testlist:
                    values.add(answer)
    
    for x in range(1,9):
        for y in range(999,9999):
            answer = x*y
            if answer < 10000:
                testingvalue = sorted(str(x) + str(y) + str(answer))
                if testingvalue == testlist:
                    values.add(answer)
    print(values)
    return sum(values)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
                
    
        