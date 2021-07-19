#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:15:44 2021

@author: igorvanloo
"""

'''
Project Euler Problem 381

For a prime p let S(p) = (∑ (p-k)!) mod(p) for 1 ≤ k ≤ 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that ∑ S(p) = 480 for 5 ≤ p < 100.

Find ∑ S(p) for 5 ≤ p < 10^8.

let p be a prime

then S(p) = (p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)! = (p-5)!((p-1)(p-2)(p-3)(p-4) + (p-2)(p-3)(p-4) + (p-3)(p-4) + (p-4) + 1)


Reasoning

Wilson's theorem states that if n is a prime then (n-1)! = -1 modn = n - 1 modn

(n-1)! = (n-1)(n-2)! = n-1 modn => (n-2)! = (n-1)(n-1)^-1 modn = 1 mod n 

(n-2)! = (n-2)(n-3)(n-4)(n-5)! = 1 modn = (n-5)! = ((n-2)(n-3)(n-4))^-1 mod n

So now we can quickly calculate the rest of the terms

Anwser:
    139602943319822
--- 44.837475061416626 seconds ---
'''

import time, math, eulerlib
start_time = time.time()

def compute():
    limit = 10**4
    primes = eulerlib.primes(limit)[2:]
    print("done")
    total = 0
    for p in primes:
        p4 = p-4
        p3 = p4*(p-3)
        p2 = p3*(p-2)
        p1 = p2*(p-1)
        total += (pow(math.factorial(p-5),1,p) * (p4+p3+p2+p1+1) %p) % p
                  
    return total

def compute1():
    limit = 10**8
    primes = eulerlib.primes(limit)[2:]
    print("done")
    total = 0
    for p in primes:
        p5 = pow((p-2)*(p-3)*(p-4), -1, p)
        p4 = ((p-4)* p5) % p
        p3 = ((p-3)* p4) % p
        p2 = 1
        p1 = p-1
        total += (p1 + p2 + p3 + p4 + p5) % p
                  
    return total

def compute2():
    limit = 9999999
    primes = eulerlib.primes(limit)[2:]
    print("done")
    print("--- %s seconds ---" % (time.time() - start_time))
    total = 0
    for p in primes:
        #S(p) = (p-5)![(p-1)(p-2)(p-3)(p-4) + (p-2)(p-3)(p-4) + (p-3)(p-4) + (p-4)] mod p
        #     = 9*(p-5)! mod p
        #(p-2)(p-3)(p-4)(p-5)! = 1 mod p
        #(p-5)! = inverse((p-2)(p-3)(p-4), mod p)

        total += (-3*pow(8, -1, p)) % p
                  
    return total

if __name__ == "__main__":
    #print(compute())
    print(compute2())
    print("--- %s seconds ---" % (time.time() - start_time))