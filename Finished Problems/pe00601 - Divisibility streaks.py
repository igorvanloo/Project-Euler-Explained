#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 09:45:56 2021

@author: igorvanloo
"""

'''
Project Euler Problem 601

streak(n) = k means that
1|n
2|n+1
3|n+2
4|n+3
... k does not divide n+k

Brute forcing first 1000 values I found
P(1,10^3) = 499 = floor(998/1) - floor(998/lcm(1,2))
P(2,10^3) = 333 = floor(998/lcm(1,2)) - floor(998/lcm(1,2,3))
P(3,10^3) = 83 = floor(998/lcm(1,2,3)) - floor(998/lcm(1,2,3,4))
P(4,10^3) = 67 = floor(998/lcm(1,2,3,4)) - floor(998/lcm(1,2,3,4,5))
P(5,10^3) = 0 = floor(998/lcm(1,2,3,4,5)) - floor(998/lcm(1,2,3,4,5,6)) (Now the 0 fits the pattern because lcm(1,2,3,4,5) = lcm(1,2,3,4,5,6))

This exact trend continues for first 100,000 values so theres definetly a pattern

P(5,10^3) = 0 is an odd case so I investigate this first

If we want streak(n) = 5 this means
1|n, 2|n+1, 3|n+2, 4|n+3, 5|n+4, 6-|n+5
2|n+1 => n is odd => n+4 is odd => because 5|n+4 then n+4 ends in a 5 => n ends in a 1
=> n+5 ends in a 6 => 2|n+5 and furthermore because 3|n+2 => 3|sum of digits(n+2) => 3|sum of digits(n+5) => 3|n+5 => 6|n+5
So we have proved that a number with streak(n) = 5 is not possible as 6 will always divide n+5

Therefore we have that P(a, b) = floor((b-2)/lcm(1,2,...,a)) - floor((b-2)/lcm(1,2,...,a,a+1))

Anwser:
    1617243
--- 0.0015027523040771484 seconds ---
'''

import time
from math import floor, gcd

start_time = time.time()
    
def lcm(numbers):
    n = sorted(numbers)
    curr = n.pop(-1)
    while len(n) != 0:
        temp = n.pop(-1)
        curr = int(abs(curr*temp)/gcd(curr, temp))
    return curr
    
def brute_force(limit):
    array = [0]*(limit+1)
    for x in range(2, limit):
        n = x + 1
        k = 2
        count = 1
        while n % k == 0:
            count += 1
            n += 1
            k += 1
        array[x] = count
    return array
    
def compute(limit):
    total = 0
    for i in range(1,limit+1):
        total += floor((pow(4,i)-2)/lcm([x for x in range(1,i+1)])) - floor((pow(4,i)-2)/lcm([x for x in range(1,i+2)]))
    return total

if __name__ == "__main__":
    print(compute(31))
    print("--- %s seconds ---" % (time.time() - start_time))