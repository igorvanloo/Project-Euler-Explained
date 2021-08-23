#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:55:24 2020

@author: igorvanloo
"""

'''
Project Euler Problem 73

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a 
reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

Anwser:
    7295372
--- 8.89788818359375 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    
    final_list = []
    
    for n in range(1,12001):

        for d in range(12000, n, -1):
            
            if 1/3 < n/d < 1/2:
                final_list.append(n/d)
    
    final_list = set(final_list)
    return len(final_list)

def compute1():
    
    count = 0    
    for n in range(1,12001):

        for d in range(12000, n, -1):
            
            if math.gcd(n,d) == 1 and 1/3 < n/d < 1/2:
                count += 1
    
    return count

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))