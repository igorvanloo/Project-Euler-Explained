#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:21:52 2020

@author: igorvanloo
"""

'''
Project Euler Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Anwser:
    
    55
--- 343.36782002449036 seconds ---
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
    
def number_rotation(x):
    list2 = []
    str1 = str(x)
    for i in range(len(str1)):
        list2.append(is_prime(int(str1[i: ] + str1[ :i])))
    return list2

def compute():
    number_of_circular_primes = 0
    list1 = eulerlib.primes(1000000)
    for x in range(len(list1)):
        temp_list = number_rotation(list1[x])
        if all(temp_list):
            number_of_circular_primes += 1
    return number_of_circular_primes
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))