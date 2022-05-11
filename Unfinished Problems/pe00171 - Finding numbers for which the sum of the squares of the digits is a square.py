#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 12:03:04 2022

@author: igorvanloo
"""
'''
Project Euler Problem 

The maximum square is 20*9^2 = 1620

My idea is to use all possible squares up to that point and then partition them into sum of other squares

Through trial and error I found that 
partition1(n, 0, 0, d) = 
    "0" + partition1(n - 1, 0, 0, d)
    "1" + partition1(n - 1, 0, 0, d - 1)
    "2" + partition1(n - 4, 0, 0, d - 1)
    "3" + partition1(n - 9, 0, 0, d - 1)
    "4" + partition1(n - 16, 0, 0, d - 1)
    "5" + partition1(n - 25, 0, 0, d - 1)
    "6" + partition1(n - 36, 0, 0, d - 1)
    "7" + partition1(n - 49, 0, 0, d - 1)
    "8" + partition1(n - 64, 0, 0, d - 1)
    "9" + partition1(n - 81, 0, 0, d - 1)

Anwser:

'''
import time, math
from functools import cache
start_time = time.time()

@cache
def partition1(n, idd, digits, max_digits):
    
    partitions = []
    
    if n == 0:
        return [idd]
    
    if n < 0:
        return []
    
    if digits > max_digits - 1:
        return []
    
    for x in range(0, int(math.sqrt(n)) + 1):
        
        partitions += partition1(n - x*x, idd + x*(10**digits), digits + 1, max_digits)
    
    return partitions

if __name__ == "__main__":
    print(partition1(9, 0, 0, 1))
    print("--- %s seconds ---" % (time.time() - start_time))
