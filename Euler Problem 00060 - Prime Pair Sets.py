#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:05:57 2021

@author: igorvanloo
"""

'''
Project Euler Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the 
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

Anwser:
    [26033, [13, 5197, 5701, 6733, 8389]]
--- 190.72501707077026 seconds ---
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

def MergedPrimeChecker(prime1, prime2):
    return (is_prime(int(str(prime1) + str(prime2))) and is_prime(int(str(prime2) + str(prime1))))
                
def compute():
    primes = eulerlib.primes(9000)
    
    length = len(primes)
    candidates = []
    for a in range(length):
        print(a)
        for b in range(a+1,length):
            if MergedPrimeChecker(primes[a],primes[b]) == True:
                for c in range(b+1, length):
                    if MergedPrimeChecker(primes[a],primes[c]) == True and MergedPrimeChecker(primes[b],primes[c]) == True:
                        for d in range(c+1, length):
                            if MergedPrimeChecker(primes[a],primes[d]) == True and MergedPrimeChecker(primes[b],primes[d]) == True and MergedPrimeChecker(primes[c],primes[d]) == True:
                                #value = [primes[a],primes[b],primes[c],primes[d]]
                                #candidates.append([sum(value), value])
                                for e in range(d+1,length):
                                    if MergedPrimeChecker(primes[a],primes[e]) == True and MergedPrimeChecker(primes[b],primes[e]) == True and MergedPrimeChecker(primes[c],primes[e]) == True and MergedPrimeChecker(primes[d],primes[e]) == True:
                                        value = [primes[a],primes[b],primes[c],primes[d],primes[e]]
                                        candidates.append([sum(value), value])
    
    candidates = sorted(candidates)
    return candidates[0]
                
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))