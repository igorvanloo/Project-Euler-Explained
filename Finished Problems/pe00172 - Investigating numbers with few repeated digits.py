#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 12:58:38 2022

@author: igorvanloo
"""
'''
Project Euler Problem 172

How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?

Anwser:
    227485267000992000
--- 9.497481107711792 seconds ---
'''
import time
from functools import cache
start_time = time.time()

def count_updater(n, count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9):
    if n == 0:
        count_0 += 1
    if n == 1:
        count_1 += 1
    if n == 2:
        count_2 += 1
    if n == 3:
        count_3 += 1
    if n == 4:
        count_4 += 1
    if n == 5:
        count_5 += 1
    if n == 6:
        count_6 += 1
    if n == 7:
        count_7 += 1
    if n == 8:
        count_8 += 1
    if n == 9:
        count_9 += 1
    return count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9

@cache
def compute(goal, pos, count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9):
    
    total = 0
    
    if count_0 > 3:
        return 0
    if count_1 > 3:
        return 0
    if count_2 > 3:
        return 0
    if count_3 > 3:
        return 0
    if count_4 > 3:
        return 0
    if count_5 > 3:
        return 0
    if count_6 > 3:
        return 0
    if count_7 > 3:
        return 0
    if count_8 > 3:
        return 0
    if count_9 > 3:
        return 0
    
    if pos == goal:
        #print(count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9)
        return 1
    
    if pos == 0:
        for cd in range(1, 10):
            a, b, c, d, e, f, g, h, i, j = count_updater(cd, count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9)
            total += compute(goal, pos + 1, a, b, c, d, e, f, g, h, i, j)
    else:
        for cd in range(0, 10):
            a, b, c, d, e, f, g, h, i, j = count_updater(cd, count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9)
            total += compute(goal, pos + 1, a, b, c, d, e, f, g, h, i, j)
    
    return total

if __name__ == "__main__":
    print(compute(18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    print("--- %s seconds ---" % (time.time() - start_time))
