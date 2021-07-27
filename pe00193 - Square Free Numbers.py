#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 01:17:08 2021

@author: igorvanloo
"""

'''
Project Euler Problem 193

Almost complete copy paste from Problem 745

Approximate anwser = 6*2**50 / (math.pi)**2 = 684465067344555

Anwser:
    684465067343069
--- 110.54865097999573 seconds ---
'''
import time, math

def S1(N): #Reduced speed for 10^8 ~ 0.02 seconds, can be used to solve final problem
    sqrtN = int(math.sqrt(N))
    a = [0] + [1]*sqrtN
    for i in range(sqrtN,1,-1):
        if i % 10**6 == 0:
            print(i)
        a[i] = math.floor(N/(i*i)) - sum([a[i*j] for j in range(2,math.floor(sqrtN/i) + 1)])
    return N - sum([a[i] for i in range(len(a))]) + 1

if __name__ == "__main__":
    start_time = time.time()
    print(S1(2**50))
    print("--- %s seconds ---" % (time.time() - start_time))