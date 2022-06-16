#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:45:13 2022

@author: igorvanloo
"""
'''
Project Euler Problem 323

Brute Force gives me an estimate of 6.3551368

The chance any one bit gets flipped from a 0 to a 1 is exactly 0.5
Therefore the chance that it does not get flipped in N rounds is 0.5^N
Therefore the chance that it does get flipped in N rounds is (1 - 0.5^N)
Therefore the chance that all 32 bits are flipped in N rounds is (1 - 0.5^N)^32

Therefore the probability that we finish on round N is (1 - 0.5^N)^32 - (1 - 0.5^(N - 1)^32)

Anwser:
    6.3551758451
--- 0.00014901161193847656 seconds ---
'''
import time
import random
start_time = time.time()

def BruteForce(trials):
    total = 0
    count = 0
    while count != trials:
        x = 0
        N = 0
        while x != (2**32 - 1):
            N += 1
            y = random.randint(0, 2**32 - 1)
            x |= y
        total += N
        count += 1
    return total/trials
    
def compute(digits):
    prev = 0
    N = 1
    total = 0
    while True:
        curr = (1 - 0.5**N)**digits
        p = curr - prev
        if N*p < pow(10, -11):
            print(N)
            break
        total += N*p
        prev = curr
        N += 1
    return round(total, 10)

if __name__ == "__main__":
    print(compute(32))
    print("--- %s seconds ---" % (time.time() - start_time))
