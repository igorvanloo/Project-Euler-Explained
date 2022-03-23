#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:30:20 2022

@author: igorvanloo
"""

'''
Project Euler Problem 214

Just make a totient sieve and run through all the primes

Anwser:
    1677366278943
--- 54.66183590888977 seconds ---
'''
import time, math
start_time = time.time()

def totient_sieve(n): 
    phi = [i for i in range(n+1)]
    primes = []
    for p in range(2, n+1): 
        if phi[p] == p:
            primes.append(p)
            phi[p] -= 1
            for i in range(2*p, n+1, p):
                phi[i] -= (phi[i]//p)
    return phi, primes

def compute(limit, max_chain_length):
    totients, primes = totient_sieve(limit)
    print("totients and primes generated")
    
    def totient_chain_length(p, max_chain_length):
        curr = p - 1
        chain_length = 2
        while curr != 1 and chain_length < max_chain_length + 1:
            curr = totients[curr]
            chain_length += 1
        return chain_length
    
    total = 0
    for p in primes:
        if p >= 9548417: #Smallest prime that generates a 25 long chain
            if totient_chain_length(p, max_chain_length) == max_chain_length:
                #print(p)
                total += p
    return total            
    
if __name__ == "__main__":
    print(compute(4*10**7, 25))
    print("--- %s seconds ---" % (time.time() - start_time))