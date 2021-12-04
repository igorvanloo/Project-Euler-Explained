#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:41:15 2021

@author: igorvanloo
"""

'''
Project Euler Problem 138

Primitive Pythagorean Triangles would work, but it was way too slow

Instead we notice h^2 + (b/2)^2 = L^2
We want h = b ± 1, therefore we have
5b^2 ± 8b + 1 = L^2

We can solve this Using Dario Alpern’s Generic Two integer variable equation solver

Anwser:
    1118049290473932
--- 0.00019979476928710938 seconds ---
'''

import time, math
start_time = time.time()

def equationsolver(n, startx, starty):
    x1 = startx
    y1 = starty
    solutions = []
    while len(solutions) != n:
        xn = -9*x1 -8*y1 - 8
        yn = -10*x1 -9*y1 - 8
        if yn > 0:
            solutions.append((yn))
        x1 = xn
        y1 = yn
        
    return solutions

def equationsolver2(n, startx, starty):
    x1 = startx
    y1 = starty
    solutions = []
    while len(solutions) != n:
        xn = -9*x1 -8*y1 + 8
        yn = -10*x1 -9*y1 + 8
        if yn > 0:
            solutions.append((yn))
        x1 = xn
        y1 = yn
        
    return solutions

def compute():
    solutions = equationsolver(15, 0, 1) + equationsolver2(15, 0, 1)
    solutions = sorted(solutions)
    return sum(solutions[0:12])

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))