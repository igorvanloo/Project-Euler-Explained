#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:09:33 2020

@author: igorvanloo
"""
'''
Project Euler Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

Reasoning:
We use eulers Pentagonal number theorem
The identity implies a recurrence for calculating {\displaystyle p(n)}p(n), the number of partitions of n:
p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+... until p(x) x <0 


Anwser:
    190569291
--- 0.0005931854248046875 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def sum_of_partitions(number):
    total = 0
    for x in range(number+1):
        total += partition(x, number)
    return total
    
def partition(k,n):
    
    if k == 0 and n == 0:
        return 1
    elif k <= 0 or n <= 0:
        return 0
    
    return partition(k, n-k) + partition(k-1, n-1) 

def Partition(goal, alist):
    ways = [1] + [0] * (goal)
    for options in alist:
        print("Current Table " + str(ways))
        print("Current number being checked " + str(options))
        for i in range(len(ways) - options):
            print("Current i: " + str(i))
            ways[i + options] += ways[i]
        print("\n")

    return ways[-1]-1

if __name__ == "__main__":
    print("Total number of ways to partition 5 is " +str(Partition(5, [x for x in range(2,6)])))
    print("--- %s seconds ---" % (time.time() - start_time))