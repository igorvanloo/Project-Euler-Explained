#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:39:03 2022

@author: igorvanloo
"""
'''
Project Euler Problem 302

1) largest prime is < 10^6
2) gcd(exponents of n) = 1

1) Note that if the largets factor p of n has exponent 2, this means φ(n) =...p*(p-1) => there will only be one 
p in the factorisation of φ(n) and therefore it cannot be an Achilles number,
this also also means we need to consider primes <= 10^6 because the largest prime must have atleast a power of 3

2) if the gcd(exponents of n) = d ≠ 1 then we have n = q^d and therefore it is a perfect power

Just need to efficiently find all candidate numbers

Anwser:

'''
import time, math
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                if d in factors:
                    factors[n] += 1
                else:
                    factors[n] = 1
            break
    return factors

def phi2(pf):
    new_pf = {}
    for p in pf:
        if p != "prod":
            new_pf[p] = (pf[p] - 1)
            for q, e in prime_factors(p - 1).items():
                if q in new_pf:
                    new_pf[q] += e
                else:
                    new_pf[q] = e
    return new_pf

def condition_checker(curr):
    alist = [curr[y] for y in curr if y != "prod"]
    if len(alist) == 1:
        return 0
    
    t = alist[0]
    for x in range(len(alist)):
        curr = alist[x]
        
        if curr < 2:
            return 0
        
        t = math.gcd(t, curr)
    return t

def compute(limit):
    primes = list_primes(int(limit**(1/3)))
    options1 = set([])
    candidates = set([])
    for a in range(1, len(primes)):
        p = primes[a]
        for b in range(a):
            q = primes[b]
            t = p*p*p*q*q
            if t < limit:
                options1.add(t)
                candidates.add(t)
                
    print("options1 ready")           
    count = 0
    while len(options1) != 0:
        curr = options1.pop()
        for x in primes:
            t = curr*x 
            if t < limit:
                candidates.add(t)
                options1.add(t)
                
    print("candidates ready")
    print("--- %s seconds ---" % (time.time() - start_time))
    for x in candidates:
        pf = prime_factors(x)
        if condition_checker(pf) == 1:                
            phi_pf = phi2(pf)
            if condition_checker(phi_pf) == 1:
                #print(x)
                count += 1
    return count

if __name__ == "__main__":
    print(compute(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))
