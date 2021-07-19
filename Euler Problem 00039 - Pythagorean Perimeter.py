#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:41:11 2020

@author: igorvanloo
"""

'''
Project Euler Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Anwser:
    
    (8, 840)
--- 4.679589748382568 seconds ---
'''

import time, math, eulerlib
start_time = time.time()

def pythagorean_solution(p):
    solutions = []
    for a in range(1,p+1):
        for b in range(a,(p-a)//2 + 1):
            c = p - a - b
            if a*a + b*b == c*c:
                solutions.append(sorted([a,b,c]))
    return len(solutions)
                    
def compute():
    current_max = 0
    number = 0
    for x in range(1,1001):
        if pythagorean_solution(x) > current_max:
            current_max = pythagorean_solution(x)
            number = x
    return current_max, number
            
        

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))