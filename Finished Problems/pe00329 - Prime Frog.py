#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:22:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 329

Wanted Sequence: PPPPNNPPPNPPNPN

Example case Frog starts at x = 15
                                                                                      x = 15 (P, 1 * 1/3)                                     
                                                                x = 14 (P, 1/2 * 1/3),                    x = 16 (P, 1/2 * 1/3)
                                           x = 13 (P, 1/4 * 2/3),                    x = 15 (P, 2/4 * 1/3),                    x = 17 (P, 1/4 * 2/3)
                     x = 12 (P, 1/8 * 1/3),                    x = 14 (P, 3/8 * 1/3),                     x = 16 (P, 3/8 * 1/3),                    x = 18 (P, 1/8 * 1/3)
x = 11 (N, 1/16 * 1/3),                   x = 13 (N, 4/16 * 1/3),                   x = 15 (N, 6/16 * 2/3),                    x = 17 (N, 4/16 * 1/3),                  x = 19 (N, 1/16 * 1/3)


Came back to attack this problem, with renewed ability in recursion and dynamic programming was able to solve it!

Given we start on one random number, say 15, the Denominator is always gonna be 2**14 * 3**15, let prob(x) denote the probability of the frog
croaking the way it does

Now the numerator is gonna be prob(15) = 1 * (prob(14)*(prob(13)... + prob(15)...) + prob(16)...)

Anwser:
    (199740353, 29386561536000)
--- 0.029585838317871094 seconds ---
'''

import time, math
from functools import cache
start_time = time.time()

def is_prime(x): #Test if giving value is a prime 
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True

def prob(x, letter):
    if is_prime(x):
        if letter == "P":
            return 2
        else:
            return 1
    else:
        if letter == "P":
            return 1
        else:
            return 2

def compute(pathlength, croaks):
    seq = "_PPPPNNPPPNPPNPN"
    
    @cache
    def rec(square, croak):
        value = prob(square, seq[croak])
        
        if croak == croaks:
            return value
        
        if square == 1:
            move_left = 2
            move_right = 2
        elif square == pathlength:
            move_left = square - 1
            move_right = square - 1
        else:
            move_left = square - 1
            move_right = square + 1 
        
        return value * (rec(move_left, croak + 1) + rec(move_right, croak + 1))
            
    num = sum(rec(x, 1) for x in range(1, pathlength + 1))
    den = pathlength * pow(2, croaks - 1) * pow(3, croaks)
    g = math.gcd(den, num)
    return num//g, den//g

if __name__ == "__main__":
    print(compute(500, 15))
    print("--- %s seconds ---" % (time.time() - start_time))