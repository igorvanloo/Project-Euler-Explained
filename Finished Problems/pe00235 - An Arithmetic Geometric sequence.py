#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:56:36 2022

@author: igorvanloo
"""
'''
Project Euler Problem 235

Given is the arithmetic-geometric sequence u(k) = (900-3k)r^k-1.
Let s(n) = Σk=1...nu(k).

Find the value of r for which s(5000) = -600,000,000,000.

Give your answer rounded to 12 places behind the decimal point.

The greater r is the more neagtive it will get

if we reach an r that results in a smaller s(5000), we need a smaller r

Anwser:
    1.002322108633
--- 0.0960090160369873 seconds ---
'''

import time
start_time = time.time()

def u(k, r):
    return (900 - 3*k)*pow(r, k-1)

def s(n, r):
    total = 0
    for k in range(1, n+1):
        total += u(k, r)
    return total

def compute():
    r = "1."
    goal = -600000000000
    while len(r) != 16:
        for x in range(0, 10):
            r1 = float(r + str(x))
            if s(5000, r1) < goal:
                r += str(x - 1)
                break
    return round(float(r), 12)
        
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
