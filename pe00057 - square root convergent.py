#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:07:19 2020

@author: igorvanloo
"""

'''
Project Euler Problem 57

We note that if p/q oncverges each next term will be p+2q/q+p

Anwser:
    153
--- 0.002134084701538086 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    count = 0
    numerator = 1
    denominator = 1
    for x in range(1000):
        temp_num = numerator + 2*denominator
        temp_denom = numerator + denominator
        
        if len(str(temp_num)) > len(str(temp_denom)):
            count += 1
        
        numerator = temp_num
        denominator = temp_denom
    return count
        

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))