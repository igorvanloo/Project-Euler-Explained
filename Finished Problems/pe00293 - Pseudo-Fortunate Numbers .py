#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:42:37 2022

@author: igorvanloo
"""
'''
Project Euler Problem 293

An even positive integer N will be called admissible, if it is a power of 2 or its distinct prime factors are consecutive primes.
The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.

If N is admissible, the smallest integer M > 1 such that N+M is prime, will be called the pseudo-Fortunate number for N.

For example, N=630 is admissible since it is even and its distinct prime factors are the consecutive primes 2,3,5 and 7.
The next prime number after 631 is 641; hence, the pseudo-Fortunate number for 630 is M=11.
It can also be seen that the pseudo-Fortunate number for 16 is 3.

Find the sum of all distinct pseudo-Fortunate numbers for admissible numbers N less than 109.

Notes

If N is admissable and not a power of 2 then it must be a product of atleast 2 consecutive primes, therefore we only need primes
up till the square root

Anwser:
    2209
--- 2.8606112003326416 seconds ---
'''
import time, math
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2*i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

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

def fermat_primality_test(n):
    if pow(4, n - 1, n) == 1 and pow(6, n - 1, n) == 1:
        return True
    return False

def admissable(p, n, primes, limit):
    a_n = [n] #admissiable numbers
    i = primes.index(p) #index
    if n > limit:
        return []
    a_n += admissable(p, n*p, primes, limit)
    if i + 1 < len(primes):
        n_p = primes[i + 1] #next prime
        a_n += admissable(n_p, n*n_p, primes, limit)
    return a_n
    
def compute(limit):
    sqrt_limit = int(math.sqrt(limit)) + 1
    primes = list_primes(sqrt_limit)
    admissiable = sorted(admissable(2, 2, primes, limit))
    p_f = set() #pseudo-fortunate
    for n in admissiable:
        #print(n)
        m = 3
        cont = True
        while cont:
            if fermat_primality_test(n + m):
                if is_prime(n + m):
                    p_f.add(m)
                    cont = False
            m += 2
        #print(m)
    return sum(p_f)

if __name__ == "__main__":
    print(compute(10**9))
    print("--- %s seconds ---" % (time.time() - start_time))