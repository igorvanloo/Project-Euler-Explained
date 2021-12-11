#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:06:20 2021

@author: igorvanloo
"""

'''
Project Euler Problem 577

H(3) = 1 = T(1)
H(4) = 3 = T(2)
H(5) = 6 = T(3)
H(6) = 12 = T(4) + 2T(1)
H(7) = 21 = T(5) + 2T(2)

H(20) = T(18) + 2T(15) + 3T(12) + 4T(9) + 5T(6) + 6T(3)

In general every time H(3n) we add n new types of hexagons

H(3) we have a 1 side length hexagons
H(6) we have 2 side length and also sqrt(3) side length 

Anwser:
    265695031399260211
--- 5.640542984008789 seconds ---'''

import time
start_time = time.time()

def compute(limit):
    total = 0
    tri_numbers = [0] + [int((n*(n+1))/2) for n in range(1, 12344)]
    
    for x in range(3, limit + 1):
        for y in range(1, x//3 + 1):
            total += y*tri_numbers[x - 2 - 3*(y-1)]    
    return total
        
if __name__ == "__main__":
    print(compute(12345))
    print("--- %s seconds ---" % (time.time() - start_time))
