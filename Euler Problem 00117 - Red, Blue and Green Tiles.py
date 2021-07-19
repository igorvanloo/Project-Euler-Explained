#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 01:06:16 2021

@author: igorvanloo
"""

'''
Project Euler Problem 117

tile a n length tile denote a(n)

a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4)

a1 = 1
a2 = 2
a3 = 4
a4 = 8

Anwser:
    100808458960497
--- 0.00018787384033203125 seconds ---
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute(y):
    a1 = 1
    a2 = 2
    a3 = 4
    a4 = 8
    
    for x in range(0,y-4):
        an = a1 + a2 + a3 + a4
        a1 = a2
        a2 = a3
        a3 = a4
        a4 = an
    
    return an

if __name__ == "__main__":
    print(compute(49))
    print("--- %s seconds ---" % (time.time() - start_time))