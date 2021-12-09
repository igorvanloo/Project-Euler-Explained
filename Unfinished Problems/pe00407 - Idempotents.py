#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 23:37:35 2021

@author: igorvanloo
"""

'''
Project Euler Problem 407

If we calculate a^2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a^2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a^2 ≡ a (mod n).
So M(6) = 4.

Find ∑ M(n) for 1 ≤ n ≤ 107.

Reasoning

Method 1:
a^2 ≡ a (mod n) -> a^2 - a = 0 (mod n) -> a(a-1) = 0 (mod n)     (1)

Notice that for n = p1^e1 * p2^e2 * ... * pr^er there are 2^r roots to the above equation (1)

For example 6 = 2*3 therefore we expect 4 roots, they are 0, 1, 3, 4

To find them analyticaly we notice that x = 0 (mod n) or x = 1 (mod n)

so the anwser for m = 6 are

1) x = 0 mod 6 and x = 1 mod 1 -> x = 0
2) x = 0 mod 1 and x = 1 mod 6 -> x = 1
3) x = 0 mod 3 and x = 1 mod 2 -> x = 3
4) x = 0 mod 2 and x = 1 mod 3 -> x = 4

Usuing the Divisors of a number we can quickly do a chinese remainder theorem to find all the roots in the quickcrt function
however, it is too slow to finish the problem

Anwser:
    Get correct answers but code is too slow to finish, up to 10^5
'''

import time, math, eulerlib
start_time = time.time()

listofprimes = eulerlib.primes(10**7)
print("Primes done")
primegen = (time.time() - start_time)
print("--- %s seconds ---" % (primegen))

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
    
def primefactorization(n): 
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
    tempfactors = list(set(factors))
    #final = []
    #for x in tempfactors:
        #final.append(x**(factors.count(x)))
    return tempfactors

def Divisors(x): #Find the divisors of a number
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            #divisors.append(int(x/i))
    #divisors.remove(x)
    return (divisors)

def quickcrt(number):
    if is_prime(number) == True:
        return 1
    else:
        factors = Divisors(number)
        candidates = [0,1]
                
        for y in factors:
            mod1 = y #x = 0 mod mod1
            mod2 = int(number/y) #x = 1 mod mod2
            
            can = [x*mod1 for x in range(1,mod2)]
            
            for z in can:
                if (z-1) % mod2 == 0:
                    candidates.append(z)
                    
            can2 = [x*mod2 for x in range(1,mod1)]
            
            for z in can2:
                if (z-1) % mod1 == 0:
                    candidates.append(z)
            
        return max(candidates)

def quickcrt2(number): #faster but still too slow
    if is_prime(number) == True:
        return 1
    else:
        factors = primefactorization(number)
        can = []
        for x in factors:
            can += [x*n for n in range(1,int(number/x))]
        can = sorted(can)
        
        while True:
            try:
                y = can.pop(-1)
                if (y**2 - y) % number == 0:
                    break
            except IndexError:
                y = 1
                break
        return y
    
def compute(value):
    total = 0
    
    for x in range(2,value+1):
        total += quickcrt2(x)
        
    return total
    
if __name__ == "__main__":
    print(compute(10**4))
    print("--- %s seconds ---" % (time.time() - start_time - primegen))
    
    
    
    
    