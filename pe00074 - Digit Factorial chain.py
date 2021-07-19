#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:24:21 2020

@author: igorvanloo
"""

'''
Project Euler Problem 74

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns 
out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting 
number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

Anwser:
    402
--- 9.977970838546753 seconds ---
    
'''

import time, math
start_time = time.time()

def factorial_digit(n):
    FACTORIAL = [math.factorial(i) for i in range(10)]
    factorialized = 0
    while n != 0:
        factorialized += FACTORIAL[n % 10]
        n //= 10
    return factorialized

def chain_length_finder(x):
    temp_list = set()
    while True:
        temp_list.add(x)
        x = factorial_digit(x)
        
        if x in temp_list:
            return len(temp_list)

def compute():
    count = 0
    for x in range(10, 1000001):
        if x % 100000 == 0:
            print(x)
        if chain_length_finder(x) == 60:
            count += 1
    return count

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += math.factorial(x % 10)
        x = x // 10
    return totalsum

def compute1(limit):
    array = [0] + [0]*limit
    
    for x in range(1,len(array)):
        array[x] = sum_digits(x)
    print("Array done")
    total = 0
    for x in range(1,len(array)):
        chain = [x]
        curr = array[x]
        while True:
            if curr in chain:
                if len(chain) == 60:
                    total += 1
                    break
                break
            chain.append(curr)
            try:
                curr = array[curr]
            except IndexError:
                curr = sum_digits(curr)
                
    return total
    
    
if __name__ == "__main__":
    #print(compute())
    print(compute1(800000))
    print("--- %s seconds ---" % (time.time() - start_time))