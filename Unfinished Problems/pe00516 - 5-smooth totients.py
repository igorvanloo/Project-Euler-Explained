#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 23:53:54 2021

@author: igorvanloo
"""
'''
Project Euler Problem 516

5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers.
Let S(L) be the sum of the numbers n not exceeding L such that Euler's totient function φ(n) is a Hamming number.
S(100)=3728.

Find S(10^12). Give your answer modulo 232.

Reasoning

Give a number n = p1^e1 * p2^e2 * ... * pk^ek
Euler totient function: phi(n) = p1^(e1-1) * (p1-1) * p2^(e2-1) * (p2-1) * ... * pk^(ek-1) * (pk-1)
a hamming number is of the form: 2^a * 3^b * 5^c

We are looking for all n from 1 till 10^12 such that phi(n) = 2^a * 3^b * 5^c

That is, phi(n) = p1^(e1-1) * (p1-1) * p2^(e2-1) * (p2-1) * ... * pk^(ek-1) * (pk-1) = 2^a * 3^b * 5^c

Of course this is means that phi(n) = p1^(e1-1) * (p1-1) * p2^(e2-1) * (p2-1) * p3^(e3-1) * (p3-1)
Where p1,p2,p3 are 2,3,5, therefore phi(n) = 2^(e1-1) * 3^(e2-1) * 2 * 5^(e3-1) * 4 = 2^(e1+2) * 3^(e2-1) * 5^(e3-1)


Anwser:
    
'''

import time, math, eulerlib
start_time = time.time()

listofprimes = eulerlib.primes(10**5)

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
        return set(factors)
    
def phi(n, primes): #Eulers Totient Function requires primefactorization and isprime function
    total = n
    prime_factor = primefactorization(n, primes)
    
    for p in prime_factor:
        total *= (1-(1/p))
        
    return int(total)

def HammingNumbers(uptillx):
    #all 5-smooth numbers are of the form 2^a * 3^b * 5^c
    numbers = []
    
    for a in range(int(math.log(uptillx, 2)) + 1):
        for b in range(int(math.log(uptillx, 3)) + 1):
            for c in range(int(math.log(uptillx, 5)) + 1):
                value = (2**a)*(3**b)*(5**c)
                if value <= uptillx:
                    numbers.append(value)
    return sorted(numbers)
    
def compute(x):
    hammingnumbers = HammingNumbers(x)
    total = 0
    for y in range(1,x + 1):
        if phi(y, listofprimes) in hammingnumbers:
            total += y
    return total

if __name__ == "__main__":
    print(compute(10**5))
    print("--- %s seconds ---" % (time.time() - start_time))
