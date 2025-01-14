# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:36:37 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 788

D(N) = sum_{n = 1}^N sum_{m = n//2 + 1}^n c(n, m)

where c(n, m) = 9^(n - m + 1) nCm

Answer:
    471745499
--- 7.021334648132324 seconds ---
'''
import time
start_time = time.time()

def factorial_mod(n, mod):
    factorial = [1]*(n + 1)
    for x in range(2, n + 1):
        factorial[x] = x*factorial[x - 1]
        factorial[x] %= mod
    return factorial

def D(N):
    mod = 10**9 + 7
    fac = factorial_mod(N, mod)
    
    def c(n, m):
        return (pow(9, n - m + 1, mod) * (fac[n] * pow(fac[n - m], -1, mod) * pow(fac[m], -1, mod))) % mod
    
    return sum(c(n, m) for n in range(1, N + 1) for m in range(n//2 + 1, n + 1)) % mod

if __name__ == "__main__":
    print(D(2022))
    print("--- %s seconds ---" % (time.time() - start_time))
