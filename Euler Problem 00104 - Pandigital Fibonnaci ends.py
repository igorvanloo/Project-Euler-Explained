#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:33:56 2021

@author: igorvanloo
"""
'''
Project Euler Problem 104

Key is keeping track of last 9 numbers by doing mod 10^10
and keeping track of first 9 numbers by not letting one set of numbers get bigger that 10^10

Anwser:
329468
--- 17.35551619529724 seconds ---    
'''

import time
start_time = time.time()

def matrixmultiplication(x,y):
    #[x[0][0], x[0][1]]    [y[0][0], y[0][1]]
    #[x[1][0], x[1][1]]    [y[1][0], y[1][1]]
    return [[x[0][0]*y[0][0] + x[0][1]*y[1][0], x[0][0]*y[0][1] + x[0][1]*y[1][1]],[x[1][0]*y[0][0] + x[1][1]*y[1][0], x[1][0]*y[0][1] + x[1][1]*y[1][1]]]

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return str(v2)[:9]

def compute():
    S = set("123456789")
    f1last9, f2last9, f1first9, f2first9, i = 1, 1, 1, 1, 2
    while set(str(f2last9 % 10**9)) != S or set(str(f2first9)[:9]) != S:
        f1last9, f2last9, f1first9, f2first9, i = f2last9, f1last9 + f2last9, f2first9, f2first9 + f1first9, i + 1
        if f2first9 > 10**9:
            f1first9, f2first9 = f1first9 / 10, f2first9 / 10

    return i

def compute1(a, b, k):
    
    S = [str(x) for x in range(1,k+1)]
    f1 = a
    f2 = b
    count = 2
    while True:
        count += 1
        fn = (f2 + f1) % 10**9
        
        if sorted(list(str(fn))) == S:
            #print(count)
            if sorted(list(fib(count))) == S:
                return (count)
                break
        f1 = (f2 % 10**9)
        f2 = fn
    
    
if __name__ == "__main__":
    print(compute1(1,1,9))
    print("--- %s seconds ---" % (time.time() - start_time))
    
    