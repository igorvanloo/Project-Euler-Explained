#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:24:28 2020

@author: igorvanloo
"""

'''
Project euler problem 31

In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

Answer:
    73682
--- 0.0004940032958984375 seconds ---
'''

import math, time

def bruteforce():
    totalways = 1
    for a in range(0,3):
        for b in range(0,5):
            print(b)
            for c in range(0,11):
                for d in range(0,21):
                    for e in range(0,41):
                        for f in range(0,101):
                            for g in range(0,201):
                                if a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g*1 == 200:
                                    totalways += 1
    return totalways

def compute():
    totalways = 1
    for a in range(0,3):
        for b in range(0,(2-a)*2 + 1):
            for c in range(0,math.ceil((2-a-b*0.5)*10)+1):
                for d in range(0,math.ceil((2-a-b*0.5-c*0.2)*20)+1):
                    for e in range(0,math.ceil((2-a-b*0.5-c*0.2-d*0.1)*40)+1):
                        for f in range(0,math.ceil((2-a-b*0.5-c*0.2-d*0.1-e*0.05)*100)+1):
                            for g in range(0,math.ceil((2-a-b*0.5-c*0.2-d*0.1-e*0.05-f*0.02)*200)+1):
                                if a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g*1 == 200:
                                    totalways += 1
    return totalways

def Partition(goal, alist):
    ways = [1] + [0] * (goal)
    for options in alist:
        for i in range(len(ways) - options):
            ways[i + options] += ways[i]
    return ways[-1]

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    t = time.time() - start_time
    print("--- %s seconds ---" % (time.time() - start_time))

    print(Partition(200, [1, 2, 5, 10, 20, 50, 100, 200]))
    print("--- %s seconds ---" % (time.time() - start_time - t))

    
    
    
    
    
    
    
    