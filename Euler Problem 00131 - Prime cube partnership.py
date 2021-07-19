#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:26:22 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

There are some prime values, p, for which there exists a positive integer, n, such that the expression n^3 + n^2p 
is a perfect cube.

For example, when p = 19, 8^3 + 8^2×19 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, 
and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

Notes:
    
n^3 + n^2p = x^3
n^3 (p/n + 1) = x^3 => n * cbrt(p/n + 1) = x
n * cbrt((p+n)/n) = x => p+n and n must both be perfect cubes

Also note that the largest prime below 1,000,000 is 999,983, and the first occurence where the difference between 2 cubic numbers
is greater than 999,983 is the 578th cubic

So this means for each prime below 1,000,000, we will find a cubic such that n+p is also a cubic

additional notes after solving:
    
n^3 + n^2p = n^2(p+n) = x^3 and we know p+n and n must both be perfect cubes so let n = k^3 and p+n = m^3

then p + n = m^3 = > p = m^3 - k^3 = (m-k)(m^2+mk-k^2) => m-k is a factor of p, but p is prime
therefore m-k = 1 = > m = k+1

p = (k+1)^3 - k^3 so p must be the difference of 2 cubes!


Anwser:
    173
--- 23.20402479171753 seconds ---

after revised notes 
--- 0.003423929214477539 seconds ---
    
'''

import time, eulerlib, math
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
    
def is_cubic(x):
    cube__root = (x**(1/3))
    if round(cube__root) ** 3 == x:
        return True
    return False

def compute():
    primes = eulerlib.primes(1000000)
    cbrt = [x**3 for x in range(1,579)]
    final = []
    for x in primes:
        for y in range(len(cbrt)):
            if is_cubic(x+cbrt[y]) == True:
                final.append((x, y))
            elif cbrt[y+1] - cbrt[y] > x:
                break
    return len(final)

def compute1():
    total = 0
    for x in range(1,577):
        if is_prime((x+1)**3 - x**3):
            total += 1
    return total

len([((x+1)**3 - x**3) for x in range(1,577) if is_prime((x+1)**3 - x**3)])

if __name__ == "__main__":
    print(compute1())
    print("--- %s seconds ---" % (time.time() - start_time))