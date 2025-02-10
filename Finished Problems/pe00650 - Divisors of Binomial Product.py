# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:46:05 2024

@author: Igor Van Loo
"""
'''
Project Euler Problem 650

B(n) = https://oeis.org/A001142

Use divisor function if n = a_1^e_1 * a_2^e_2 * ... * a_k^p_k

then sigma(1, n) = sum of divisors of n = prod (p_i^(a_1 + 1) - 1)/(p_i - 1)

using B(n) = (n!)^(n + 1) / prod_{i = 1}^n (i!)^2

hence we have

B(n) = B(n - 1) * n^n/n!, we can quickly add priem factors of n^n, and subtract prime factors of n!
with precomputed arrays and we find prime factors of B(n)

Answer:
    538319652
--- 87.43184995651245 seconds ---
'''
import time
start_time = time.time()

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                factors[n] = 1
            break
    return factors

def divisor(pf, mod):
    total = 1
    for p in pf:
        e = pf[p]
        total *= (pow(p, e + 1, mod) - 1) * pow(p - 1, -1, mod) % mod
    return total % mod

def prime_factors_sieve(limit):
    result = [{} for _ in range(limit + 1)]
    for i in range(2, limit + 1):
        if len(result[i]) == 0:
            #prime number found
            for j in range(i, limit + 1, i):
                n = j
                if i in result[j]:
                    while n % i == 0:
                        n //= i
                        result[j][i] += 1
                else:
                    result[j][i] = 1
                    n //= i
                    while n % i == 0:
                        n //= i
                        result[j][i] += 1
    return result

def S(n):
    if n == 1:
        return 1
    if n == 2:
        return 4
    #pre compute prime factors of all n
    pf_array = prime_factors_sieve(n + 1)
    
    #Precompute prime factors of n! iteratively
    pf_fac = [{} for _ in range(n + 1)]
    for x in range(2, n + 1):
        pf_fac[x] = {}
        for p in pf_fac[x - 1]:
            pf_fac[x][p] = pf_fac[x - 1][p]
        v = pf_array[x]
        for p in v:
            if p in pf_fac[x]:
                pf_fac[x][p] += v[p]
            else:
                pf_fac[x][p] = v[p]
    
    mod = 10**9 + 7
    B = {2: 1}
    
    D = [0] * (n + 1)
    D[1] = 1
    D[2] = 3
    
    for x in range(3, n + 1):
        pf_x = pf_array[x]
        for p in pf_x:
            if p in B:
                B[p] += pf_x[p]*x
            else:
                B[p] = pf_x[p]*x
        lpf_x = pf_fac[x]
        for p in lpf_x:
            if p in B:
                B[p] -= lpf_x[p]
            else:
                B[p] = lpf_x[p]
        D[x] = divisor(B, mod)
    return sum(D) % mod

if __name__ == "__main__":
    print(S(20000))
    print("--- %s seconds ---" % (time.time() - start_time))
