#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:40:53 2022

@author: igorvanloo
"""
'''
Project Euler Problem 189

    2450774016 - 6 rows
--- 0.5343091487884521 seconds ---
    3104112826368 - 7 rows
--- 5.317054986953735 seconds ---

Anwser:
    10834893628237824
--- 60.749743938446045 seconds ---
'''
import time
from functools import cache
start_time = time.time()

def gen_string(mask, pos, prev):
    strings = []
    
    if pos == len(mask) + 2:
        return [prev]
    
    if pos == 0:
        for x in ("R", "G", "B"):
            strings += gen_string(mask, pos + 1, prev + x)
    else:
        if pos % 2 == 1:
            for x in ("R", "G", "B"):
                if x != mask[pos - 1] and x != prev[-1]:
                    strings += gen_string(mask, pos + 1, prev + x)
        else:
            for x in ("R", "G", "B"):
                if x != prev[-1]:
                    strings += gen_string(mask, pos + 1, prev + x)
    return strings     

@cache
def compute(row, mask):
    total = 0
    
    if row == 1:
        return len(gen_string(mask, 0, ""))
    
    else:
        possib = gen_string(mask, 0, "")
    
        for x in possib:
            total += compute(row - 1, x)
    
    return total
    
if __name__ == "__main__":
    print(compute(7, "R")*3)
    print("--- %s seconds ---" % (time.time() - start_time))
