#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:57:18 2022

@author: igorvanloo
"""
'''
Project Euler Problem 318

Just need to sum ceil(-2011/log_10(p + q - 2sqrt(pq))) if 0 < p + q - 2sqrt(pq) < 1

Anwser:
    709313889
--- 0.2456071376800537 seconds ---
'''
import time, math
start_time = time.time()

def compute(limit):
    total = 0
    for p in range(1, limit):
        for q in range(p + 1, limit - p + 1):
            t = p + q - 2*math.sqrt(p*q)
            if 0 < t < 1:
                total += math.ceil(-limit/math.log(t, 10))
    return total
                
if __name__ == "__main__":
    print(compute(2011))
    print("--- %s seconds ---" % (time.time() - start_time))
