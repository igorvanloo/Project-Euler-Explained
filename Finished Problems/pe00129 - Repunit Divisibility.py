#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:40:46 2021

@author: igorvanloo
"""

'''
Project Euler Problem 129



Anwser:
    1000023
--- 4.162177085876465 seconds ---
'''
    
import time, math
start_time = time.time()

def compute(limit):
    
    n = 10**6
    valuenotfound = True
        
    while valuenotfound == True:
        if math.gcd(n, 10) == 1:
            l = 1
            while True:
                if pow(10,l,9*n) == 1:
                    break
                l += 1
                if l > limit:
                    value = n
                    valuenotfound = False
        n += 1

    return value

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))