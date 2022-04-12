#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 23:32:59 2022

@author: igorvanloo
"""
'''
Project Euler Problem 

Anwser:
    605857431263981935
'''
import time, math
start_time = time.time()

def legendre_factorial_single_prime(x, p):
    total = 0
    i = 1
    while pow(p, i) < x:
        total += (math.floor(x//(p**i)))
        i += 1
    return total
    
def T(n, p):
    s0 = 290797
    array = [0]*(n + 1)
    for x in range(n):
        array[x] = s0 % p
        sn = s0*s0
        sn %= 50515093
        s0 = sn
    return array
    
def N(p, q, power):
    total = 0
    t = T(q, p)
    for n in range(0, q + 1):
        total += t[n]*pow(p, n)
    return total

def NF(p, q, power):
    return legendre_factorial_single_prime(N(p, q, power), p) % (p**power)
    
if __name__ == "__main__":
    print(NF(3, 10000, 20))
    #print(NF(61, 10**7, 10))
    print("--- %s seconds ---" % (time.time() - start_time))