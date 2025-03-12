#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:06:30 2021

@author: igorvanloo
"""
'''
Project Euler Problem 754

After some brute force found

g(n) = https://oeis.org/A001783

g(n) = n^phi(n)*Product_{d|n} (d!/d^d)^mu(n/d)

    517055464 ~ 10^4
--- 10.316388845443726 seconds ---
    516871211 ~ 10^5
--- 0.9417591094970703 seconds ---
    557051244 ~ 10^6
--- 10.077383279800415 seconds ---
    623561178 ~ 10^7
--- 117.46165204048157 seconds ---

Anwser:
    785845900
--- 2452.4602587223053 seconds ---
'''

import time
start_time = time.time()

def totient_mobius_sieve(n):
    phi = [i for i in range(n + 1)]
    mob = [1]*(n + 1)
    mob[0] = 0
    for p in range(2, n + 1):
        if phi[p] == p:
            # print(p)
            for i in range(p, n + 1, p):
                phi[i] -= (phi[i] // p)
                mob[i] *= -1
            sq = p*p
            if sq < n:
                for j in range(sq, n + 1, sq):
                    mob[j] = 0
    return phi, mob

def modfactorial(limit, mod):
    factorial = [1]*(limit + 1)
    for x in range(2, limit):
        factorial[x] = x*factorial[x - 1]
        factorial[x] %= mod
    return factorial

def ModDivision(a,b,m):
    a = a % m
    try:
        inv = pow(b,-1,m)
    except ValueError:
        return "Division not defined"
    else:
        return (inv*a) % m

def compute(limit, mod):
    phi_sieve, mu_sieve = totient_mobius_sieve(limit)
    factorial = modfactorial(limit, mod)
    G = 1
    for n in range(0, limit + 1):
        G *= pow(n, phi_sieve[n], mod)
        G %= mod
    for d in range(2, limit + 1):
        fac = ModDivision(factorial[d - 1], pow(d, d - 1, mod), mod)
        mu_total = sum(mu_sieve[n//d] for n in range(d, limit + 1, d))
        G *= pow(fac, mu_total, mod)
        G %= mod
    return G

if __name__ == "__main__":
    print(compute(10**8, 10**9 + 7))
    print("--- %s seconds ---" % (time.time() - start_time))