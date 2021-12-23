#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:55:34 2021

@author: igorvanloo
"""

'''
Project Euler Problem 


For fixed integers a, b, c, define the crazy function F(n) as follows:
F(n) = n - c for all n > b
F(n) = F(a + F(a + F(a + F(a + n)))) for all n ≤ b.

Also, define S(a, b, c) = sum_{n = 0 to b} F(n)
.

For example, if a = 50, b = 2000 and c = 40, then F(0) = 3240 and F(2000) = 2040.
Also, S(50, 2000, 40) = 5204240.

Find the last 9 digits of S(21^7, 7^21, 12^7).


Anwser:


'''
import time, math
start_time = time.time()

def F(a, b, c, n):
    if n > b:
        return n - c
    else:
        return F(a, b, c, a + F(a, b, c, a + F(a, b, c, a + F(a, b, c, a + n))))

def S(a,b,c):
    total = 0
    
    for n in range(b + 1):
        total += F(a, b, c, n)
        
    return total
    
if __name__ == "__main__":
    print(S(50, 2000, 40))
    print("--- %s seconds ---" % (time.time() - start_time))
    
