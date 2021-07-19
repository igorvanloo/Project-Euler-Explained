#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 21:48:51 2021

@author: igorvanloo
"""
'''
Project Euler Problem 115

c(n,m) = 2*c(n-1,m) - c(n-2,m) + c(n-m-1,m)

note c(0,m) = ... = c(m-1,m) = 1

so c(n=50, 50) = 2*c(49,50) - c(48,50) + c(-1,50) = 3
c(n=51, 50) = 2*c(50,50) - c(49,50) + c(0,50) = 6
c(n=52, 50) = 2*c(51,50) - c(50,50) + c(1,50) = 10

Anwser:
    (168, 1053389)
--- 0.005525112152099609 seconds ---
    
'''

import time, numpy
start_time = time.time()

def compute(limit):
    iv = [1 for x in range(0,51)] + [2] + [0 for x in range(0,1000)]
    
    n = 51
    
    while True:
        iv[n] = 2*iv[n-1] - iv[n-2] + iv[n-50-1]
        
        if iv[n] > limit:
            break
        n += 1
    return n-1, iv[n]

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))