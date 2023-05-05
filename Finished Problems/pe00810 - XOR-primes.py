# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:36:44 2023

@author: igorvanloo
"""
'''
Project Euler Problem 810

Brute force shows that the first few primes are probably
2, 3, 7, 11, 13, 19, 25, 31, 37, 41 - https://oeis.org/A014580

I learnt this in galois theory, Dummit and Foote pg 589

Anwser:
    124136381
--- 241.78080296516418 seconds ---
'''
import time, math, galois
from functools import cache

start_time = time.time()

def xorProduct(x, y):
    prod = 0
    while y != 0:
        if y % 2 == 1:
            prod ^= x
        x <<= 1
        y >>= 1
    return prod

def bruteForce():
    values = set()
    for x in range(2, 10**4):
        for y in range(x, 10**4):
            values.add(xorProduct(x, y))
    return sorted(values)

def Divisors_of(x):  # Find the divisors of a number
    divisors = set([1])
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.add(i)
            divisors.add(int(x//i))
    return divisors

@cache
def recGenIrredPoly(n):
    #Function will find all irreducibles polynomials of deg(d) such that d|n
    #Using galois theory we know that x^(p^n) - x is the product of all irreducible polynomials
    #of degree d where d|n
    #For example x^(2^2) - x = x(x-1)(x^2 + x + 1) where x, x - 1 are irred poly of degree 1, x^2 + x + 1
    #is irred poly of degree 2
    
    GF = galois.GF(2)
    f = galois.Poly.Degrees([pow(2, n), 1], coeffs = [1, 1], field = GF)
                        
    if n == 1:
        return [galois.Poly([1, 1], field = GF), galois.Poly([1, 0], field = GF)]
    
    div = Divisors_of(n)
    for d in div:
        t = recGenIrredPoly(d)
        for g in t:
            f = f//g
    return f.factors()[0]

def mobius_k_sieve(n, k = 2):
    '''
    I redefined the the Mobius function:
                    1 if n is k-free positive integer with even number of prime factors
        μ_{k}(n) = -1 if n is k-free positive integer with odd number of prime factors
                    0 if n has a k power factor
    '''
    prime = [1]*(n + 1)
    prime[0] = prime[1] = 0
    mob = [0] + [1]*(n)
    for p in range(2, n + 1):
        if prime[p]:
            mob[p] *= -1
            for i in range(2*p, n + 1, p):
                prime[i] = 0
                mob[i] *= -1
            sq = pow(p, k)
            if sq <= n:
                for j in range(sq, n + 1, sq):
                    mob[j] = 0
    return mob

def numOfIrred(n):
    tot = 0
    mob = mobius_k_sieve(n)
    div = Divisors_of(n)
    div.add(n)
    for d in div:
        tot += mob[d]*pow(2, n//d)
    return tot//n

def compute(g):
    tot = 0
    d = 1
    while True:
        t = numOfIrred(d)
        if tot + t > g:
            break
        tot += t
        d += 1
    index = g - tot
    #Once we cross this we know our g-th prime is a degree d polynomial
    print(d, t, index)
    for x in range(pow(2, d) + 1, pow(2, d + 1), 2):
        polyBin = bin(x)
        if polyBin.count("1") % 2 == 1:
            poly = galois.Poly.Int(int(polyBin, 2), field = galois.GF(2))
            if poly.is_irreducible():
                index -= 1
        if index == 0:
            return int(polyBin, 2)
    
def sieve(lim):
    tot = 0
    d = 1
    while True:
        t = numOfIrred(d)
        if tot + t > lim:
            break
        tot += t
        d += 1
        
    N = pow(2, d + 1)
    result = [True]*N
    result[0] = result[1] = False
    for x in range(4, N, 2):
        result[x] = False
    
    count = 1
    for i in range(3, N, 2):
        if result[i]:
            count += 1
            if count == lim:
                return i
            
            j = i
            while True:
                x = xorProduct(j, i)
                if x >= N:
                    break
                result[x] = False
                j += 2
        
    
if __name__ == "__main__":
    print(sieve(5*10**6))
    print("--- %s seconds ---" % (time.time() - start_time))
