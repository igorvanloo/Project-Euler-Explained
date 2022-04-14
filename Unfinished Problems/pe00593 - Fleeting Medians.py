#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:52:15 2022

@author: igorvanloo
"""

'''
Project Euler Problem 593

Get both correct test cases, but it is way too slow, haven't figured out the trick yet
Anwser:

'''
import time, math
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2*i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def M(i, j, S_2):
    values = S_2[i:j+1]
    values = sorted(values)
    if len(values) % 2 == 0:
        return (values[len(values)//2 - 1] + values[len(values)//2])/2
    else:
        return values[len(values)//2]

def F(n, k, S_2):
    total = 0
    for i in range(1, n - k + 2):
        if i % 1000 == 0:
            print(i)
        total += M(i, i + k - 1, S_2)
    return total  
    
def compute(n, x):
    primes = [0] + list_primes(10**8)
    print("primes done")
    mod = 10007
    S = [0]*(n + 1)
    for k in range(1, len(S)):
        S[k] = pow(primes[k], k, mod)
    #print(S)
    
    S_2 = [0]*(n + 1)
    for k in range(1, len(S_2)):
        S_2[k] = S[k] + S[math.floor(k/10000) + 1]
    #print(sorted(S_2))
    
    return F(n, x, S_2)

if __name__ == "__main__":
    print(compute(10**6, 10**5))
    print("--- %s seconds ---" % (time.time() - start_time))