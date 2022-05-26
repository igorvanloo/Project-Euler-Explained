#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:11:21 2022

@author: igorvanloo
"""
'''
Project Euler Problem 274

brute force works quickly for up to 10,000

Lets think of a smarter way, we have a number p
decompose it into 10a + b = 0 mod p, therefore if we have an n such that 10n = 1 mod p
then we can do n(10a + b) = a + nb = 0 mod p which is exactly what we want
n = (10)^(-1) mod p

Anwser:
    1601912348822
--- 2.6436920166015625 seconds ---
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

def find_divisibility_bf(p):
    if p == 3:
        start = 12
    elif p == 7:
        start = 14
    else:
        start = p
    last_digit = start%10
    rest_digits = (start - last_digit)//10
    for m in range(2, p):
        if (rest_digits + m*last_digit) % p == 0:
            return m
    return 1
    
def compute(limit):
    primes = list_primes(limit)
    primes.remove(2)
    primes.remove(5)
    total = 0
    for p in primes:
        if p == 3:
            total += 1
        elif p == 7:
            total += 5
        else:
            total += pow(10, -1, p)
    return total

if __name__ == "__main__":
    print(compute(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))
