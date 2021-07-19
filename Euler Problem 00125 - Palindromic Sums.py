#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:05:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 125

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 
    6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and 
the sum of these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with 
the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive 
squares

Reasoning

Way #1: Turned out too be too slow 
    
We can simply generate all palindromes less than 10^8

Now if a number, say N, is a sum of consecutive squares then N = a^2 + (a+1)^2 + ... + (a+n)^2

=> N = a^2 + (a+1)^2 + ... + (a+n)^2 = sum from i = 0 to n of (n + 1)(6a^2 + 6an + 2n^2 + n)/6

So we can simply start at a = 1 and if a^2 > N and a sequence has not been found then it is not 

Way #2:

Generate the maximum n possible that is 1^2 + ... + n^2 < 10**8 (n = 668)

a consecutive square number must be of the form a^2 + (a+1)^2 = 2a^2 + 2a + 1 therefore the biggest a possible is

2a^2 + 2a + 1 = x => 2a^2 + 2a + (1-x) = 0 use quadratic formula to find maximum a

Then loop through all a then n and create sum a^2 + (a+n)^2 + ... if the sum goes over the limit break it to move onto
next a, if the sum is palindromic add it too a list

Right at the end make the list a set to remove duplicates

Anwser:
    (166, 2906969179)
--- 0.29149484634399414 seconds ---
'''

import time, math, eulerlib
start_time = time.time()

def is_quadratic(x):
    cube__root = (x**(1/2))
    if round(cube__root) ** 2 == x:
        return True
    return False

def compute(uptill):
    palindromes =[x for x in range(2,uptill + 1) if str(x) == str(x)[::-1]]
    print("palindromes Ready")
    print("--- %s seconds ---" % (time.time() - start_time))
    
    candidates = []
    for y in palindromes:
        if is_quadratic(y) == True:
            pass
        elif Is_Sum_Consecutive_squares(y) == True:
            candidates.append(y)
    return len(candidates), sum(candidates)

def Is_Sum_Consecutive_squares(N):
    for a in range(1,int(math.sqrt(N))):
        i = 0
        tempsum = 0
        while True:
            tempsum += (a+i)**2
            
            if tempsum > N:
                break
            
            if tempsum == N:
                return True
                break
            i += 1
    return False
            
def quadraticformula(a,b,c):
    return (-a + math.sqrt(b**2 - 4*a*c))/(2*a)

def compute1(limit):
    maxn = 0
    while (maxn+1)*(2*maxn+1)*maxn/6 < limit:
        maxn += 1
    maxn -= 1
    
    candidates = []
    for a in range(1,math.floor(quadraticformula(2,2,1-limit))+1):
        print(a)
        tempsum = a**2
        for n in range(1, maxn+1):
            tempsum += (a+n)**2
            
            if tempsum > limit:
                break
            
            if str(tempsum) == str(tempsum)[::-1]:
                candidates.append(tempsum)
    candidates = list(set(candidates))
    return len(candidates), sum(candidates)

if __name__ == "__main__":
    #print(compute(10**6))
    print(compute1(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))