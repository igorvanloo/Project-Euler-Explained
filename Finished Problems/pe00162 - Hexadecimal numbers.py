#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:08:50 2022

@author: igorvanloo
"""
'''
Project Euler Problem 162

This is a basic inclusion exclusion principle type question

Let 
T = total number of strings = 15*16^(n-1) - n denotes length of string

A = {strings with atleast 1 0 inside}
B = {strings with atleast 1 1 inside}
C = {strings with atleast 1 A inside}

we want |A n B n C| = {strings with atleast 1 0,1,A inside}
|A n B n C| = |A u B u C| + |A n C| + |A n B| + |B n C| - |A| - |B| - |C|

|A| = T - |A'| = T - 15^n = 15*16^(n-1) - 15^n
|B| = T - |B'| = T - 14*15^(n-1) = 15*16^(n-1) - 14*15^(n-1)
|C| = T - |C'| = T - 14*15^(n-1) = 15*16^(n-1) - 14*15^(n-1)

|A n C| = |A| + |C| - |A u C| = |A| + |C| - (T - |(A u C)'| = (15*16^(n-1) - 15^n) + (15*16^(n-1) - 14*15^(n-1)) - (15*16^(n-1) - 14^n)
                                            = 15*16^(n-1) - 29*15^(n-1) + 14^n

|A n B| = |A| + |B| - |A u B| = |A| + |B| - (T - |(A u B)'| = (15*16^(n-1) - 15^n) + (15*16^(n-1) - 14*15^(n-1)) - (15*16^(n-1) - 14^n) = 
                                            = 15*16^(n-1) - 29*15^(n-1) + 14^n                                

|B n C| = |B| + |C| - |B u C| = |B| + |C| - (T - |(B u C)'| = (15*16^(n-1) - 14*15^(n-1)) + (15*16^(n-1) - 14*15^(n-1)) - (15*16^(n-1) - 13*14^(n-1))
                                            = 15*16^(n-1) - 28*15^(n-1) + 13*14^(n-1)
                                            
|A u B u C| = T - |(A u B u C)'| = 15*16^(n-1) - 13^n

Therefore as per above
|A n B n C| = (15*16^(n-1) - 13^n) + (15*16^(n-1) - 28*15^(n-1) + 13*14^(n-1)) + 2*(15*16^(n-1) - 29*15^(n-1) + 14^n) - 2*(15*16^(n-1) - 14*15^(n-1)) -  15*16^(n-1) - 15^n
            = 15*16^(n-1) - 43*15^(n-1) + 41*14^(n-1) - 13^n         
                                             
Anwser:
    3D58725572C62302
--- 0.0001399517059326172 seconds ---
'''
import time
start_time = time.time()

def compute(limit):
    t = sum([int(15*16**(n-1) - 43*15**(n-1) + 41*14**(n-1) - 13**n) for n in range(1, limit + 1)])
    return "Hexadecimal: " + str(hex(t).upper()[2:]) + "\nBase 10: " + str(t)

if __name__ == "__main__":
    print(compute(16))
    print("--- %s seconds ---" % (time.time() - start_time))