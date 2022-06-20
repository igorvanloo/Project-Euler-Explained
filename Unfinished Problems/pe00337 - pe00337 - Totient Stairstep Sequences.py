#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 09:25:00 2022

@author: igorvanloo
"""
'''
Project Euler Problem 337

Recursively build trees is my first idea
Like this I can confirm both test cases

Anwser:

'''
import time, math
from functools import cache
start_time = time.time()

def totient_sieve(n):
    phi = [i for i in range(n + 1)]
    for p in range(2, n + 1):
        if phi[p] == p:
            # print(p)
            phi[p] -= 1
            for i in range(2*p, n + 1, p):
                phi[i] -= (phi[i] // p)
    return phi
    
def compute(limit):
    phi_sieve = totient_sieve(limit)
    mod = 10**8
    
    @cache
    def rec(n, phi_n, goal):
        total = 0
        if n <= goal:
            total += 1
            total %= mod
        for x in range(n + 1, goal + 1):
            phi_x = phi_sieve[x]
            if phi_n < phi_x < n:
                total += rec(x, phi_x, goal)
                total %= mod
        return total % mod
    return rec(6, phi_sieve[6], limit)

if __name__ == "__main__":
    print(compute(10000))
    print("--- %s seconds ---" % (time.time() - start_time))
