#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:12:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 108

1/x + 1/y = 1/n find all solutions for integer n

ny + nx = xy => n(x+y) = xy

We also knows that x,y > n because if either were less => 1/x or y > 1/n and the other cannot be negative

let x = n + a < y = n + b

=> n(2n + a + b) = n^2 + na + nb + ab
=> n^2 = ab

This means that ab are pair divisors of n^2, so this problem is reduced to finding the first n^2 with > 1000 divisors

Note
if n = p1^a * p2^b * p3^c * ...
then d(n) = (a+1)(b+1)(c+1)...

=> d(n^2) = (2a+1)(2b+1)(2c+1)

So I go through n and calculate the number of divisors of n^2 if > 1000, abort


Anwser:
    180180
--- 2.5153961181640625 seconds ---
'''

import time
        
def Divisors_of_n_squared(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(n)
            break
    temp = set(factors)
    
    divisors = 1
    for x in temp:
        divisors *= (2*factors.count(x) + 1)
    
    return divisors/2

def compute():
    x = 1
    while True:
        if Divisors_of_n_squared(x) > 1000:
            return x
        x += 1
        
if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))