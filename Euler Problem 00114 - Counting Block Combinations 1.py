#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:02:56 2021

@author: igorvanloo
"""

'''
Project Euler Problem 114

let c(n,m) denote the number of ways to cover n tiles with red tiles of minimum length m

let cr(n,m) denote number of ways to cover n tiles ending in a red tile
let cg(n,m) denote number of ways to cover n tiles ending in a grey tile

c(n,m) = cr(n,m) + cg(n,m)                     (1)
cg(n,m) = cr(n-1,m) + cg(n-1,m) = c(n-1,m)     (2) because adding a black tile at the end does not change anything so we have
cr(n,m) = cr(n-1,m) + cg(n-m,m)                (3) because we can either we adding a red tile to a n-1 or adds a length n-m red tile to a black tile
cr(n,m) = c(n-1,m) - cg(n-1,m) + cg(n-m,m)        substiute equation (1)
cr(n,m) = c(n-1,m) - c(n-2,m) + c(n-m-1,m)        substitute equation (2)

substitute (2), (3) back into (1)
c(n,m) = 2*c(n-1,m) - c(n-2,m) + c(n-m-1,m)

note c(0,m) = ... = c(m-1,m) = 1

we are looking for c(50,3) thereofre c(50,3) = 2*c(49,3) - c(48,3) + c(46,3) = ....
with intial values c(-1,3) = c(0,3) = c(1,3) = c(2,3) = 1

Anwser:
    16475640049
--- 9.393692016601562e-05 seconds ---
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute(limit):
    c0 = 1
    c1 = 1
    c2 = 1
    c3 = 2
    
    n = 3
    
    while True:
        cn = 2*c3 - c2 + c0
        c0 = c1
        c1 = c2
        c2 = c3
        c3 = cn
        
        n += 1
        if n == limit:
            break
    return cn

if __name__ == "__main__":
    print(compute(100))
    print("--- %s seconds ---" % (time.time() - start_time))