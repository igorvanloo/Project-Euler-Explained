#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:46:15 2020

@author: igorvanloo
"""

'''
Project Euler Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is 
almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of 
the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

Anwser:
    972
--- 0.10810613632202148 seconds --- 
'''

import time
start_time = time.time()

def compute():
    maximum = 0
    for a in range(2,100):
        for b in range(1,100):
            x = a**b
            temp_var = sum([int(y) for y in list(str(x))])
            if temp_var > maximum:
                maximum = temp_var
    return maximum

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))