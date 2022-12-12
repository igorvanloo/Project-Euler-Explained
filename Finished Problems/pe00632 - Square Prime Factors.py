# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:19:36 2022

@author: igorvanloo
"""
'''
Project Euler Problem 632

Using a modified generalised Mobius function sieve which counts the number of sq prime factors along side it,
we can naively brute force the given solutions.

We know the number of squarefree numbers less than n can be computed by sum_{i = 1}^sqrt(n) floor(n/i*i)

We want a function C_k(n) to count the number of primes such that p^2|n

We know C_0(n) = sum_{i = 1}^sqrt(n) μ(i) floor(n/i*i)

Now for C_k(n) = #of integers x <= n such that x has exactly k squared prime factor
1. If x is square-free its co-eff should still be 0,
2. If x has a square factor, 
    1. Suppose it has less than 1 prime factor the co-eff should still be 0
    2. Suppose it has m >= k prime factors, it's co-efficient is explained here: https://math.stackexchange.com/questions/1716833/a-generalized-version-of-inclusion-exclusion-principle-using-a-binomial-identity
    it is (-1)^(m - k) choose(m, k)

let p(i) denote the number of prime factors i has, then 

If μ(i) = 1, we have an even number of prime factors

C_k(n) = (-1)^? sum_{i = 1}^sqrt(n) μ(i) floor(n/i*i) choose(p(i), k)

Anwser:
    728378714
--- 363.4533610343933 seconds ---
'''
import time, math
from functools import cache
start_time = time.time()
    
def mobius_k_sieve(n, k = 2):
    prime = [1]*(n + 1)
    prime[0] = prime[1] = 0
    mob = [0] + [1]*(n)
    num_of_pf = [0]*(n + 1)
    for p in range(2, n + 1):
        if prime[p]:
            mob[p] *= -1
            num_of_pf[p] += 1
            for i in range(2*p, n + 1, p):
                prime[i] = 0
                mob[i] *= -1
                num_of_pf[i] += 1
            sq = pow(p, k)
            if sq <= n:
                for j in range(sq, n + 1, sq):
                    mob[j] = 0
    return mob, num_of_pf, prime

@cache
def choose(n, r):
    if r > n:
        return 0
    if r == 0:
        return 1
    return choose(n-1, r-1) + choose(n-1, r)

def compute(n):
    sq = int(math.sqrt(n))
    mob, num_of_pf, isprime = mobius_k_sieve(sq, 2)
    prime = [i for i, p in enumerate(isprime) if p]
    print("sieve done")
    print("--- %s seconds ---" % (time.time() - start_time))
    
    max_prime = 1
    prod_prime = 2
    while prod_prime <= sq:
        prod_prime *= prime[max_prime]
        max_prime += 1
    
    Ck = [0]*max_prime
    for i in range(1, sq + 1):
        const = mob[i]*(n//pow(i, 2))
        for k in range(max_prime):
            v = const*pow(-1, k)*choose(num_of_pf[i], k)
            if v == 0:
                break
            Ck[k] += v
    total = 1
    for k, x in enumerate(Ck):
        print("C_(%s)(%s) = %s" % (k, n, x))
        if x == 0:
            break
        total *= x
        total %= (10**9 + 7)
    return total

if __name__ == "__main__":
    print(compute(10**14))
    print("--- %s seconds ---" % (time.time() - start_time))

