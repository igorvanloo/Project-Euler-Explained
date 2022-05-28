#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:44:37 2022

@author: igorvanloo
"""
'''
Project Euler Problem 281

Using Cauchy Frobenius lemma/Polya enumeration theorem

We have |S\G| = 1/m*n sum_{d|m*n} phi(d)x_d^(m*n/d)

we replace x_d with a^i + b^i + ... + c^i which represent the colours, and we search for the co-efficient a^nb^n...c^n

Anwser:
    1485776387445623
--- 0.0007867813110351562 seconds ---
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
            phi *= (d ** (count - 1)) * (d - 1)
        d = d + 1
        if d * d > n:
            if n > 1:
                phi *= int(n - 1)
            break
    return phi

def f(m, n):
    return sum([phi(n//d) * math.factorial(m*d) // pow(math.factorial(d), m) for d in range(1, n + 1) if n % d == 0])//(m*n)

def compute(limit):
    total = 0
    for m in range(2, 100):
        for n in range(1, 100):
            t = f(m, n)
            if t <= limit:
                total += t
            else:
                break
    return total

if __name__ == "__main__":
    print(compute(10**16))
    print("--- %s seconds ---" % (time.time() - start_time))