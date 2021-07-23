#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:46:11 2020

@author: igorvanloo
"""

'''
Project Euler Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Reasoning

1+2+3+4+5+6+7+8+9 = 45 => this number is always divisble by 9
1+2+3+4+5+6+7+8 = 36 => this number is always divisible by 9

7 digit numbers are allowed

1+2+3+4+5+6 = 21 => always divisble by 3
1+2+3+4+5 = 15 => always divisble by 3

4 digit numbers are allowed

1+2 = 3 => always divisble by 3
1 = 1 not prime

We can conclude that only primes of length 4 and 7 are allowed

Anwser:
    7652413
--- 1.9822278022766113 seconds ---
'''

import time, math, eulerlib, itertools
start_time = time.time()

def is_prime(x):
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
    final_list = []
    for x in range(2,10):
        temp_list = list(itertools.permutations(range(1,x+1),x))
        for y in range(len(temp_list)):
            temp_var = "".join(str(temp_list[y][i]) for i in range(0, len(temp_list[y])))
            if is_prime(int(temp_var)) == True:
                final_list.append(int(temp_var))
                
    return max(final_list), final_list

def compute1():
    primes = eulerlib.primes(10**7)
    pandigital = []
    for x in primes:
        if len(str(x)) == 4 or 7:
            if sorted(str(x)) == [str(i) for i in range(1,len(str(x))+1)]:
                pandigital.append(x)
    return max(pandigital)

if __name__ == "__main__":
    print(compute1())
    print("--- %s seconds ---" % (time.time() - start_time))