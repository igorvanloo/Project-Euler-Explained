#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:46:17 2021

@author: igorvanloo
"""
'''
Project Euler Problem 757

N = ab = cd , a + b = c + d + 1

Let a < b,c,d, x = c - a, y = d - a, then notice 

xy = N -a(c+d) + a^2 = N - a(a+b-1) + a^2 = N - ab + a = a
(x+1)(y+1) = xy + x + y + 1 = a + c - a + d - a + 1 = c + d + 1 - a = b
x(y+1) = xy + x = c
y(x+1) = d

Therefore N = x(x+1)y(y+1)
These are known as Bipronic numbers

For a given x, y can take values y^2 + y < 10^14/(x(x+1)) => x <= y < 1/2*(1+ sqrt(x^2+x+400,000,000,000,000 / (x(x+1))))

Anwser:
    75737353
--- 73.9674928188324 seconds ---
'''

import time, math
start_time = time.time()

def Divisors(x): #Find the divisors of a number
    divisors = []
    for i in range(int(math.sqrt(x)),0,-1):
        if x % i == 0:
            divisors.append(i + int(x/i))
    return (divisors)

def compute(limit): #Specific for 10^14 somehow faster? Not sure why
    array = set()
    for x in range(1, int(1/2*(math.sqrt(200000000000001) - 1)) + 1):
        for y in range(x, int(1/2*(math.sqrt((x**2 + x + 400000000000000)/(x*(x+1)))-1)) + 1):
            n = x*(x+1)*y*(y+1)
            if n > limit:
                break
            array.add(n)
            
    return len(array)
    
def compute1(limit): #Faster for lower numbers
    a = set()
    p = []
    for x in range(1, int(math.sqrt(limit))+1):
        p.append(x*(x+1))
        
    for x in p:
        for y in p:
            if x*y > limit:
                break
            a.add(x*y)
            
    return len(a)
    
if __name__ == "__main__":
    print(compute(10^14))
    print("--- %s seconds ---" % (time.time() - start_time))