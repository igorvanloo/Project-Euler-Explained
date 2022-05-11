#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:00:20 2022

@author: igorvanloo
"""
'''
Project Euler Problem 183

Let X = round(N/e), then M(N) = (N/X)^X

Then we need to check if M(N) terminates, this is only true if (N/X)^X = k/(2^a*5^b)

This is of course only true if N/X = k/(2^c*5^d)

Therefore we divide X by the gcd(X, N) and we continuously divide by 2 and 5, 
if we are left with one it terminates otherwise it repeats
 
Anwser:
    48861552
--- 0.009014129638671875 seconds ---
'''
import time, math
start_time = time.time()

def compute(limit):
    total = 0
    for N in range(5, limit + 1):
        X = round(N/math.e)
        den = (X/math.gcd(N, X))          
        while den % 2 == 0:
            den /= 2
        while den % 5 == 0:
            den /= 5
        if int(den) == 1:
            total -= N
        else:
            total += N
    return total
                
if __name__ == "__main__":
    print(compute(10000))
    print("--- %s seconds ---" % (time.time() - start_time))
