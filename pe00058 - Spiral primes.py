#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:10:45 2020

@author: igorvanloo
"""

'''
Project Euler Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more 
interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral for which the ratio of primes along 
both diagonals first falls below 10%?

Anwser:
    26241
--- 2.1476309299468994 seconds ---
    
'''

import time, math, eulerlib, itertools
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
    
def compute():

    prime_numbers = 0
    for x in itertools.count(1,2):
        
        for y in range(1,4):
            if is_prime(x*x - y* (x-1)) == True:
                prime_numbers += 1
        
        total_numers = 2*x-1
        if x > 1 and prime_numbers/total_numers < 1/10:
            print(prime_numbers/total_numers)
            return x
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))