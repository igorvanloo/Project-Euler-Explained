#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:21:45 2022

@author: igorvanloo
"""
'''
Project Euler Problem 249

Contiuously build sets

The maxixmum sum is 1548136

Idea is to have an array that stores number of ways to create x

For example 
array[0] = 1, {}
array[2] = 1, {2}
array[3] = 1, {3}
array[5] = 2, {5}, {2, 3}

I initialize the array as [1, 0, 0, ...], and curr_largest = 1
then I use p = 2
I run through array from 0 to largest 
array[0 + 2] = 1, curr_largest = 3

then I use p = 3
I run through array from 0 to largest
array[0 + 3] = array[0] = 1
array[1 + 3] = array[1] = 0
array[2 + 3] = array[2] = 1, curr_largest = 6

etc

10 = 2 + 3 + 5 = 7 + 3 = 8 + 2

This method will end up overcounting solutions

What about if I count backwards from curr_largest? That should stop the overcount
So instead I run through largest-1 to 0 and perform the same operations

Anwser:
    9275262564250418
--- 121.81318783760071 seconds ---
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
    mod = 10**16
    primes = list_primes(limit)
    SUM = sum(primes)
    primality = list_primality(SUM)
    array = [1] + [0]*SUM
    
    curr_largest = 1
    for p in primes:
        for x in range(curr_largest-1, -1, -1):
            array[x + p] += array[x]
            array[x + p] %= mod
        curr_largest += p
                
    return sum([array[x] for x in range(len(array)) if primality[x]]) % mod

if __name__ == "__main__":
    print(compute(5000))
    print("--- %s seconds ---" % (time.time() - start_time))
