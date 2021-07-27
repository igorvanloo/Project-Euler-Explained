#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 12:50:03 2021

@author: igorvanloo
"""

'''
Project Euler Problem 743

Anwser:
    259158998
--- 260.2642171382904 seconds ---
'''

import time, math

def smartbin(n,k):
    total = 1
    for i in range(1,k+1):
        total *= ((n+1-i))
        total *= pow(i, -1, 1000000007)
        total %= 1000000007
    return int(total) % 1000000007

def A(k,n): 
    total = 0
    for x in range(0, math.floor(k/2) + 1):
        total += pow(2,int(n*(k-2*x)/k), 1000000007) * smartbin(k, x) * smartbin(k-x,x)
        total %= 1000000007
    return total % 1000000007

def A1(k,n): #faster version
    total = 0
    f0 = 1
    modulo = 1000000007
    power = pow(2, n//k, modulo)
    
    for a in range(0, n//k + 1):
        total += ((f0 * pow(power, k-2*a, modulo))) % modulo
        f0 *= ((k-2*a)*(k-2*a-1)) % modulo
        f0 *= (pow((a+1)**2, -1, modulo)) % modulo
    return total % modulo

if __name__ == "__main__":
    start_time = time.time()
    print(A1(10**4, 10**8))
    print("--- %s seconds ---" % (time.time() - start_time))