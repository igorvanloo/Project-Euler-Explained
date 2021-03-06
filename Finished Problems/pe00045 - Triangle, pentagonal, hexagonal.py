#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:22:12 2020

@author: igorvanloo
"""

'''
Project Euler Problem 45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

Anwser:
    1533776805.0
--- 0.022198915481567383 seconds ---
'''

import time
start_time = time.time()

def is_pentagonal(x):
    #Take the inverse function to test whether or not a number is pentagonal
    if (1+(24*x+1)**0.5) % 6 == 0:
        return True
    return False

def is_hexagonal(x):
    if (1+(8*x+1)**0.5) % 4 == 0:
        return True
    return False
    
def compute():
    i = 286
    while True:
        a = (i/2)*(i+1)
        if is_pentagonal(a) == True and is_hexagonal(a) == True:
            print(i)
            return a
        i += 1

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))