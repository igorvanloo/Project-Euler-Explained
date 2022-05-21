#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:13:58 2022

@author: igorvanloo
"""
'''
Project Euler Problem 266

The divisors of 12 are: 1,2,3,4,6 and 12.
The largest divisor of 12 that does not exceed the square root of 12 is 3.
We shall call the largest divisor of an integer n that does not exceed the square root of n the pseudo square root (PSR) of n.
It can be seen that PSR(3102)=47.

Let p be the product of the primes below 190.
Find PSR(p) mod 1016

ln(2) + ln(3) + ... + ln(181) = ln(5397346292805549782720214077673687806275517530364350655459511599582614290) = 167.47203410109333

Now we want to find a subset of [ln(2), ln(3), ..., ln(181)] such that its sum is closest to 83.73601705054666

This is familiar to the knapsack problem, should be fun to try and implement


Anwser:

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

def prod(alist):
    total = 1
    for x in alist:
        total *= x
    return total
    
def psr(n):
    for x in range(int(math.sqrt(n)), 0, -1):
        if n % x == 0:
            return x

def KnapSack(values, weights, n, W, no_values = True):
    array = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                array[i][j] = 0
                
            elif weights[i - 1] > j:
                array[i][j] = array[i-1][j]
            else:
                array[i][j] = max(array[i - 1][j], array[i - 1][j - weights[i - 1]] + values[i - 1])
    
    if no_values:
        return array[n][W]
    if not no_values:
        return array
    
def KnapSackValues(values, weights, n, W):
    array = KnapSack(values, weights, n, W, no_values = False)
    if n == 0:
        return {}
    if array[n][W] > array[n - 1][W]:
        return {weights[n - 1]}.union(KnapSackValues(values, weights, n - 1, W - weights[n - 1]))
    else:
        return KnapSackValues(values, weights, n - 1, W)
    
def compute(limit):
    cons = 1000
    primes = list_primes(limit)[::-1]
    
    weights = [int(math.log(p)*cons) for p in primes]
    n = len(weights)
    values = [1]*n
    W = int(math.log(prod(primes))*(cons//2))
    
    optimal = KnapSackValues(values, weights, n, W)
    print(optimal)
    total = 1
    
    for x in optimal:
        total *= primes[weights.index(x)]
        total %= 10**16
    return total

if __name__ == "__main__":
    print(compute(10))
    print("--- %s seconds ---" % (time.time() - start_time))
