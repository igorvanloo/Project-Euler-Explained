#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:45:00 2022

@author: igorvanloo
"""

'''
Project Euler Problem 191

Not a very difficult problem if you know some dynamic programming

We make a dynamic programming function compute(d, a, l) where d = days in total, a = number of absences, l = number of lates

if a == 3 -> this string will not result in a prize
if l > 1 -> this string will not result in a prize
if d = 0 -> we have reached the end of the string and not ecnountered any problem, hence we get a prize

we start at day n and we go down till 0

we add 
1) if the student is ontime (absence goes to 0, late stays the same)
2) if the student is absent (absence + 1, late stays the same)
3) if the studebt is late (absence goes to 0, late + 1)

then we can use the inbuilt @cache function because if we encounter a different string, with the same number of lates and absences 
on the same day, then they can be evaluated the same from that day onward

Anwser:
    1918080160
--- 0.0011339187622070312 seconds ---
'''
import time
from functools import cache
start_time = time.time()

@cache
def compute(d, a, l): #days, absent, late
    total = 0
    
    if a == 3:
        return 0
    if l > 1:
        return 0
    if d == 0:
        return 1
    
    total += compute(d - 1, 0, l)
    total += compute(d - 1, a + 1, l)
    total += compute(d - 1, 0, l + 1)
    
    return total

if __name__ == "__main__":
    print(compute(30, 0, 0))
    print("--- %s seconds ---" % (time.time() - start_time))