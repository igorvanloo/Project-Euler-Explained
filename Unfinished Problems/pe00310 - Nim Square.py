#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 21:12:34 2022

@author: igorvanloo
"""
'''
Project Euler Problem 310

we use https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem again, same as problem 306

Find all nim values for all possible heaps

then for each triplet, if the sum of num valyes is even, player 1 wins

Anwser:

'''
import time, math
start_time = time.time()

def mex(alist):
    mex = 0
    while mex in alist:
      mex += 1
    return mex

def compute(limit):
    array = [0]*(limit + 1)
    squares = [x*x for x in range(1, int(math.sqrt(limit)) + 1)]
    
    for x in range(1, len(array)):
        mex_list = set([])
        for sq in squares:
            if sq <= x:
                mex_list.add(array[x - sq])
            else:
                break
        array[x] = mex(mex_list)
    
    count = 0
    for a in range(limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                if (array[a] ^ array[b] ^ array[c]) == 0:
                    count += 1
    return count

if __name__ == "__main__":
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
