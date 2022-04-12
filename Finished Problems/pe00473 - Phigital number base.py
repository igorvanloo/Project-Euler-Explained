#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:01:40 2022

@author: igorvanloo
"""
'''
Project Euler Problem 473

1) f(n) = (φ^n - (-φ)^-n)/√(5)
    1.1) φ^n + (φ)^-n = √(5)f(n) if n is odd
    1.2) φ^n + (φ)^-n = √(5)f(n) - 2(φ)^-n
2) φ^n = f(n)φ + f(n-1))
3) φ^(-n) = (-1)^(n+1) (f(n)φ - f(n + 1)))
4) (φ)^n + (φ)^(-n - 1) = (f(n) + f(n + 1))φ + (f(n - 1) - f(n + 2)), when n is even
5) (φ)^n + (φ)^(-n - 1) = (f(n) - f(n + 1))φ + (f(n - 1) + f(n + 2)), when n is odd


Anwser:
    10^5 - 3517491
    10^6 - 51883315
    10^7 - 2218435383
    10^8 - 43116488159
    10^9 - 634787225557 - for some reason this one is slow so I added a stopper
    10^10 - 35856681704365
    35856681704365
--- 0.5208139419555664 seconds ---
'''
import time, math
from decimal import *
start_time = time.time()

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2

def Fibtill(x):
    fibnumbers = [0]
    n = 1
    while len(fibnumbers) != x:
        fibnumbers.append(fibonnaci(n))
        n += 1
    return fibnumbers

def values(limit):
    g_r = (1 + math.sqrt(5))/2
    x = math.ceil(math.log(limit, g_r))
    v = [g_r**n for n in range(0, - x - 1, -1)]
    return v, x

def compute(limit):
    getcontext().prec = 20
    g_r = Decimal(1 + Decimal(5).sqrt())/Decimal(2)
    pow_lim = math.ceil(math.log(limit, g_r))
    f = Fibtill(pow_lim + 50)
    
    possib = []
    for n in range(1, pow_lim + 1):
        if n % 2 == 0:
            t = Decimal(f[n] + f[n + 1])*Decimal(g_r) + (f[n - 1] - f[n + 2])
        else:
            t = Decimal(f[n] - f[n + 1])*Decimal(g_r) + (f[n - 1] + f[n + 2])
        
        if t < limit:
            possib.append(t)
            
    print("possib are done")
    print(possib)
    principal = [1, 2]
    derived = set()
    
    main = [[2, [1, 0]]]
    sub = [[2, [1, 0]]]
    for x in range(1, len(possib) - 2):
        for y in range(x + 2, len(possib)):
            t = Decimal(possib[x]) + Decimal(possib[y])
            if t < limit:
                if round(t, 1) == t:
                    principal.append(t)
                    main.append([t, [x, y]])
                    sub.append([t, [x, y]])  
    
    print("main and sub are done")
    sub = sorted(sub)
    count = 0
    prev_sum_1 = 0
    prev_sum_2 = 1
    
    while len(sub)!= 0:
        curr_sum = sum(principal) + sum(derived)
        if round(curr_sum, 1) == round(prev_sum_2, 1) and round(prev_sum_2, 1) == round(prev_sum_1, 1):
            return int(curr_sum)
        else:
            prev_sum_1 = prev_sum_2
            prev_sum_2 = curr_sum
        count += 1
        a, b = sub.pop(0)
        if a > limit/2:
            break
        
        for x in range(count, len(main)):
            c, d = main[x]
            
            if a + c < limit:
                test = min([abs(i - j) for i in b for j in d])
                
                if test >= 2:
                    if a + c < limit:
                        sub.append([a + c, b + d])
                        main.append([a + c, b + d])
                        derived.add(int(a + c))
            
    return int(sum(principal) + sum(derived))
            
if __name__ == "__main__":
    print(compute(10**10))
    print("--- %s seconds ---" % (time.time() - start_time))
