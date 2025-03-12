#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:37:26 2022

@author: igorvanloo
"""
'''
Project Euler Problem 188

The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b or ba, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a^(a↑↑k).

Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987 and 3↑↑4 is roughly 10^3.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.

We can re-define this sequence x↑↑y by a(n) = x^(a(n-1)), a(0) = 1 because we notice the following

a(0) = 1
a(1) = x^a(0)
a(2) = x^a(1)
...
a(n) = x^a(n-1)

Then using pow() function we can keep track of last 8 digits

Anwser:
    95962097
--- 0.00799703598022461 seconds ---
'''
import time
start_time = time.time()

def compute(x, y, mod):
    a0 = 1
    for i in range(y):
        a1 = pow(x, a0, mod)
        a0 = a1
    return a1
        
if __name__ == "__main__":
    print(compute(1777, 1855, 10**8))
    print("--- %s seconds ---" % (time.time() - start_time))