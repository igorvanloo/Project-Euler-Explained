#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:04:16 2021

@author: igorvanloo
"""

'''
Project Euler Problem 130

Just modified my code from problem 129 to check if the condition is true

Anwser:
    149253
--- 7.208454847335815 seconds ---
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
    
def compute(limit):
    
    n = 2
    values = []
        
    while len(values) != limit:
        if math.gcd(n, 10) == 1 and is_prime(n) == False:
            l = 1
            while True:
                if pow(10,l,9*n) == 1:
                    break
                l += 1
            if (n - 1) % l == 0:
                values.append(n)
        n += 1

    return sum(values)

if __name__ == "__main__":
    print(compute(25))
    print("--- %s seconds ---" % (time.time() - start_time))