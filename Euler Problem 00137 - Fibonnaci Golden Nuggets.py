#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:27:34 2021

@author: igorvanloo
"""

'''
Project Euler Problem 137

Af(x) = f1x + f2x^2 + f3x^3 + ... = sum from k = 1 to infinity of fkx^k

This has maclaurin series f(x) = x/(1-x-x^2)

so we must simply find when f(x) = an positive integer, that is x is divisible by 1-x-x^2

x/(1-x-x^2) = h, an integer

=> x = h - hx - hx^2 => hx^2 + x(h+1) - h = 0
=> x = (-(h+1) +- sqrt(5h^2+2h+1))/2h

for this to be an integer 5h^2 + 2h + 1 must be a perfect square

After quick calculation we can find the first 10, and notice a pattern
    
2 = f(2)f(3) = 1*2
15 = f(4)f(5) = 3*5
104 = f(6)f(7) = 8*13
714 = f(8)f(9) = 21*34
4895
33552
229970
1576239
10803704
74049690 = f(20)f(21)

so we are looking for f(30)f(31)

Anwser:
    1120149658760
--- 7.200241088867188e-05 seconds ---
    
'''

import time, math
start_time = time.time()

def is_quadratic(x):
    cube__root = (x**(1/2))
    if round(cube__root) ** 2 == x:
        return True
    return False

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2

def compute():
    final = []
    h = 1

    while True:
        if len(final) == 15:
            break
        
        d = (5*(h**2) + 2*h + 1)
        if is_quadratic(d) == True:
            x = (-(h+1) + math.sqrt(d))/(2*h)
            print(round(x/(1-x-x**2)))
            final.append(round(x/(1-x-x**2)))

        h += 1
    return final


if __name__ == "__main__":
    print(fibonnaci(50) * fibonnaci(51))
    print("--- %s seconds ---" % (time.time() - start_time))