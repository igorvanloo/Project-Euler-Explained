#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:34:44 2020

@author: igorvanloo
"""
'''
Project Euler Problem 36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

Anwser:
    
    Total = 872187, 
    All number are [1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 73737, 585585])
--- 0.283123254776001 seconds ---
'''

import time, math, eulerlib
start_time = time.time()

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
    
def compute():
    total = 0
    list1 = []
    for x in range(1,int(1000000)):
        tempx = str(x)
        if tempx == tempx[::-1]:
            if bin(x)[2:] == bin(x)[2:][::-1]:
                list1.append(x)
                total += x
    return total, list1

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))