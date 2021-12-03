#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 12:17:58 2021

@author: igorvanloo
"""

'''
Project Euler Problem 136

Exactlu the same code as 135, take a bit longer but it's okay

Anwser:
    2544559
--- 65.39310908317566 seconds ---
'''
import time, math
start_time = time.time()

def compute(limit):
    
    array = [0]*(limit)
    
    for a in range(1, limit):
        for d in range(int(math.floor(a/4))+1, a):
            n = a*(4*d-a)
            if n > limit-1:
                break
            else:
                array[n] += 1
                #print(n)
    
    return array.count(1)
                    

if __name__ == "__main__":
    print(compute(50*10**6))
    print("--- %s seconds ---" % (time.time() - start_time))