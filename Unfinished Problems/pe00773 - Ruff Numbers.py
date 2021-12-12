#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:47:04 2021

@author: igorvanloo
"""

'''
Project Euler Problem 773

Get F(3) correct but way too slow, haven't made the key discovery yet

Anwser:

'''

import time, math, eulerlib
start_time = time.time()

primes = eulerlib.primes(100000)

def compute(n):
    S_k = [2,5] + [x for x in primes if str(x)[-1] == "7"]
    S_k = S_k[0:n+2]
    print(S_k)
    N_k = 1
    for x in S_k:
        N_k *= x
    print(N_k)
    
    k_ruff = []
    
    for x in range(7, N_k + 1, 10):
        is_k_ruff = True
        for y in S_k:
            if x % y == 0:
                is_k_ruff = False
                break
        if is_k_ruff:
            k_ruff.append(x)
                
    return sum(k_ruff) % 1000000007

if __name__ == "__main__":
    print(compute(5))
    print("--- %s seconds ---" % (time.time() - start_time))