#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:40:46 2021

@author: igorvanloo
"""

'''
Project Euler Problem 129

Proof of Claim:

Let n be an integer such that gcd(10,n) = 1

Now take a set of repunits {R(1) mod n, R(2) mod n, ..., R(n+1) mod n} there are obviously n choice for remainders
mod n, {0,1,2,...,n-1}, therefore by the pigeonhole principle there must be an R(i) = R(j) mod n, where i > j
Therefore R(i) - R(j) = 0 mod n and now note that R(i) - R(j) = R(k)*10^a and because gcd(10,n) = 1 n must divide R(k)

Now we can namely notice that R(k) < R(i) <= R(n+1) => k <= n.
Therefore if we want an n such that n|R(k), k > 10^6, we must have that n >= 10^6

Anwser:
    1000023
--- 4.162177085876465 seconds ---
'''
    
import time, math
start_time = time.time()

def compute(limit):
    
    n = 10**6
    valuenotfound = True
        
    while valuenotfound == True:
        if math.gcd(n, 10) == 1:
            l = 1
            while True:
                if pow(10,l,9*n) == 1:
                    break
                l += 1
                if l > limit:
                    value = n
                    valuenotfound = False
        n += 1

    return value

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))