# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:46:58 2023

@author: igorvanloo
"""
'''
Project Euler Problem 540

Optimizing an optimized version of my pythagorean_triples function 

we can find the count quite quickly for up to 10^8 which is too slow, but it is correct according to 
https://oeis.org/A101931 - Answer for 10^n

1. https://mathworld.wolfram.com/PythagoreanTriple.html
Lehmer finds that the P(n) ~ n/(2*pi)
So we expect P(3141592653589793) ~ pi*10^15/2*pi = 5*10^14

2. Algorithm to find number of primitive triples is here https://vixra.org/pdf/1310.0211v1.pdf but it is
Barely faster than my optimized method

3. Following this paper https://www.sciencedirect.com/science/article/pii/S0377042701004964 we can get an answer
See website for details

Anwser:
    500000000002845
--- 536.6237738132477 seconds ---
'''
import time, math

start_time = time.time()

def mobius_k_sieve(limit, k = 2):
    isprime = [1]*(limit + 1)
    isprime[0] = isprime[1] = 0
    mob = [0] + [1]*(limit)
    for p in range(2, limit + 1):
        if isprime[p]:
            mob[p] *= -1
            for i in range(2*p, limit + 1, p):
                isprime[i] = 0
                mob[i] *= -1
            sq = pow(p, k)
            if sq <= limit:
                for j in range(sq, limit + 1, sq):
                    mob[j] = 0
    return mob

def P(n):
    mu = mobius_k_sieve(int(math.sqrt(n)) + 1)
    
    R_cache = {}
    def R(n):
        if n in R_cache:
            return R_cache[n]
        c = 0 
        for x in range(int(math.sqrt(n)) + 1):
            min_y, max_y = x + 1, int(math.sqrt(n - x*x))
            if max_y < min_y:
                break
            c += max_y - min_y + 1
        R_cache[n] = c
        return c
    
    def Q(n):
        total = 0
        m = math.sqrt(n)
        for d in range(1, int(m) + 1):
            total += mu[d] * R(n // (d*d))
        return total
    
    c = 0
    k = 0
    while 2**k <= n:
        x = Q(n // pow(2, k))
        c += pow(-1, k) * x
        k += 1
    return c

if __name__ == "__main__":
    print(P(3141592653589793))
    print("--- %s seconds ---" % (time.time() - start_time))
