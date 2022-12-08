#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 01:17:08 2021

@author: igorvanloo
"""

'''
Project Euler Problem 193

Almost complete copy paste from Problem 745

Approximate anwser = 6*2**50 / (math.pi)**2 = 684465067344555

Anwser:
    684465067343069
--- 42.56223487854004 seconds ---
'''
import time, math

def mobius_k_sieve(n, k):
    isprime = [1]*(n + 1)
    isprime[0] = isprime[1] = 0
    mob = [0] + [1]*(n)
    for p in range(2, n + 1):
        if isprime[p]:
            mob[p] *= -1
            for i in range(2*p, n + 1, p):
                isprime[i] = 0
                mob[i] *= -1
            sq = pow(p, k)
            if sq <= n:
                for j in range(sq, n + 1, sq):
                    mob[j] = 0
    return isprime, mob

def count_kfree(n, k):
    '''
    I re-defined the the Mobius function:
                    1 if n is kpower-free positive integer with even number of prime factors
        μ_{k}(n) = -1 if n is kpower-free positive integer with odd number of prime factors
                    0 if n has a k power factor
                    
    Computes the number of integers x <= n such that x is k-free, denote this as S(n)
    We use the fact that S(n) = sum_{d = 1}^n |μ_k(d)| = sum_{d = 1}^{floor{n^(1/k)}} μ_{k}(d)*floor{n/d^k}
    '''
    sq = int(pow(n, 1/k))
    _, mobius_k = mobius_k_sieve(sq, k)
    return sum([mobius_k[i]*(n//pow(i, k)) for i in range(1, sq + 1)])

def S1(N): #Reduced speed for 10^8 ~ 0.02 seconds, can be used to solve final problem
    sqrtN = int(math.sqrt(N))
    a = [0] + [1]*sqrtN
    for i in range(sqrtN,1,-1):
        if i % 10**6 == 0:
            print(i)
        a[i] = math.floor(N/(i*i)) - sum([a[i*j] for j in range(2,math.floor(sqrtN/i) + 1)])
    return N - sum([a[i] for i in range(len(a))]) + 1

if __name__ == "__main__":
    start_time = time.time()
    print(count_kfree(2**50, 2))
    print("--- %s seconds ---" % (time.time() - start_time))