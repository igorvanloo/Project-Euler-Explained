#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 21:27:26 2021

@author: igorvanloo
"""

'''
Project Euler Problem 101

Using Lagrange polynomial

Anwser:
    37076114526.0
--- 0.0003387928009033203 seconds ---
'''

import time, math, eulerlib

def PolynomialInterpolator(sequence):
    if len(sequence) == 1:
        return sequence[0][1]
    
    elif len(sequence) == 2:
        return sequence[1][1] + (sequence[1][1] - sequence[0][1])
    
    else:
        length = len(sequence)
        goal = length + 1
        total = 0
        for x in range(length):
            temp_total_multiple = sequence[x][1]
            temp_total_divisor = 1
            for y in range(1,goal+1):
                if (x+1) - y != 0 and goal - y != 0:
                    temp_total_multiple *= (goal - y)
                    temp_total_divisor *= ((x+1)-y)
                    
            total += temp_total_multiple/temp_total_divisor
    return total

def compute():
    
    terms = [(1,1),(2,683),(3,44287),(4,838861),(5,8138021),(6,51828151),(7,247165843),(8,954437177),(9,3138105961),(10,9090909091)]
    
    total = 0
    for x in range(1,len(terms)+1):
        temp = PolynomialInterpolator(terms[:x])
        print(temp)
        total += temp
    
    return total

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))