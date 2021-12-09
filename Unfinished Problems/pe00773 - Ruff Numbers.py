#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:47:04 2021

@author: igorvanloo
"""

'''
Project Euler Problem 773

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
    
    k_ruff = [x for x in range(1,N_k + 1)]
    
    for x in range(len(k_ruff)):
        if str(k_ruff[x])[-1] == "7":
            for y in S_k:
                if k_ruff[x] % y == 0:
                    k_ruff[x] = 0
                    break
        else:
            k_ruff[x] = 0
                
    return sum(k_ruff) % 1000000007

if __name__ == "__main__":
    print(compute(97))
    print("--- %s seconds ---" % (time.time() - start_time))