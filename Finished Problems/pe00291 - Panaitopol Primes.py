#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:54:28 2022

@author: igorvanloo
"""
'''
Project Euler Problem 

p is a Panaitopol prime if p = (x^4 + y^4)/(x^3 + y^3) = (x - y)(x^2 + y^2)/(x^2 -xy + y^2)

Brute force leads us to https://oeis.org/A027862 which are primes of the form n^2 + (n^2 + 1)

Anwser:
    4037526
--- 668.2800509929657 seconds ---
'''
import time, math
start_time = time.time()

def is_prime(x):  # Test if giving value is a prime
    if x <= 1:
        return 0
    elif x <= 3:
        return 1
    elif x % 2 == 0:
        return 0
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return 0
        return 1
            
def fermat_primality_test(n, tests):
    if n < 10**5:
        return is_prime(n)
    else:
        for x in range(tests):
            if pow(2*(x + 2), n - 1, n) != 1:
                return 0
        return 1

def compute(limit):
    count = 0
    for n in range(1, int(math.sqrt((limit - 1)/2)) + 1):
        p = 2*n*n + 2*n + 1
        if p >= limit:
            break
        count += fermat_primality_test(p, 5)
    return count

if __name__ == "__main__":
    print(compute(5*10**15))
    print("--- %s seconds ---" % (time.time() - start_time))
