#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:32:52 2022

@author: igorvanloo
"""
'''
Project Euler Problem 239

First pick 3 primes 25C3, now there are 97 numbers remaining, 22 of which are prime

We want to find the number of derangments such that the 22 remaining primes do not go into their position.

We simplify the problem visually by saying all 25 primes are originally ordered in the first 25 places

Let's say the 3 primes we picked were the slots 23, 24, 25, now we pick the rest

There are 22 fixed number and we have 75 free choices, we can do 2 things

A) pick a free choice, and now the prime that was meant to go into that slot becomes a free choice
    we are left with 21 fixed spots and 75 choices, there are 75 ways to do this
B) pick a prime, now given that there are 22 fixed left, we have 21 ways to pick a prime
    by picking a prime we have inadvertedly fixed a second spot which can now have any number in its slot
    therefore we are left with 20 fixed slots and 76 choice (because now 1 prime have become choice)


We continue like this, at the end we multiply by choice!

Anwser:
    0.001887854841
--- 0.0004930496215820312 seconds ---
'''
import time, math
from functools import cache
start_time = time.time()

def n_choose_r(n, r):  # nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))

def D(n):
    return int(math.floor(math.factorial(n)/math.e + 0.5))
    
@cache
def derangments(fixed_left, choice):
    
    total = 0
    
    if fixed_left == 0:
        return math.factorial(choice)
    
    total += choice*derangments(fixed_left - 1, choice) #A
    if fixed_left > 1:
        total += (fixed_left - 1)*derangments(fixed_left-2, choice + 1) #B
    
    return total
    
def compute(fixed):
    return round((n_choose_r(25, fixed) * derangments(25-fixed, 75))/math.factorial(100), 12)

def compute2():
    return round((2300 * sum([n_choose_r(75, i)*D(97 - i) for i in range(0, 76)]))/math.factorial(100), 12)
                    
if __name__ == "__main__":
    print(compute(3))
    print("--- %s seconds ---" % (time.time() - start_time))
