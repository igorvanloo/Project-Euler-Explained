#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:33:03 2022

@author: igorvanloo
"""
'''
Project Euler Problem 174

Anwser:
    209566
--- 1.1640172004699707 seconds ---
'''
import time, math
from collections import Counter
start_time = time.time()

def compute(limit):
    pl = [] #possible laminae
    
    for x in range(1, int(limit/4) + 1):
        temp1 = 4*(x + 1)
        if temp1 <= limit:
            pl.append(temp1)
    
    nl = [] #new laminae
    for i in range(len(pl) - 2):
        curr_sum = pl[i]
        curr = i + 2
        while curr_sum + pl[curr] <= limit:
            new_sum = curr_sum + pl[curr]
            nl.append(new_sum)
            curr_sum = new_sum
            if curr + 2 < len(pl):
                curr += 2
    final = pl + nl
    counter = Counter(final)
    total = sum([1 for x in set(final) if 1 <= counter[x] <= 10])
    
    return total
    
if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))
