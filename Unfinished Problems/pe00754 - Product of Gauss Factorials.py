#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:06:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

After some brute force found

g(n) = https://oeis.org/A001783
G(n) = https://oeis.org/A280820



Anwser:

'''

import time, math
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
    
def Mobius(n):
    if n == 1:
        return 1
    d = 2
    num_of_primes = 0
    while n > 1:
        while n % d == 0:
            num_of_primes += 1
            if n % (d*d) == 0:
                return 0
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                num_of_primes += 1
            break
    return (-1)**num_of_primes

def compute(limit):
    
    G = []    
    for z in range(1, limit + 1):
        total = 1
        for x in range(1, z + 1):
            temp_total = 1
            for y in range(1, x):
                if math.gcd(x,y) == 1:
                    temp_total *= y
            total *= temp_total
        G.append(total)
    
    return G
    

if __name__ == "__main__":
    print(is_prime())
    print("--- %s seconds ---" % (time.time() - start_time))