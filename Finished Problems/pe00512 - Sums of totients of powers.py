#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:10:56 2021

@author: igorvanloo
"""

'''
Project Euler Problem 512

It appears that f(n) = 0 when n is even and is equal to phi(n) when n is odd

why?
phi(n^k) = n^k Prod(p|n^k) (1 - 1/p) = n^(k-1) * (n Prod(p/n <=> p/n^k) (1- 1/p)) = n^(k-1) * phi(n)

Now because phi(n^k) = n^(k-1) * phi(n) => 
phi(n^k) = (-1)^(k-1) phi(n) mod(n+1)

so f(n) = sum_{k = 1 to n} phi(n^k) mod(n+1) = sum_{k = 1 to n} (-1)^(k-1) phi(n)
Therefore when n is even we have f(n) = 0
and when n is odd we have f(n) = phi(n)

Anwser:
    2026423657126435 ~ 10^8
--- 72.85672426223755 seconds ---

    50660591862310323
--- 1021.46232567244944 seconds ---
--- 24.47919201850891 seconds --- with pypy
'''

import time
start_time = time.time()

def totient_sieve(n): 
    phi = [i for i in range(n+1)]
    for p in range(3, n+1, 2): 
        if phi[p] == p:
            #print(p)
            phi[p] -= 1
            for i in range(3*p, n+1, 2*p):
                phi[i] -= (phi[i]//p)
    total = 0
    for x in range(1, len(phi), 2):
        total += phi[x]
    return total

if __name__ == "__main__":
    print(totient_sieve(5*(10**8)))
    print("--- %s seconds ---" % (time.time() - start_time))