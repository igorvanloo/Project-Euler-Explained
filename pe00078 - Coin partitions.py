#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:29:37 2021

@author: igorvanloo
"""

'''
Project Euler Problem 77

g(k) = (3*k*k - k)/2 for k = 1,-1,2,-2,...
p(n) = sum (-1)^(k-1) * p(n- g(k)), p(n) = 0 for all n < 0

Anwser:
    55374
--- 4.500371932983398 seconds ---
'''

import time, math, eulerlib

def Partition(goal, alist, divisor): #Works but It is quite slow
    ways = [1] * (goal+1)
    for options in alist:
        for i in range(len(ways) - options):
            ways[i + options] += ways[i]
    
    for x in range(len(ways)):
        if ways[x] % divisor == 0:
            return x
    
def PentagonalNumberTheorem(N):
    #this will use the pentagonal number theorem
    p = [1] + [0]*(N + 1)
        
    for n in range(1,len(p)):
        y = 1
        while True:            
            if y % 2 == 0:
                sign = -1
            else:
                sign = 1
            
            pen = (3*y*y - y)//2
            if pen > n:
                break
            
            p[n] += sign*p[n-pen]
            
            pen += y
            if pen > n:
                break
            
            p[n] += sign*p[n-pen]
            y += 1
        
        if p[n] % 10**6 == 0:
            return n
        
if __name__ == "__main__":
    start_time = time.time()
    print(PentagonalNumberTheorem(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))