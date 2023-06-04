#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:49:32 2021

@author: igorvanloo
"""

'''
Project Euler Problem 179

Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors. 
For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

Reasoning

Generate an array that is 1 + 10^7 long which looks like values = [0,1,1,1,1, .... ,1,1,1]

Now create 2 loops, for x and y, x will be values from 1 to 10^7 / 2, y will be from 1 to 10^7 / x

This is so that when we go through both of the loops x*y will create every single number from 1 to 10^7

Now each position in the array represents numbers, so we can see that when x = 2 x*y = [2,4,6,8,....]
and correspondingly those numbers have the divisors 2, so we continue the process and make values[x*y] += 1

Found a new solution using greatest prime factor sieve
Anwser:
    986262
--- 24.348713874816895 seconds ---
--- 5.308513879776001 seconds --- Using gpf sieve
'''

import time, math
start_time = time.time()

def old(limit):
    values = [0] + [1] * limit
    
    for x in range(2,int(limit/2) + 1):
        for y in range(1,int(limit/x)+1):
            values[x*y] += 1
    
    count = 0
    for z in range(limit-1):
        if values[z] == values[z+1]:
            count += 1
    return count

def gpf_sieve(N):
    #smallest prime factor sieve
    gpf = [i for i in range(N + 1)]
        
    for i in range(2, int(math.sqrt(N)) + 1):
        if gpf[i] == i:
            for j in range(i*i, N + 1, i):
                gpf[j] = i
    return gpf

def compute(limit):
    gpf = gpf_sieve(limit + 1)
    d = gpf
    for i in range(2, limit + 2):
        if gpf[i] == i:
            d[i] = 2
        else:
            #We use the fatc that d_array[n] = (e + 1) * d_array[n/p^e]
            p = gpf[i]
            t = i // p
            e = 2
            while t % p == 0:
                e += 1
                t //= p
            d[i] = d[t]*e
    count = 0
    for z in range(limit-1):
        if d[z] == d[z+1]:
            count += 1
    return count
    
if __name__ == "__main__":
    print(compute(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))