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
    8581146
--- 27.841413736343384 seconds ---
    
'''

import time
start_time = time.time()

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += (x % 10)**2
        x = x // 10
    return totalsum

def square_digit_terminal_finder(x):
    while True:
        x = sum_digits(x)
        if x == 89:
            return 89
        if x == 1:
            return 1

def compute(limit):
    count = 0
    values = [0] + [square_digit_terminal_finder(x) for x in range(1,len(str(limit)) * 9**2)]     
    for y in range(1,limit + 1):
        temp_var = values[sum_digits(y)]
        if temp_var == 89:
            count += 1    
    return count

if __name__ == "__main__":
    print(compute(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))