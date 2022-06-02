#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:24:21 2022

@author: igorvanloo
"""
'''
Project Euler Problem 297

Zeckendorf representation can be found using a greedy algorithm, this means there will be
a recusrive sequence that should appear.

using the wikipedia picture we can see there are repeated "blocks" that are added.
This make it very easy to find the solution if we are dealing with only fibonnaci numbers, how to we deal with non-fibonnaci?
Seperate them into 2 parts a fib part and non fib part, repeat the function for the non fib part, and continue until we reach a fib
decomposition!

Anwser:
    2252639041804718029
--- 0.0027909278869628906 seconds ---
'''
import time
start_time = time.time()

def fibonnaci(n):  # Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0  # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2

def fib_till(x):
    fibnumbers = []
    n = 1
    while fibonnaci(n) <= x:
        fibnumbers.append(fibonnaci(n))
        n += 1
    return fibnumbers

def ZeckendorfRepresentation(x):
    zeckrep = []
    fibs = fib_till(x)[::-1]
    
    number = x
    count = 0
    while number != 0:
        if number - fibs[count] >= 0:
            number -= fibs[count]
            zeckrep.append(fibs[count])
            count += 1
        count += 1
    return zeckrep

def compute(limit):
    if limit == 1:
        return 0
    if limit == 2:
        return 1
    if limit == 3:
        return 2
    
    fib = fib_till(limit)
    total = 0
    
    t = limit - fib[-1]
    if t != 0:
        total += compute(t) + t
        
    block1 = 2
    block2 = 3
    
    for x in range(3, len(fib) - 1): #start at f_3 = 3
        blockn = (fib[x] + block1)
        block1 = block1 + block2
        block2 = blockn
    
    return block1 + total
        
if __name__ == "__main__":
    print(compute(10**17))
    print("--- %s seconds ---" % (time.time() - start_time))
