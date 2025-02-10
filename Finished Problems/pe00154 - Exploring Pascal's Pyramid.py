# -*- coding: utf-8 -*-
#!/usr/bin/env pypy
"""
Created on Wed Feb  5 13:05:25 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 154

https://en.wikipedia.org/wiki/Pascal%27s_pyramid#Relationship_with_Pascal's_triangle
We get C(n, i, j) = C(i, j) * C(n, i)

Note that we want to find all coefficients with 2^(12) * 5^(12) = 10^(12) in their prime factorization
Recursively build up a prime factorization of all binomial coefficients, only caring about the 2's, and 5's

Answer:
    479742450
--- 675.7337036132812 seconds ---
--- 21.235472917556763 seconds --- using pypy
'''
import time
start_time = time.time()

def fac(n, d):
    c = 0
    while n % d == 0:
        n //= d
        c += 1
    return c

def compute(N, a, ae, b, be):
    pfa = [0]*(N + 1) 
    pfb = [0]*(N + 1)
    
    for n in range(a, N + 1, a):
        pfa[n] = fac(n, a)
        
    for n in range(b, N + 1, b):
        pfb[n] = fac(n, b)
        
    for n in range(1, N + 1):
        pfa[n] += pfa[n - 1]
        pfb[n] += pfb[n - 1]
    
    total = 0
    for i in range(N//3 + 1):
        for j in range(i, (N - i)//2 + 1):
            k = N - i - j
            #i <= j <= k
            if pfb[N] - pfb[i] - pfb[j] - pfb[k] >= be:
                if pfa[N] - pfa[i] - pfa[j] - pfa[k] >= ae:
                    if i == j and j == k:
                        total += 1
                    elif i == j or j == k:
                        total += 3
                    else:
                        total += 6
    return total
            
if __name__ == "__main__":
    print(compute(200000, 2, 12, 5, 12))
    print("--- %s seconds ---" % (time.time() - start_time))
