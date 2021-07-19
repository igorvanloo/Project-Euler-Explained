#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:52:54 2021

@author: igorvanloo
"""

'''
Project Euler Problem 116

red tiles denote r(n) = r(n-1) + r(n-2)
green tiles denote g(n) = g(n-1) + g(n-3)
blue tiles denote b(n) = b(n-1) + b(n-4)


Anwser:
    20492570929
--- 0.00015497207641601562 seconds ---
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute(y):
    r1 = 1
    r2 = 2
    
    g1 = 1
    g2 = 1
    g3 = 2
    
    b1 = 1
    b2 = 1
    b3 = 1
    b4 = 2
    
    for x in range(y-2):
        rn = r2 + r1
        r1 = r2
        r2 = rn
    
    for x in range(y-3):
        gn = g3 + g1
        g1 = g2
        g2 = g3
        g3 = gn
    
    for x in range(y-4):
        bn = b4 + b1
        b1 = b2
        b2 = b3
        b3 = b4
        b4 = bn
    
    return rn+gn+bn - 3

if __name__ == "__main__":
    print(compute(49))
    print("--- %s seconds ---" % (time.time() - start_time))