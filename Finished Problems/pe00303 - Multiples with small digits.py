#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:01:25 2022

@author: igorvanloo
"""
'''
Project Euler Problem 303

Anwser:
    1111981904675169
--- 55.10569381713867 seconds ---
'''
import time
from functools import cache
start_time = time.time()

@cache
def build_next_stack(curr_round):
    stack = ["1", "2"]
    for x in range(curr_round):
        next_stack = []
        for y in stack:
            next_stack.append(y + "0")
            next_stack.append(y + "1")
            next_stack.append(y + "2")
        stack = next_stack
    return stack
    
def construct_sequence(n):
    curr_round = 0
    while True:
        stack = build_next_stack(curr_round)
        for x in stack:    
            if int(x) % n == 0:
                return int(x)
        curr_round += 1
            
def compute(limit):
    total = 0
    for n in range(1, limit + 1):
        if n in [9, 99, 999, 9999]:
            a = len(str(n))
            total += int(a*"1" + 4*a*"2")/n
        else:
            t = construct_sequence(n)
            total += t/n
    return int(total)

if __name__ == "__main__":
    print(compute(100))
    print("--- %s seconds ---" % (time.time() - start_time))
