#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:01:05 2022

@author: igorvanloo
"""
'''
Project Euler Problem 200

We shall define a sqube to be a number of the form, p^2q^3, where p and q are distinct primes.
For example, 200 = 5^2 * 2^3 or 120072949 = 23^2 * 61^3.

The first five squbes are 72, 108, 200, 392, and 500.

Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; we shall call such numbers, prime-proof. The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.

Find the 200th prime-proof sqube containing the contiguous sub-string "200"

Anwser:
    229161792008
--- 5.06461501121521 seconds ---
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

def fermat_primality_test(n):
    if pow(4, n - 1, n) == 1 and pow(6, n - 1, n) == 1:
        return True
    return False

def prime_proof_checker(x):
    
    og = list(str(x))
    number = list(str(x))
    prime_proof = True
    
    for pos in range(len(number)):
        if pos == 0:
            for x in range(1, 10):
                number[pos] = str(x)
                if fermat_primality_test(int("".join(number))):
                    prime_proof = False
            
        else:
            for x in range(0, 10):
                number[pos] = str(x)
                if fermat_primality_test(int("".join(number))):
                    prime_proof = False
        number[pos] = og[pos]
        if prime_proof == False:
            return False
    
    return True
    
def string_checker(x):
    if "200" in str(x):
        if prime_proof_checker(x):
            return True
    return False
    
def compute(limit):
    primes = list_primes(10**6)
    candidates = []
    count = 0
    for a in range(len(primes)):
        for b in range(a + 1, len(primes)):
            
            p = primes[a]
            q = primes[b]
            
            x = p*p*q*q*q
            y = p*p*p*q*q
            if x > limit and y > limit:
                break
            
            if x < limit:
                if string_checker(x):
                    candidates.append(x)
                    count += 1
                    print(x, count)
            
            if y < limit:
                if string_checker(y):
                    candidates.append(y)
                    count += 1
                    print(y, count)
            
    candidates = sorted(candidates)
    return candidates[199]
    
        

if __name__ == "__main__":
    print(compute(10**13))
    print("--- %s seconds ---" % (time.time() - start_time))
