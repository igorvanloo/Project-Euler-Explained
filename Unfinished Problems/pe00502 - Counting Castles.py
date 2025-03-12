# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 22:30:10 2025

@author: Igor Van Loo
"""

'''
Project Euler Problem 502

https://charlesreid1.com/wiki/Project_Euler/502

Answer:

'''
import time, math
start_time = time.time()

def binom(n, k, p = None):
    #Finds nCk % p
    if k > n:
        return 0
    
    num = 1
    for i in range(n - k + 1, n + 1):
        num *= i
        num %= p
    
    den = 1
    for i in range(1, k + 1):
        den *= i
        den %= p
    print(num, den, pow(den, p - 2, p))
    return (num * pow(den, p - 2, p)) % p

def F(w, h):
    mod = 10**9 + 7
    return binom(2*h + w - 3, w - 1)

if __name__ == "__main__":
    print(F(4, 4))
    print("--- %s seconds ---" % (time.time() - start_time))