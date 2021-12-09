#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:58:08 2021

@author: igorvanloo
"""

'''
Project Euler Problem 759

f(1) = 1
f(2n) = 2f(n)
f(2n+1) = 2n + 1 + 2f(n) +f(n)/n = 2n + 1 + f(2n)(1+1/2n) = 2n + 1 + f(2n)((2n+1)/2n) = (2n + 1)(1 + f(2n)/2n)

f(1) = 1

n = 1 
f(2) = 2
f(3) = 3 + 2f(1) + f(1)/1 = 6

n = 2
f(4) = 4
f(5) = 5 + 2f(2) + f(2)/2 = 5 + 4 + 1 = 10

n = 3
f(6) = 2f(3) = 12
f(7) = 7 + 2f(3) + f(3)/3 = 7 + 12 + 2 = 21

f(n) = n*(number of 1's in the base 2 conversion of n)
https://oeis.org/A245788

Anwser:
    
'''

import time, math
start_time = time.time()

def compute(limit):
    f = [0,1]
    
    for x in range(1,int(limit/2) + 1):
        f += [2*f[x], int(2*x + 1 + 2*f[x] + f[x]/x)]
    
    #print(f)
    return sum([pow(x,2,1000000007) for x in f[1:limit + 1]]) % 1000000007

def compute1(limit):
    return sum([pow(n*bin(n)[2:].count('1'),2,1000000007) for n in range(limit + 1)]) % 1000000007

if __name__ == "__main__":
    print(compute(10**4))
    #print(compute1(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))