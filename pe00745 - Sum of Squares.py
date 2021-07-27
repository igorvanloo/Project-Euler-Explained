#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 01:36:32 2021

@author: igorvanloo
"""

'''
Project Euler Problem 745

Product of first 13 primes > 10^14

Anwser:
    94586478
--- 37.27331185340881 seconds ---
'''

import time, math
start_time = time.time()

def compute1(length): #For 10^8 724475280152 ~ 44 seconds still too slow
    squares = [x**2 for x in range(0,(length)+1)]
    max_square = [0] + [1] * (length**2)
    
    for x in range(2, len(squares)):
        start = squares[x]
        while start < length**2 + 1:
            
            max_square[start] = max(max_square[start], squares[x]) % 10**18
            
            start += squares[x]
    return sum(max_square) % 10**18
    
def S(N): #Faster varitation 10^8 ~ 7 seconds
    max_square = [1]*(N+1)
    limit = math.floor(math.sqrt(N))
    for x in range(2, limit+1):
        square = x**2
        for k in range(square, N+1, square):
            max_square[k] = square
    return sum(max_square[1:]) % 1000000007

def S1(N): #Reduced speed for 10^8 ~ 0.02 seconds, can be used to solve final problem
    sqrtN = int(math.sqrt(N))
    a = [0] + [1]*sqrtN
    for i in range(sqrtN,0,-1):
        a[i] = math.floor(N/(i*i)) - sum([a[i*j] for j in range(2,math.floor(sqrtN/i) + 1)])
    return (sum([i*i*a[i] for i in range(len(a))])) % 1_000_000_007
        
if __name__ == "__main__":
    print(S1(10**14))
    print("--- %s seconds ---" % (time.time() - start_time))