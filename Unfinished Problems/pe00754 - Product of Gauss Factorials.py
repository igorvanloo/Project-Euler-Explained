#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:06:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

After some brute force found

g(n) = https://oeis.org/A001783
G(n) = https://oeis.org/A280820

g(n) = n^phi(n)*Product_{d|n} (d!/d^d)^mu(n/d)

Anwser:
    517055464 ~ 10^4
--- 10.316388845443726 seconds ---
'''

import time, math
start_time = time.time()

def phi(n):
    if n == 1:
        return 1
    phi = 1
    d = 2 
    while n > 1:
        count = 0 
        while n % d == 0:
            count += 1
            n /= d
        if count > 0:
            phi *= (d**(count-1))*(d-1)
        d = d + 1
        if d*d > n:
            if n > 1: 
                phi *= int(n - 1)
            break
    return phi

def Mobius(n):
    if n == 1:
        return 1
    d = 2
    num_of_primes = 0
    while n > 1:
        while n % d == 0:
            num_of_primes += 1
            if n % (d*d) == 0:
                return 0
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                num_of_primes += 1
            break
    return (-1)**num_of_primes

def Mobius_phi(n): #Combined mobius and phi function, must faster than doing both seperately
    mu = 2
    phi = 1
    if n == 1:
        return [1, 1]
    d = 2
    num_of_primes = 0
    
    while n > 1:
        count = 0 
        while n % d == 0:
            num_of_primes += 1
            count += 1
            if n % (d*d) == 0:
                mu = 0
            n /= d
        if count > 0:
            phi *= (d**(count-1))*(d-1)
        d = d + 1
        if d*d > n:
            if n > 1: 
                num_of_primes += 1
                phi *= int(n - 1)
            break
    if mu == 0:
        return [0, phi]
    return [(-1)**num_of_primes, phi]

def modfactorial(n, mod):
    total = 1
    for x in range(2, n+1):
        total *= x
        total %= mod
    return total

def modDivide(a,b,m):
    a = a % m
    inv = pow(b,-1,m)
    if inv != -1:
        return (inv*a) % m
        
def Divisors(x): #Find the divisors of a number
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    return set(divisors)

def compute(limit, mod):
    G = 1
    divisor = [0]*(limit+1)
    divisor[1] = [1]
    
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(x, limit + 1, x):
            z = int(y/x)
            
            if divisor[y] == 0:
                divisor[y] = [x, z]
            else:
                divisor[y] += [x, z]
    
    for x in range(1,limit + 1):
        if x % 1000 == 0:
            print(x)
        g = pow(x,phi(x),mod)
        for d in set(divisor[x]):
            g *= pow(modDivide(modfactorial(d, mod),pow(d,d,mod), mod), Mobius(x/d), mod)
        G *= g
        G %= mod
    return G
    
def compute1(limit): #Calculates small values of g quickly
    G = 1
    for x in range(1,limit + 1):
        
        g = x**phi(x)
        for d in Divisors(x):
            g *= ((math.factorial(d)/(d**d))**Mobius(x/d))
        G *= math.ceil(g)
        print(g)
    
    return G 

def compute2(limit): #Simplest Version
    for x in range(1, limit + 1):
        g = 1
        for y in range(1, x):
            if math.gcd(x,y) == 1:
                g *= y
        print(g)
    
if __name__ == "__main__":
    print(compute(10**5, 1000000007))
    print("--- %s seconds ---" % (time.time() - start_time))