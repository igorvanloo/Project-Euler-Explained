# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:52:33 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 932

Answer:
    72673459417881349
--- 58.646085262298584 seconds ---
'''
import time, math
start_time = time.time()

def compute(N):
    total = -1 #To account for (a, b) = (0, 1) solution
    for b in range(1, 10**(N//2)):
        n = len(str(b))
        v = 4*b*(1 - 10**n) + 10**(2*n)
        if v > 0:
            v = math.sqrt(v)
            if v == int(v):
                v = int(v)
                a = (10**n - 2*b + v)//2
                total += a*10**n + b
                    
                a = (10**n - 2*b - v)//2
                total += a*10**n + b
    return total

if __name__ == "__main__":
    print(compute(16))
    print("--- %s seconds ---" % (time.time() - start_time))
