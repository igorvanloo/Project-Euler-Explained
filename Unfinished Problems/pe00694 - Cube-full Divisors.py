#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 00:37:34 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

n is Cube full means that if for every prime, p, that divides n then p^3 also divides n

=> n = p_1^(3e_1) * p_2^(3e_2) * ...

Note that (2*3*4*5*6*7*8*9)^3 > 10^18

The largest p must be less than 10^6 for all of our numbers

https://oeis.org/A036966

Anwser:

'''

import time, math
start_time = time.time()

def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(2 * i, len(result), i):
				result[j] = False
	return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def generator(g, alist, limit):
    #Takes an input g, multiplies it with all the elements in alist
    #Limit sets the limit of g*x, x comes from alist
    if len(alist) == 0:
        return []
    
    multiples = []
    
    temp = alist.pop(0)
    for x in temp:
        a = x*g
        if a < limit + 1:
            multiples.append(x*g)
    multiples += generator(g, alist, limit)
    
    return multiples
    
def compute(limit):
    primes = list_primes(int(limit**(1/3)) + 1)
    
    c = []
    for x in primes:
        temp_can = []
        temp = x**3
        
        while True:
            if temp > limit:
                break
            temp_can.append(temp)
            temp *= x
        
        c.append(temp_can)
    cube_full = []
    for x in range(len(c)):
        for y in range(len(c[x])):
            cube_full += [c[x][y]]
            a = generator(c[x][y], c[x+1:], limit)
            cube_full += a
    
    count = limit
    for x in cube_full:
        count += int(math.floor(limit/x))
    return count

if __name__ == "__main__":
    print(compute(10**13))
    print("--- %s seconds ---" % (time.time() - start_time))