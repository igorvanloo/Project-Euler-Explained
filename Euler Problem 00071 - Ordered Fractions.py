#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:16:53 2020

@author: igorvanloo
"""

'''
Project Euler Problem 71

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced 
proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator 
of the fraction immediately to the left of 3/7.

Let a<b therefore there is a p/q such that p/q < a/b -> pb < aq we are looking for the largest p possible 
therefore pb <= aq - 1 -> p <= (aq-1)/b - > p = floor((aq-1)/b). So we simpyl loop through d from 1 to 1000001 and assign
n = math.floor((3*d - 1)/7) add it too a list, sorted the list and return the second last element
Anwser:
    [0.42857128571385716, 428570, 999997]
--- 1.7626428604125977 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()
            
def compute(limit):
    
    final_list = []
    
    for d in range(1,limit+1):
        n = math.floor((3*d)/7) 
        if d % 7 == 0:
            final_list.append([(n-1)/d, n-1, d])
        else:
            final_list.append([n/d, n, d])
    
    final_list = sorted(final_list)
    return final_list[-1]

if __name__ == "__main__":
    print(compute(1000000))
    print("--- %s seconds ---" % (time.time() - start_time))