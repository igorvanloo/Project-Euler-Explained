# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 12:28:19 2022

@author: igorvanloo
"""
'''
Project Euler Problem 531

Let g(a,n,b,m) be the smallest non-negative solution x to the system:
x = a mod n
x = b mod m
if such a solution exists, otherwise 0.

E.g. g(2,4,4,6)=10, but g(3,4,4,6)=0.

Let φ(n) be Euler's totient function.

Let f(n,m)=g(φ(n),n,φ(m),m)

Find ∑ f(n,m) for 1000000 ≤ n < m < 1005000

Anwser:
    4515432351156203105
--- 37.31134653091431 seconds ---
'''
import time
start_time = time.time()

def ExtendedEuclideanAlgorithm(a, b):
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    # gcd(a, b) = as + bt
    old_r, r = a, b
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s - q*s 
    if b != 0:
        bezout_t = (old_r - old_s*a) // b
    else:
        bezout_t = 0
    return old_r, old_s, bezout_t
        
def Generalised_CRT(a1, a2, n1, n2):
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Generalization_to_non-coprime_moduli
    #x = a1 (mod n1)
    #x = a2 (mod n2)
    g, u, v = ExtendedEuclideanAlgorithm(n1, n2)
    # g = u*n1 + v*n2
    if g == 1:
        return (a1*v*n2 + a2*u*n1) % (n1*n2)
    M = (n1*n2)//g
    if a1 % g != a2 % g:
        return 0    
    return ((a1*v*n2 + a2*u*n1)//g) % M
    
def totient_sieve(n):
    phi = [i for i in range(n + 1)]
    for p in range(2, n + 1):
        if phi[p] == p:
            # print(p)
            phi[p] -= 1
            for i in range(2*p, n + 1, p):
                phi[i] -= (phi[i] // p)
    return phi

def compute(start, limit):
    total = 0
    phi = totient_sieve(limit)
    for n in range(start, limit):
        for m in range(n + 1, limit):
            total += Generalised_CRT(phi[n], phi[m], n, m)
    return total
        
if __name__ == "__main__":
    print(compute(10**6, 10**6 + 5000))
    print("--- %s seconds ---" % (time.time() - start_time))
