#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 21:54:26 2020

@author: igorvanloo
"""
'''
Project Euler Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

10^n will always result in a number that is n+1 digits long therefore we only need to focus on numbers 1 - 9 so we need
to find bounds for each

n = 9 bound is 22 because 9^22
n = 8 bound is 11
n = 7 bound is 7
n = 6 bound is 5 .... we can just brute force with 22

Anwser:
    49
--- 0.0001888275146484375 seconds ---
'''

import time
start_time = time.time()

def find_bound(x):
    i = 1
    while True:
        if i > len(str(x**i)):
            break
        else:
            i += 1
    return i
    
def compute():
    count = []
    for n in range(1,10):
        for i in range(1,22):
            if i == len(str(n**i)):
                count.append(n**i) 
    return len(count)

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
