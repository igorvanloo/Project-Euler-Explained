#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:11:48 2022

@author: igorvanloo
"""
'''
Project Euler Problem 234

Lets call the limit N

Find all prime factors less than sqrt(N) and then next prime factor
then we check each pair of consecutive primes

for example 3, 5 now all numbers between 3*3 and 5*5 (9, 10, 11, 12, 13, 14, 25) will have lps = 3 ups = 5

Lets check the sum of those numbers divisble by 3
up till 15 there are 15//3 = 5 number divisible by 3 (3, 6, 9, 12, 15) the sum is (5*(6*3))/2
up till 8 there are 8//3 = 2  numbers (3, 6) the sum is (2*(3*3))/2
therefore total sum is 45-9 = 36

Anwser:
    1259187438574927161
--- 1.3137469291687012 seconds ---
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
    
def sumseq(ups, lps, limit):
    total = 0
    for x in range(lps*lps + lps, min(ups*ups, limit + 1), lps):
        total += x
    for x in range(ups*ups, lps*lps, -ups):
        if x < min(ups*ups, limit + 1):
            total += x
    for x in range(ups*lps, min(ups*ups, limit + 1), lps*ups):
        total -= 2*x
    return total
    
def compute(N):
    sqrt_limit = math.floor(math.sqrt(N))
    primes = list_primes(sqrt_limit + 100)
    total = 0
    for x in range(len(primes) - 1):
        p1 = primes[x]
        p2 = primes[x + 1]
        if p1*p1 > N:
            break
        total += sumseq(p2, p1, N)
    return total
        
if __name__ == "__main__":
    print(compute(999966663333))
    print("--- %s seconds ---" % (time.time() - start_time))
