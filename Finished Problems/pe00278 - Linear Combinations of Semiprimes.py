#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:24:07 2022

@author: igorvanloo
"""
'''
Project Euler Problem 278

Johnsons formula
if gcd(a1, a2, a3) = 1 and gcd(a1, a2) = d and ai= d*ai' for i = 2, 3
Then g(a1, a2, a3) = d*g(a1, a2', a3') + a1*(d - 1)

Anwser:
    1228215747273908452
--- 18.127201080322266 seconds ---
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
    
def compute(limit):
    total = 0
    primes = list_primes(limit)
    for a in range(len(primes)):
        p = primes[a]
        for b in range(a + 1, len(primes)):
            q = primes[b]
            for c in range(b + 1, len(primes)):
                r = primes[c]
                total += p*q*r*2 - p*q - p*r - q*r
    return total

if __name__ == "__main__":
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
