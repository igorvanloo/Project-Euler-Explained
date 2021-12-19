#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:53:12 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

From OEIS: https://oeis.org/A064602

a(n) = Sum_{k=1..s} (A000330(floor(n/k)) + k^2*floor(n/k)) - s*A000330(s), s = floor(sqrt(n))

A000330(n) = n*(n+1)*(2*n+1)/6

How to derive the above?

It is quite easy to realise that we are looking for sum_(k = 1 to n) k^2 * floor(n/k) because a divisor i, will divide floor(n/i) numbers
However this will be an O(n) time program, which is too slow for 10^15,

The key is to note that for all p > n/2, floor(n/p) = 1 for all n/2 ≥ p > n/3 floor(n/p) = 2, etc

This way we can group all of the terms together

We then have 

sum_(k = 1 to n) k^2 * floor(n/k) = sum_(k = 1 to sqrt(n)) k^2 * floor(n/k) + sum_(k = sqrt(n) to n) k^2 * floor(n/k)

= sum_(k = 1 to sqrt(n)) k^2 * floor(n/k) + sum_(l = 1 to sqrt(n)) l * sum_{floor(n/(l + 1)) < k < floor(l/k)} k^2
                                  
let f(n) = n*(n+1)*(2*n+1)/6,

then sum_(k = 1 to sqrt(n)) k * sum_{n/(l + 1) < k < floor(n/l)} = f(floor(n/l)) - f(floor(n/(l + 1)))

As we iterate through l we will have 

sum_(l = 1 to sqrt(n)) l * sum_{floor(n/(l + 1)) < k < floor(l/k)} k^2 = 1*(f(n) - f(floor(n/(l + 1)))) + 2*(floor(n/(l + 1)) - f(floor(n/(l + 2))))

+ .. + n*(f(floor(n/sqrt(n) - 1)) - f(floor(sqrt(n)))) = sum_(k = 1 to sqrt(n)) f(floor(n/k)) - sqrt(n)*f(floor(sqrt(n)))
Anwser:
    281632621
--- 39.543633222579956 seconds ---
'''

import time, math
start_time = time.time()

def f(n):
    return (n*(n+1)*(2*n+1))//6

def compute(n):
    total = 0
    mod = 10**9
    s = int(math.floor(math.sqrt(n)))
    
    for k in range(1, s + 1):
        x = (n//k)
        t = f(x)
        total += (t % 10**9)
        total += pow(k, 2, mod) * x
        total %= mod
        
    total -= s*f(s)
    
    return total % mod

if __name__ == "__main__":
    print(compute(10**15))
    print("--- %s seconds ---" % (time.time() - start_time))