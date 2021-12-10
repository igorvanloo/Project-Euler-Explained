#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:28:40 2021

@author: igorvanloo
"""

'''
Project Euler Problem 

Let d(p,n,0) be the multiplicative inverse of n modulo prime p, defined as n × d(p,n,0) = 1 mod p.
Let d(p,n,k) = sum{i = 1 to n} d(p,i,k−1) for k ≥ 1.
Let D(a,b,k) = sum{p} (d(p,p-1,k) mod p) for all primes a ≤ p < a + b.

You are given:

D(101,1,10) = 45
= d(101,100,10)
= d(101,1,9) + d(101,2,9) + ... + d(101,100,9)

d(101,1,9) = d(101,1,8) = ... = d(101,1,0) = x

d(101,2,9) = d(101,1,8) + d(101,2,8) = x + d(101,1,7) + d(101,2,7) = 2x + d(101,1,6) + d(101,2,6) = .. = 9x + d(101,2,0) = y

d(101,3,9) = d(101,1,8) + d(101,2,8) + d(101,3,8) = y + d(101,1,7) + d(101,2,7) + d(101,3,7)

Create array = [
                [d(101,1,0), d(101,2,0), d(101,3,0), ... , d(101,100,0)]
                [d(101,1,1), d(101,2,1), d(101,3,1), ... , d(101,100,1)]
                [d(101,1,2), d(101,2,2), d(101,3,2), ... , d(101,100,2)]
                .
                .
                .
                [d(101,1,10), d(101,2,10), d(101,3,10), ... , d(101,100,10)]
                ]
Then d(101, a, b) = d(101, a-1, b) + d(101, a, b-1) a,b ≥ 1

Now we can notice everything is essentialy a sum of the the first row, just need to figure out how many times to pick it

D(10^3,10^2,10^2) = 8334: Got it ~0.3 sec but having trouble moving forward

D(10^6,10^3,10^3) = 38162302
Find D(10^9,10^5,10^5).


Anwser:

'''

import time, math
start_time = time.time()

def n_choose_r(n, r): #nCr function
    if r > n:
        return 0
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
    
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

def d(p,n,k):
    array = []
    
    array.append([pow(i,-1,p) for i in range(1,n+1)])
    
    for x in range(1,k):
        row = [1]
        for y in range(1,n):
            row.append(array[x-1][y] + row[y-1])
        array.append(row)
    
    return sum(array[k-1])
    
def D(a,b,k):
    primes = [x for x in range(a, a+b) if is_prime(x)]
    total = 0
    
    
    for p in primes:
        inv = [0] + [pow(i,-1,p) for i in range(1,p)]
        
        total_1 = (sum([n_choose_r(p-x-2,k-1)*inv[x] for x in range(1,p-1)]) % p)
        
        total_2 = (d(p,p-1,k) % p)
        
        print(p, total_1, total_2)
    
    return total

if __name__ == "__main__":
    #print(D(101,1,10))
    print(D(10**3,10**2,10**2))
    #print(D(10**6,10**3,10**3))
    print("--- %s seconds ---" % (time.time() - start_time))