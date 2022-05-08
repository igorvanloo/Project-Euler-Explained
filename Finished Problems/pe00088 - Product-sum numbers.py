#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:06:00 2022

@author: igorvanloo
"""

'''
Project Euler Problem 88

https://oeis.org/A104173

We can see that a(n) ≤ 2n since 1^(n-2)*2*n = (n-2)*1 + 2 + n = 2n
This gives us an upper bound for which numbers we need to check

Therefore I want to make a function PossFact(n) which takes a number n and returns all its possible factorisations

PossFact(8) = [4, 5] because we can create a ProdSum of length 4 and 5 as shown below
8 = 4 * 2 * 1 * 1 = 4 + 2 + 1 + 1
8 = 2 * 2 * 2 * 1 * 1 = 2 + 2 + 2 + 1 + 1

Anwser:
    7587457
--- 5.894201040267944 seconds ---
'''
import time, math
from functools import cache
start_time = time.time()

def Divisors(x): #Find the divisors of a number
    divisors = [x]
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    return sorted(set(divisors))

@cache
def PossFact(og_n, n, Prod, Sum, count):
    possib = []
    
    Prod = Prod
    Sum = Sum
    
    if Prod > og_n or Sum > og_n:
        return []
    
    if Prod == og_n and Sum == og_n:
        return [count]
    
    if n == 1:
        return [count + (og_n - Sum)]
    
    div = Divisors(n)
    
    for x in div:
        possib += PossFact(og_n, n//x, Prod*x, Sum + x, count + 1) 
    
    return possib

def compute(limit):
    INF = 10**8
    array = [INF]*(2*limit + 1)
    for x in range(4, 2*limit + 1):
        for y in set(PossFact(x, x, 1, 0, 0)):
            array[y] = min(array[y], x)
    
    array = array[2:limit]
    return sum(set(array))

if __name__ == "__main__":
    print(compute(12000))
    print("--- %s seconds ---" % (time.time() - start_time))