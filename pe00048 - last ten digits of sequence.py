#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:18:24 2020

@author: igorvanloo
"""

'''
Project Euler Problem 48

The series, 11 + 22 + 33 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

Anwser:
    
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    total = 0

    for x in range(1,1001):
        total += x**x
    total = str(total)
    return total, total[len(total)-10:]

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))