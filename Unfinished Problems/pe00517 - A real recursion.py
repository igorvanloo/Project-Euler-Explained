#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:31:56 2021

@author: igorvanloo
"""

'''
Project Euler Problem 517

a > 1 
g_a(x) = 1 if x < a
g_a(x) = g_a(x-1) + g_a(x - a) if x ≥ a

G(n) = g_sqrt(n)(n)

Let b = sqrt(90)
G(90) = g_b(90) = g_b(89) + g_b(x-b)
                = g_b(88) + g_b(89 - b) + g_b(x-b-1) + g_b(x-2b)

First 100 terms of G(n) are
[2, 2, 3, 5, 5, 8, 9, 13, 19, 19, 28, 35, 42, 50, 69, 95, 95, 131, 143, 194, 231, 265, 325, 431, 571, 571, 
 756, 866, 1021, 1312, 1468, 1846, 2225, 2402, 3088, 3970, 3970, 5103, 6042, 6840, 7686, 9733, 11035, 12658, 
 15386, 17843, 19796, 24851, 31200, 31200, 39173, 42308, 49751, 58702, 65668, 81643, 91339, 102297, 117925, 144852, 
 158192, 179426, 221049, 272333, 272333, 335525, 371698, 422870, 497928, 555578, 638289, 757164, 831849, 926134, 1129209, 
 1203134, 1443585, 1679766, 1770255, 2147563, 2605267, 2605267, 3160516, 3572022, 3856725, 4602616, 5189912, 5739144, 
 6279823, 7564511, 8339955, 9310710, 10739482, 12133639, 13500673, 15711165, 17586284, 18858092, 22582581, 22582581]

We have a double in a gap going by 1 space, then 3, 5, 7, 9, ....

Absolutely no idea how to continue


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

def g(x, a):
    if x < a:
        return 1
    return g(x-1,a) + g(x-a, a)
    
    
def compute():
    primes = [x for x in range(10**7, 10**7 + 10001) if is_prime(x)]
    

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))