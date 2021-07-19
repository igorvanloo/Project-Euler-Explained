#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:17:28 2021

@author: igorvanloo
"""

'''
Project Euler Problem 77

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

Anwser:
    71
--- 1.5247690677642822 seconds ---
'''

import time, math, eulerlib

def Partition(goal, alist):
    ways = [1] + [0] * (goal)
    for options in alist:
        for i in range(len(ways) - options):
            ways[i + options] += ways[i]
    return ways

def compute():
    alist = eulerlib.primes(10000)
    goal = 10000
    temp_list = Partition(goal, alist)
    
    for x in range(len(temp_list)):
        if temp_list[x] > 5000:
            return x
            break

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))