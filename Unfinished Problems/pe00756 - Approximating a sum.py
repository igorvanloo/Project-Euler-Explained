#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:57:23 2021

@author: igorvanloo
"""

'''
Project Euler Problem 756

Not quite sure how to move forward, get a reasonable estimate for first case

Anwser:

'''

import time, math, random
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

def phi(n): #Euler's Totient Function
    total = n
    prime_factor = prime_factors(n)
    
    for p in prime_factor:
        total *= (1-1/p)
        
    return int(total)

def compute(n,m):
    S = sum([phi(x) for x in range(1,n+1)])
    
    trials = 1
    total_error = 0
    while trials < 10**3:
        choices = [x for x in range(1,n+1)]
        S_prime = [0]
        
        for x in range(m):
            temp_choice = random.choice(choices)
            choices.remove(temp_choice)
            S_prime.append(temp_choice)
        
        S_prime = sorted(S_prime)
        total = 0
        for y in range(1,len(S_prime)):
            t = phi(S_prime[y])
            total += t*(S_prime[y] - S_prime[y-1])
        
        error = S - total
        #print(error)
        total_error += error
        trials += 1
        
    return total_error/trials

if __name__ == "__main__":
    print(compute(10**4, 10**2))
    print("--- %s seconds ---" % (time.time() - start_time))