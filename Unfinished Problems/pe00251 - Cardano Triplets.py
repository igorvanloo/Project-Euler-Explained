#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:23:33 2022

@author: igorvanloo
"""
'''
Project Euler Problem 251

8a^3 + 15a^2 + 6a - 27b^2c = 1
c = (8a^3 + 15a^2 + 6a - 1)/27b^2
if b = 0 then 2a^(1/3) = 1 => a = 1/8 is the only solution which is not an integer so we can skip b = 0 case
I notice that a is always of the form 3k + 2
this leads to 27(k + 1)^2(8k + 5) = 27b^2c => b^2c = (k + 1)^2(8k + 5)
we want a + b + c <= limit, therefore fix k we then have (3k + 2) + b + c <= limit and b^2c = (k + 1)^2(8k + 5)
This is minimal when b = 2c

This problem comes down to factoring b^2c efficiently and matching square divisors

b^2c = (k + 1)^2(8k + 5), let (8k + 5) = p^2q then we have (k + 1)^2p^2q = b^2c where b = (k+1)p/d, c = q/d^2

Alternate:

b^2 | (8a^3 + 15a^2 + 6a - 1)/27 and c = (8a^3 + 15a^2 + 6a - 1)/27b^2

Therefore we go through the divisors, d, of (8a^3 + 15a^2 + 6a - 1)/27, if d*d divides (8a^3 + 15a^2 + 6a - 1)/27, then we have found
a (b, c) pair
My own divisors function is too slow so I use sympy's divisor function with an early exit, but it is still too slow

Anwser:

'''
import time, math
from sympy import divisors

start_time = time.time()

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                if d in factors:
                    factors[n] += 1
                else:
                    factors[n] = 1
            break
    return factors

def compute(limit):
    count = 0
    new_limit = math.floor((limit - 2)/6.5) + 1
    for k in range(new_limit):
        print(k)
        t = (k + 1)*(k + 1)*(8*k + 5)
        a = 3*k + 2
        #let p = k +1, q = 8k + 5
        p = prime_factors(k + 1)
        q = prime_factors(8*k + 5)
        pf = {}
        for x in p:
            pf[x] = 2*p[x]
        for x in q:
            if x in pf:
                pf[x] += q[x]
            else:
                pf[x] = q[x]
        
        square_divisors = []
        for p in pf:
            for i in range(math.floor(math.log(pf[p], 2)) + 1):
                square_divisors.append(pow(p, i))
        
                
    return count

def compute2(limit):
    '''
    16916 - 10^5
    --- 6.018966913223267 seconds ---
    171128 - 10^6
    --- 118.07689690589905 seconds ---
    '''
    count = 0
    done = 1
    new_limit = math.floor((limit - 2)/6.5) + 1
    for k in range(new_limit):
        if k > done*10000:
            print(round(100*k/new_limit, 3))
            done += 1
        
        a = 3*k + 2
        t = (((8*a + 15)*a + 6)*a -1)//27
                
        for c in divisors(t):
            if c <= min(math.sqrt(t), limit - a + 1):
                if t%(c*c) == 0:
                    b = t//(c*c)
                    if a + b + c <= limit:
                        count += 1
            else:
                break
    return count
        
if __name__ == "__main__":
    print(compute2(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
