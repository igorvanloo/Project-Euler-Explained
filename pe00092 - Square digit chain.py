#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:22:55 2020

@author: igorvanloo
"""

'''
Project Euler Problem 92

A number chain is created by continuously adding the square of the digits in a number to form a new number
 until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that 
EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

The sum of the square digits has a maximum of 9^2 * 7 because of 9,999,999. So we can look for which numbers from
1 - 567 result in 89 or 1 and then check if any number from 1 - 10,000,000 end up on one of these numbers we immediately
know the solution

Anwser:
    (1418854, 8581146, 10000000)
--- 40.76573419570923 seconds ---
    
'''

import time, math, eulerlib, itertools
start_time = time.time()

def square_digit_terminal_finder(x):
    while True:
        
        x = str(x)
        x = sum([int(x[y])**2 for y in range(len(x))])
        if x == 89:
            return 89
        if x == 1:
            return 1

def compute():
    
    count = 0
    count2 = 0
    
    values = [square_digit_terminal_finder(x) for x in range(1,568)]
        
    
    print(values)
    
    
    for y in range(1,10000001):
        y = str(y)
        try:
            temp_var = values[sum([int(z)**2 for z in y]) - 1]
        except IndexError:
            print(y)

        if temp_var == 1:
            count += 1
        elif temp_var == 89:
            count2 += 1
            
    return count, count2, count + count2
        

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))