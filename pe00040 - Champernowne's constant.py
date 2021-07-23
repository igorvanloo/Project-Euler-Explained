#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:15:45 2020

@author: igorvanloo
"""

'''
Project Euler Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

Anwser:
    210
--- 0.2806992530822754 seconds ---
    
'''

import time, math, eulerlib
start_time = time.time()

def weird_decimal():
    x = ""
    for i in range(1,1000000):
        x += str(i)
    return x
        
def compute():
    num = weird_decimal()
    total = 1
    for x in range(7):
        print(int(num[10**x - 1]))
        total *= int(num[10**x - 1])
    return total
        
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))