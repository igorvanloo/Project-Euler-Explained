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
--- 0.16759133338928223 seconds ---    
'''

import time
start_time = time.time()

def compute():
    x = 100
    while True:
        count = 1
        for i in range(2, 7):
            if sorted(str(x)) != sorted(str(i*x)):
                break
            count += 1
        if count == 6:
            return x
        x += 1

def HackerRankVer(N, K):
    x = 100
    while x != N+1:
        count = 1
        for i in range(2, K+1):
            if sorted(str(x)) != sorted(str(i*x)):
                break
            count += 1
        tempstr = ""
        if count == K:
            for y in range(1,K+1):
                tempstr += str(y*x)
                tempstr += " "
            print(tempstr)
        x += 1
        
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))