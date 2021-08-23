#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:06:38 2021

@author: igorvanloo
"""

'''
Project Euler Problem 518

Let S(n) = Σ a+b+c over all triples (a,b,c) such that:

a, b, and c are prime numbers.
a < b < c < n.
a+1, b+1, and c+1 form a geometric sequence.
For example, S(100) = 1035 with the following triples:

(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71), (11, 23, 47), (17, 23, 31), 
(17, 41, 97), (31, 47, 71), (71, 83, 97)

Find S(10^8).

Reasoning

we are looking for primes a < b < c s.t. (a+1), (b+1), (c+1) forms a geometric seuqence => (c+1)/(b+1) = (b+1)/(a+1) = r

Now let r = z / y, because a < b < c => r > 1 => z > y and gcd(z,y) = 1

Let x = (a+1)/y^2 => (a+1) = x * y * y, 
now (b+1) = r * (a+1) = z * x * y,
and (c+1) = r * (b+1) = z * z * x

Therefore we can determine all the triples (a+1, b+1, c+1) by using only z,y s.t z > y and gcd(z,y) = 1

Anwser:
    100315739184392
--- 55.269689083099365 seconds ---
    
'''

import time, math, eulerlib, itertools
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
    
def compute(x):
    primes = eulerlib.primes(x)
    print("Primes Ready")
    print(len(primes))
    
    total = 0
    
    for a in range(len(primes)):
        for b in range(a+1, len(primes)):
            
            temp = (((primes[b] + 1)**2)/(primes[a] + 1)) - 1

            if temp.is_integer() == True:
                if temp > x:
                    break
                else:
                    if is_prime(temp) == True:
                        total += (primes[a] + primes[b] + temp)
    return total
                    
def compute1(limit):
    #(a+1) = x * y * y, 
    #(b+1) = r * (a+1) = z * x * y,
    #(c+1) = r * (b+1) = z * z * x
    total = 0
    #We first find the possible x values. Notice that c + 1 = xzz <= limit, which implies that (a+1) = xyy <= limit
    #Because z > y > 0, we know y >= 1 => z >= 2 => c + 1 > 4x <= limit
    for x in range(1, limit//4 + 1):
        #Now we want to find y, we know that a + 1 = xyy, so we can begin to find all candidate values of y
        # with a simple if a >= limit break
        for y in range(1,int(math.sqrt((limit - 1)/x)) + 1):
            a = x * y * y - 1
            if a >= limit:
                break
            #now we want to find z, we know that gcd(y,z) == 1 and z > y > 0, so we can simply check these conditions,
            #check if c = xzz - 1 goes over the limit and finally check if our triple is valid
            if is_prime(a) == True:
                for z in range(y+1, int(math.sqrt((limit - 1)/x)) + 1):
                    if math.gcd(y, z) == 1:
                        c = x * z * z - 1
                        if c >= limit:
                            break
                        if is_prime(c) == True:
                            b = x * y * z - 1
                            if is_prime(b) == True:
                                total += (a+b+c)
    return total

def list_primality(n):
	# Sieve of Eratosthenes
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result

def compute2(limit):
    primes = list_primality(limit)
    print("Primes done", time.time() - start_time)
    #(a+1) = x * y * y, 
    #(b+1) = r * (a+1) = z * x * y,
    #(c+1) = r * (b+1) = z * z * x
    total = 0
    for z in range(2, int(math.sqrt(limit)) + 1):
        z2 = z**2
        for x in range(2, int(limit/4)+1):
            c = x * z2 - 1
            if c >= limit:
                break
            if primes[c] == True:
                for y in range(1, z):
                    if z % 2 == 0 and y % 2 == 0:
                        continue
                    b = x * y * z - 1
                    a = x * y * y - 1
                    if primes[a] == True and primes[b] == True:
                        if math.gcd(z,y) == 1:
                            total += (a+b+c)
    return total
                              
if __name__ == "__main__":
    print(compute2(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))