#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:33:44 2022

@author: igorvanloo
"""
'''
Project Euler Problem 306

https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem

Solving problem 301 led me to Sprague Grundy theorem, coded it up and got to 10^4 quite quickly, couldn't progress so I searched up
up each case where we lost and won, hoping to find something on oeis and tada https://oeis.org/A215721

Shoulds that for n > 14 a(n) = a(n-5) + 34

Anwser:
    852938
--- 0.09212303161621094 seconds ---
'''
import time
start_time = time.time()

def mex(alist):
    mex = 0
    while mex in alist:
      mex += 1
    return mex
    
def compute(limit):
    array = [0] * (limit + 1)
    array[2] = 1
    
    losses = [0, 1]
    x = 3
    while len(losses) != 14 and x < limit:
        mex_list = set([])
        for y in range(x//2):
            if y == 0:
                t = array[x - 2]
            else:
                t = array[y]^array[x - y - 2]
            mex_list.add(t)
        array[x] = mex(mex_list)
        if array[x] == 0:
            losses.append(x)
        x += 1
    if len(losses) == 14: 
      n = 14
      while losses[n - 5] + 34 < limit:
          losses.append(losses[n - 5] + 34)
          n += 1
    return limit - len(losses) + 1       

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))
