#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:01:49 2020

@author: igorvanloo
"""

'''
Project Euler Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can 
work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes

Anwser:
    748317
--- 0.5134131908416748 seconds ---
'''

import time, math, eulerlib
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
    
def compute(limit):
    stack = [2,3,5,7]
    valid = []
    while len(stack) != 0:
        curr = stack.pop(0)
        for y in [1,3,5,7,9]:
            temp1 = int(str(curr) + str(y))
            if is_prime(temp1):
                stack.append(temp1)
                valid.append(temp1)
    
    maximum = max(valid)
    stack1 = [2,3,5,7]
    valid1 = []
    while len(stack1) != 0:
        curr = stack1.pop(0)
        for y in [1,2,3,4,5,6,7,8,9]:
            temp2 = int(str(y) + str(curr))
            if temp2 < maximum:
                if is_prime(temp2):
                    stack1.append(temp2)
                    valid1.append(temp2)
    
    total = 0
    temp = list(set(valid).intersection(set(valid1)))
    for x in temp:
        if x < limit:
            total += x
            #print(x)
    return total

if __name__ == "__main__":
    print(compute(1000000))
    print("--- %s seconds ---" % (time.time() - start_time))