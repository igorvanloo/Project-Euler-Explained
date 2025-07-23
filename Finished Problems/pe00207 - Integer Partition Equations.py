# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 17:41:44 2025

@author: Igor van loo
"""
'''
Project Euler Problem 207

Fairly simple problem.

Let x = 2^t, then we have the equation 2^2t - 2^t - k = 0 which is a quadratic
Hence we have 2^t = x = (1 + sqrt(1 + 4k)) / 2 allowing us to solve for t = log_2(1 + sqrt(1 + 4k)) - 1

But we need x to be an integer which implies that sqrt(1 + 4k) has to be an integer and hence 1 + 4k must be a square

Simply loop through squares and test is a^2 - 1 is divisble by 4, if yes we have found a valid value of k, then just test if t is an integer

Answer:
    44043947822
--- 0.1787395477294922 seconds ---
'''
    
import time, math
start_time = time.time()

def compute(frac):
    
    perf_count = 0
    total_count = 0
    
    a = 2 
    while True:
        v = a*a - 1
        if v % 4 == 0:
            k = v//4
            t = math.log(1 + a, 2) - 1 
            if t == int(t):
                perf_count += 1
            total_count += 1 
            if perf_count/total_count < frac:
                return k
        a += 1 

if __name__ == "__main__":
    print(compute(1/12345))
    print("--- %s seconds ---" % (time.time() - start_time))
