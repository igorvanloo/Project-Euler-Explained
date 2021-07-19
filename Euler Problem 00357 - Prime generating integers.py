#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:21:25 2021

@author: igorvanloo
"""

'''
Project Euler Problem 357

Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.

Take a number n: it will always have divisors 1 and n
=> 1+ n/1 = n+1 and n + n/n = n+1 must be prime

2 is the only even prime therefore for n >= 2, n + 1 must be an odd prime number => n must be even

if n is even => 2 is a divisors and therefore 2 + n/2 must be prime, however this can only be prime 
if n/2 is odd

So n must be even and n/2 must be odd => n must be a multiple of 2 but not 4, because if n is a multiple of 4
=> n = 4k => 4k/2 = 2k which is even

Conclusion: n = 1 is a valid number, we need to check through all numbers divisible by 2 but not 4 and a quick check is to 
see if n + 1 is prime

Anwser:
    1739023853137
--- 52.71331596374512 seconds ---
'''

import time, math, eulerlib, itertools
start_time = time.time()

def Modified_Divisors(x): #Find the divisors of a number
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if is_prime(int(i + x/i)) == False:
                return False
    return True

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

def AreDivisorsPrime(alist):
    for x in alist:
        if is_prime(x) == False:
            return False
    return True

def compute():
    totalsum = 1
    primes = eulerlib.primes(10**8 + 1)
    finallist = [x-1 for x in primes if ((x) - 1) % 4 != 0 and ((x) - 1) % 2 == 0]
    
    print("done making list")
    
    count = 0
    for i in finallist:
        if count % 500000 == 0:
            print(count)
        
        if AreDivisorsPrime(Divisors(i)) == True:
            totalsum += i
        count += 1
        
    return totalsum

def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(2*i, len(result), i):
				result[j] = False
	return result

def compute1(limit):
    primelist = list_primality(limit+1)
    print("Primes done")
    print("--- %s seconds ---" % (time.time() - start_time))
    values = [x for x in range(2, limit+1, 4)]
    #print("values done")
    #print("--- %s seconds ---" % (time.time() - start_time))
    #print(len(values))
    
    totalsum = 1
    for x in (values):
        isvalid = True
            
        if primelist[x+1] == False:
            isvalid = False
        
        if isvalid == True:
            for d in range(2,int(math.sqrt(x))+1):
                if x % d == 0 and primelist[int(d + x/d)] == False:
                    isvalid = False
                    break
        
        if isvalid == True:
            totalsum += x
            
    return totalsum 
    
if __name__ == "__main__":
    print(compute1(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))