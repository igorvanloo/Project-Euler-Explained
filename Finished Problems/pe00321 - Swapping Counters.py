#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:46:15 2022

@author: igorvanloo
"""
'''
Project Euler Problem 321

M(1) = 3
M(2) = 8
M(3) = 15
https://oeis.org/A005563

M(n) = n^2 + 2n = (n + 1)^2 - 1
n^2 + 2n = t(t + 1)/2 => 2n^2 + 4n = t^2 + t

Anwser:
    2470433131948040
--- 0.0004699230194091797 seconds ---
'''
import time
start_time = time.time()

def equationsolver(x, startx, starty, a, b, c, d, e, f):
    x1 = startx
    y1 = starty
    solutions = []
    while len(solutions) != x:
        xn = a*x1 + b*y1 + c
        yn = d*x1 + e*y1 + f
        if xn > 0:
            solutions.append(xn)
        x1 = xn
        y1 = yn
    return solutions

def compute(limit):
    solutions = equationsolver(40, 0, 0, 3, 2, 3, 4, 3, 5) + equationsolver(40, 0, -1, 3, 2, 3, 4, 3, 5)
    return sum(sorted(list(set(solutions)))[:limit])

if __name__ == "__main__":
    print(compute(40))
    print("--- %s seconds ---" % (time.time() - start_time))
