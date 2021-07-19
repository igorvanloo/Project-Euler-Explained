#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 20:14:16 2021

@author: igorvanloo
"""

'''
Project Euler Problem 95

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors 
of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming 
a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

Reasoning:
    First I use a divisor function to find all the divisors and sum them
    then I will start looping them till i find my original number while increasing a count 
    once I find the longest chain I will just add that chain to a list and print the minimum element
    
Anwser:
    (28, 14316)
--- 75.3214340209961 seconds ---
'''

import time
from math import sqrt
from eulerlib import primes
from collections import Counter
start_time = time.time()

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(n)
            break
    return factors

def sum_of_divisors(number, prime_factors):
    factors = list(set(prime_factors))
    number_of_each = Counter(prime_factors)
    
    final = 1
    for i in range(0,len(factors)):
        total = 0
        for x in range(0,number_of_each[factors[i]]+1):
            total += (factors[i])**x
        final *= total
    return final - number

def Divisors(x): #Find the divisors of a number
    divisors = []
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    divisors.remove(x)
    return sum(set(divisors))

def chain_length(x):
    original = x
    loop = []
    while True:
        x = Divisors(x)
        loop.append(x)
        print(x)
        if x > 1000000:
            count = 0
            break
        elif x == 1:
            count = 0
            break
        elif x in loop and x != original:
            print("test")
            loop = []
            break
        elif x == original:
            break
    return len(loop)
        
def compute():
    
    maximum = 0
    maximumnum = 0
    for x in range(2, 1000000+1):
        if x % 100000 == 0:
            print(x)
            
        original = x
        loop = [x]
        
        while True:
            
            original = Divisors(original)
            
            
            if original > 1000000:
                loop = []
                break
            elif original == 1:
                loop = []
                break
            elif original in loop:
                if original == x:
                    break
                else:
                    loop = []
                    break
            elif original < x:
                loop = []
                break

            loop.append(original)
        #print(loop)  
        if len(loop) > maximum:
            maximum = len(loop)
            maximumnum = x
            
    return maximum, maximumnum

def compute1(limit):
    values = [0] + [1] * limit
    
    for x in range(2,int(limit/2) + 1):
        for y in range(1,int(limit/x)+1):
            if x*y != x:
                values[x*y] += x
    
    print("Values ready")
    
    maximum, maxchain = 0, []
    for x in range(1,len(values)):
        chain = [x]
        curr = values[x]
        while True:
            if curr in chain:
                if curr == x:
                    if len(chain) > maximum:
                        maximum, maxchain = len(chain), chain
                        break
                    break
                break
            
            if curr > limit:
                break
            chain.append(curr)
            curr = values[curr]
            
    return values
            
if __name__ == "__main__":
    #print(sum_of_divisors(999999, primefactorization(999999, listofprimes)))
    print(compute1(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))