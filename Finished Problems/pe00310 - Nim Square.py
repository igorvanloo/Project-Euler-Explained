#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 21:12:34 2022

@author: Igor Van Loo
"""
'''
Project Euler Problem 310

we use https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem again, same as problem 306

Calculate sprague-grundy value for a single heap, then XOR the 3 heaps, if the value is 0, then the position is losing for the next player

We want sa ^ sb ^ sc = 0 <=> sa = sb ^ sc

Anwser:
    2586528661783
--- 2556.0157606601715 seconds ---
--- 77.06826639175415 seconds --- with pypy
'''
import time, math
start_time = time.time()

def mex(L):
    for i in range(len(L)):
        if L[i] == 0:
            return i
    return len(L)

def brute_force(limit):
    
    sG_cache = [-1]*(limit + 1)
    def sG(x):
        
        if x == 0:
            sG_cache[x] = 0
            return 0
        
        if sG_cache[x] != -1:
            return sG_cache[x]
        
        vec = []
        for i in range(int(math.sqrt(x)), 0, -1):
            v = sG(x - i*i)
            if v >= len(vec):
                vec += [0]*(v + 10 - len(vec))
            vec[v] = 1
        
        sG_cache[x] = mex(vec)
        return sG_cache[x]
    
    total = 0
    for a in range(limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                if sG(a) ^ sG(b) ^ sG(c) == 0:
                    total += 1
    return total

def compute(limit):
    
    sG_cache = [-1]*(limit + 1)
    def sG(x):
        
        if x == 0:
            sG_cache[x] = 0
            return 0
        
        if sG_cache[x] != -1:
            return sG_cache[x]
        
        vec = []
        for i in range(int(math.sqrt(x)), 0, -1):
            v = sG(x - i*i)
            if v >= len(vec):
                vec += [0]*(v + 10 - len(vec))
            vec[v] = 1
        
        sG_cache[x] = mex(vec)
        return sG_cache[x]
    
    total = 0
    freq = {}
    for a in range(limit, -1, -1):
        b = a
        for c in range(b, limit + 1):
            v = sG(b) ^ sG(c)
            if v in freq:
                freq[v] += 1
            else:
                freq[v] = 1
        t = sG(a)
        if t in freq:
            total += freq[t]
    return total

if __name__ == "__main__":
    print(compute(100000))
    print("--- %s seconds ---" % (time.time() - start_time))
