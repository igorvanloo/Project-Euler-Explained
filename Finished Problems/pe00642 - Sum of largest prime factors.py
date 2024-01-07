#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:54:43 2022

@author: igorvanloo
"""
'''
Project Euler Problem 642

See website for clearer notes

Anwser:
    631499044
--- 97.60407447814941 seconds ---
'''
import time, math
from functools import cache
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2*i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def sum_of_primes(n):
    r = int(math.sqrt(n))
    primes = []
    
    V = [n//i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = {i:i*(i+1)//2-1 for i in V}
    
    for p in range(2, r + 1):
        if S[p] > S[p-1]:  # p is prime
            primes += [p]
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2:
                    break
                S[v] -= p*(S[v//p] - sp)
    return S, primes

def compute(N, p):
    S, primes = sum_of_primes(N)
    
    @cache
    def r(N, p):
        if N == p:
            return p
        if N < 0:
            return 0
        total = S[N] - S[p - 1]
        sqrt_N = math.floor(math.sqrt(N))
        
        for prime in primes:
            if prime > sqrt_N:
                break
            if prime >= p:
                v = r(N//prime, prime)
                total += v

        return total 

    return r(N, p) % 10**9

def compute1(N):
    
    sqrtN = math.floor(math.sqrt(N))
    
    S, primes = sum_of_primes(N)
    k_cache = {}
    def k_smooth(n, i):
        p = primes[i]
        if n <= 0:
            return 0
        if i == 0:
            return int(math.log(n, 2)) + 1
        
        total = 0
        
        if (n, i - 1) in k_cache:
            total += k_cache[(n, i - 1)]
        else:
            k_cache[(n, i - 1)] = k_smooth(n, i - 1)
            total += k_cache[(n, i - 1)]
        
        if (n//p, i) in k_cache:
            total += k_cache[(n//p, i)]
        else:
            k_cache[(n//p, i)] = k_smooth(n//p, i)
            total += k_cache[(n//p, i)]
        return total
    
    total = 0
    #sum 1
    for i in range(len(primes)):
        p = primes[i]
        total += p*k_smooth(N//p, i)
                
    #sum 2
    total -= sqrtN*S[N//(sqrtN + 1)]
    for a in range(1, sqrtN + 1):
        total += S[N//a]
    return total % 10**9
    
if __name__ == "__main__":
    print(compute(201820182018, 2))
    print("--- %s seconds ---" % (time.time() - start_time))
