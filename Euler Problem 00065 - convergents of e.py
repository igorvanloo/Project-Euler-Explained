#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:14:30 2020

@author: igorvanloo
"""

'''
Project Euler Problem 65

we make a list, e, with all the canonical form numbers, it will of the form e[x] + 1/e[x+1]
so we what this is now the next term will be the one above, so we repeat this process backwards in the list till
the end

Anwser:
    272
--- 0.0001361370086669922 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def overall_fraction(a, numer, denom):
    return a*denom + numer, denom

def compute(limit):
    e = [2]
    i = 1
    while len(e) < limit:
        e.append(1)
        e.append(2*i)
        e.append(1)
        
        i += 1
    e = e[0:limit]
    e = e[::-1]
    numerator, denominator = 1, e[0]
    
    for x in range(1,len(e)):
        numerator, denominator = denominator, e[x]*denominator + numerator
        
    
    return sum([int(y) for y in list(str(denominator))])

if __name__ == "__main__":
    print(compute(10))
    print("--- %s seconds ---" % (time.time() - start_time))