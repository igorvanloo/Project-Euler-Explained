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
    9110846700
--- 0.0016629695892333984 seconds ---
'''

import time, math
start_time = time.time()

def compute():
    total = 0
    for x in range(1,1001):
        total += pow(x,x,10**10)
    return total % 10**10

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))