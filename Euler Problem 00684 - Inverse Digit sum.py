#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:56:17 2020

@author: igorvanloo
"""

'''
Project Euler Problem 684

Anwser:
    922058210
--- 0.0007109642028808594 seconds ---
    
'''

import time, math, eulerlib, itertools

start_time = time.time()

def fibonnaci(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    
    f1 = 1
    f2 = 1
    fib_numbers = [0, f1, f2]
    while len(fib_numbers) < x:
        fn = f1 + f2
        fib_numbers.append(fn)
        f1 = f2
        f2 = fn
    return fib_numbers

def sn(b):
    return ((b % 9 + 1)*(pow(10,(b // 9), 1000000007)) - 1) % 1000000007

def S(k,N=1000000007):
    return (pow(10,k//9,N)*(6+(k%9)*(k%9+3)//2)-6-k)%N

def MyS(k):
    q = k // 9
    r = k % 9
    sum1 = (6*(pow(10,q,1000000007) - 1)) - (9*q % 1000000007)
    sum2 = sum([i*pow(10,q,1000000007) - 1 for i in range(2,r+2)])
    return (sum1+sum2) % 1000000007

def finals(k):
    q = k // 9
    r = k % 9
    
    return (6*(pow(10,q,1000000007) - 1) - (9*q % 1000000007) + (r/2)*(r*pow(10,q,1000000007) + 3*pow(10,q,1000000007) - 2)) % 1000000007
    
def compute():
    total = 0
    temp_list = fibonnaci(92)
    for x in range(2,91):
        total += S(temp_list[x])
    return total % 1000000007

def compute1():
    total = 0
    temp_list = fibonnaci(92)
    for x in range(2,91):
        total += MyS(temp_list[x])
    return total % 1000000007

def compute2():
    total = 0
    temp_list = fibonnaci(92)
    for x in range(2,91):
        total += finals(temp_list[x])
    return total % 1000000007

if __name__ == "__main__":
    print(compute())
    print(compute1())
    print(compute2())
    print("--- %s seconds ---" % (time.time() - start_time))