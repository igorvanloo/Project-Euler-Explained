#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:13:26 2021

@author: igorvanloo
"""

'''
Project Euler Problem 135

3 consecutive integers look like a-d, a, a+d,
then (a+d)^2 - a^2 - (a-d)^2 = 4ad-a^2 = a(4d-a) = n

This means 1 <= a < n and because a-d > 0 then a > d we have that a/4 < d < a
Build an array and count solutions 

Anwser:
    4989
--- 1.0179691314697266 seconds ---
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
    
    return array.count(10)
                    

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))
