#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:01:49 2020

@author: igorvanloo
"""

'''
Project Euler Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Anwser:
    142857
--- 1.8680148124694824 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    
    x = 100000
    while True:
        count = 0
        temp_list = list(itertools.permutations(str(x)))
        for y in range(1,7):
            if tuple(list(str(y*x))) in temp_list:
                count += 1
                if count == 6:
                    return x
                    break
            else:
                break
        x += 1
        if len(str(6*x)) > len(str(x)):
            x = 10**(len(str(6*x))-1)
            print(x)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))