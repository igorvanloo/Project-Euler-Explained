#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 20:52:09 2021

@author: igorvanloo
"""
'''
Project Euler Problem 140

g(1) = 1, g(2) = 4, g(k) = g(k-1) + g(k-2)
g(3) = 5, g(4) = 9, g(5) = 14, g(6) = 23

A(x) = g1x + g2x^2 + g3x^3 + ...
xA(x) = g1x^2 + g2x^3 + g3x^4 + ...
x^2A(x) = g1x^3 + g2x^4 + g3x^5 + ...

A(x)(1-x-x^2) = xg1 + x^2(g2-g1) + x^3(g3-g2-g1) + x^3(g4-g3-g2) = x + 3x^2

so we see that A(x) = (x+3x^2) / (1-x-x^2)

Same as in problem 137

we want A(x) = (x+3x^2) / (1-x-x^2) = h, an integer

x+3x^3 = h - xh - x^2h  =>  x^2(h+3) + x(h+1) - h = 0

we solve for x

x = (-(h+1) + sqrt(h+1)^2 - 4(h+3)(-h))/2(h+3)

x = (-(h+1) + sqrt(5h^2 + 14h + 1)/(2(h+3))
     
so we see that 5h^2 + 14h + 1 must be a perfect square

quick code produces first 20 numbers

2
5
21
42
152
296
1050
2037
7205
13970
49392
95760 
338546
656357
2320437
4498746
15904520
30834872
109011210
20th 211345365

Anwser:
    ([2, 5, 21, 42, 152, 296, 1050, 2037, 7205, 13970, 49392, 95760, 338546, 656357, 2320437, 4498746, 15904520, 30834872, 109011210, 211345365, 747173957, 1448582690, 5121206496, 9928733472, 35101271522, 68052551621, 240587694165, 466439127882, 1649012587640, 3197021343560], 
     5673835352990)
--- 0.00026798248291015625 seconds ---
'''

import time, math
start_time = time.time()

def Fibonnacimod(x):
    fibnumbers = [1,4]
    f1 = 1
    f2 = 4
    while len(fibnumbers) != x:
        fx = f2 + f1
        fibnumbers.append(fx)
        f1 = f2
        f2 = fx
    return fibnumbers

def equationsolver(x, startx, starty):
    x1 = startx
    y1 = starty
    solutions = []
    while len(solutions) != x:
        xn = -9*x1 -4*y1 - 14
        yn = -20*x1 -9*y1 - 28
        if xn > 0:
            solutions.append((xn))
        x1 = xn
        y1 = yn
        
    return solutions

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
        
        d = (5*(h**2) + 14*h + 1)
        if is_quadratic(d) == True:
            x = (-(h+1) + math.sqrt(d))/(2*(h+3))
            final.append(round((x+3*x**2)/(1-x-x**2)))

        h += 1
        
    return final

def compute1():
    final = equationsolver(15,0,1) + equationsolver(15,0,-1) + equationsolver(15,-3,-2) + equationsolver(15,-3,2) + equationsolver(15,-4,-5) + equationsolver(15,-4,5) + equationsolver(15,2,-7) + equationsolver(15,2,-7)
    final = sorted(list(set(final)))
    final = final[:30]
    
    return len(final), sum(final)

if __name__ == "__main__":
    print(compute1())
    print("--- %s seconds ---" % (time.time() - start_time))

