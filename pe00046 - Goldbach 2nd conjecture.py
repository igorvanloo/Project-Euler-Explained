#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:53:34 2020

@author: igorvanloo
"""

'''
Project Euler Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a 
prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

Anwser:
    
    5777
--- 0.01988387107849121 seconds ---
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
    
    number = False
    count = 33
    while number == False:
        for x in range(1, int(math.sqrt(count))+1):
            
            temp_var = count - 2*(x**2)
            
            if is_prime(temp_var) == True:
                count += 2
                if is_prime(count) == True:
                    count += 2
                    break
                break
                    
                    
            elif is_prime(temp_var) == False:
                if x == int(math.sqrt(count)):
                    return count
                    number = True

        

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    