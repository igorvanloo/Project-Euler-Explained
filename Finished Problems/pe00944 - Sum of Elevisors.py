# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 10:05:52 2026

@author: Igor Van Loo
"""
'''
Project Euler Problem 944

Answer:
    1228599511
--- 169.13043761253357 seconds ---
--- 8.837327480316162 seconds --- Using PyPy
'''
import time, math
start_time = time.time()

def T(N):
    return N*(N + 1) // 2

def S(N, mod = 1234567891):
    
    total = T(N) * pow(2, N - 1, mod)
    
    sqrtN = int(math.sqrt(N))
    total -= sqrtN * pow(2, N - sqrtN, mod)
    
    for k in range(1, sqrtN):
        total -= (k * pow(2, N - N//k, mod)) % mod 
        total -= ((T(N//k) - T(N//(k + 1))) * pow(2, N - k, mod)) % mod
    return int(total) % mod

if __name__ == "__main__":
    print(S(10**14))
    print("--- %s seconds ---" % (time.time() - start_time))
