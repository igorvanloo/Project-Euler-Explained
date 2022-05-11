#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:07:21 2022

@author: igorvanloo
"""
'''
Project Euler Problem 164

Just a simple recursive function takes 4 arguments
goal: how many digits do we want
pos: current digit we are on
prev_digit_1, prev_digit_2: previous 2 digits

Answer for n digits is dp(n, 0, 0, 0)

Anwser:
    378158756814587
--- 0.0024051666259765625 seconds ---
'''
import time
from functools import cache
start_time = time.time()

@cache
def compute(goal, pos, prev_digit_1, prev_digit_2):
    
    total = 0
    
    if pos == goal:
        return 1
    
    if pos == 0:
        for curr_digit in range(1, 10):
            if 0 <= prev_digit_1 + prev_digit_2 + curr_digit <= 9:
                total += compute(goal, pos + 1, prev_digit_2, curr_digit)
    else:
        for curr_digit in range(0, 10):
            if 0 <= prev_digit_1 + prev_digit_2 + curr_digit <= 9:
                total += compute(goal, pos + 1, prev_digit_2, curr_digit)
    
    return total

if __name__ == "__main__":
    print(compute(20, 0, 0, 0))
    print("--- %s seconds ---" % (time.time() - start_time))
