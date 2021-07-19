#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:08:19 2021

@author: igorvanloo
"""

'''
Project Euler Problem 347

The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96=32*3=25*3. For two distinct 
primes p and q let M(p,q,N) be the largest positive integer ≤N only divisible by both p and q and M(p,q,N)=0 if such a 
positive integer does not exist.

E.g. M(2,3,100)=96.
M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

Find S(10 000 000).

Reasoning

Just iterate through primes less than half of the limit because the lowest pair is 2, limit/2
and then iterate through the next prime

For each pair, iterate through their powers to find the max of x^a * x^b, sum this max to a total

Anwser:
    11109800204052
--- 37.969449043273926 seconds ---
    
'''

import time, math, eulerlib
start_time = time.time()


def primefactorization(n, listofprimes): #Requires a preloaded list of primes
    if is_prime(n) == True:
        return [n]
    else:
        factors = []
        while n != 1:
            for x in listofprimes:
                if n % x == 0:
                    factors.append(x)
                    n = n/x
                    break
        return list(set(factors))

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
    
def compute(): #Original try, works but is too slow
    limit = 100
    total = 0
    values = []
    listofprimes = eulerlib.primes(limit)
    for x in range(2, limit + 1):
        if len(primefactorization(x, listofprimes)) == 2:
            
            if primefactorization(x, listofprimes) in values:
                pos = values.index(primefactorization(x, listofprimes))
                values.pop(pos)
                subtract = values.pop(pos)
                total -= subtract
            
            values.append(primefactorization(x, listofprimes))
            values.append(x)
            total += x

    return values, total
            
def compute1(limit):
    primes = eulerlib.primes(limit/2)
    total = 0
    for x in range(len(primes)):
        for y in range(x+1,len(primes)):
            if primes[x] * primes[y] > limit:
                break
            
            
            maximum = 0
            for a in range(1,int(math.log(limit/primes[y],primes[x]))+1):
                
                for b in range(1,int(math.log(limit/primes[x],primes[y]))+1):
                    
                    value = primes[x]**a * primes[y]**b
                    if value > limit:
                        break
                    elif value > maximum:
                        #print(primes[x],primes[y],a,b)
                        maximum = value
            total += maximum
    return total
                

if __name__ == "__main__":
    print(compute1(10000000))
    #print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))