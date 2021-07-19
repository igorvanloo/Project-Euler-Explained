#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:41:14 2020

@author: igorvanloo
"""

'''
Project euler problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

answer:
    
    [[16, 64], [19, 95], [26, 65], [49, 98]]
100.0
--- 0.0027740001678466797 seconds ---
'''

import time
start_time = time.time()

def func1():
    values = []
    for x in range(10,100):
        for y in range(10, 100):
            if x/y < 1 and x%10 != 0 and y%10 != 0:
                value1 = str(x)
                value2 = str(y)
                if value1[0] == value2[1] or value1[1] == value2[0]:
                    if x/y == int(value1[1])/int(value2[0]) or x/y == int(value1[0])/int(value2[1]):
                        values.append([x,y])
    print(values)
    return values

def compute():
    test_list = func1()
    denominator = 1
    for x in range(len(test_list)):
        denominator *= test_list[x][1]/test_list[x][0]
    return denominator
        
                


if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))