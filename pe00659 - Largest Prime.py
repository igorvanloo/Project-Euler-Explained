#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:39:22 2021

@author: igorvanloo
"""

'''
Project Euler Problem 659

Consider the sequence  $n^2+3$ with $n \ge 1$.
If we write down the first terms of this sequence we get
$4, 7, 12, 19, 28, 39, 52, 67, 84, 103, 124, 147, 172, 199, 228, 259, 292, 327, 364,$... .
We see that the terms for $n=6$ and $n=7$ ($39$ and $52$) are both divisible by $13$.
In fact $13$ is the largest prime dividing any two successive terms of this sequence.

Let $P(k)$ be the largest prime  that divides any two successive terms of the sequence $n^2+k^2$.

Find the last 18 digits of $\displaystyle \sum_{k=1}^{10\,000\,000} P(k)$.

Reasoning

let q be the biggest prime that divides n^2 + k^2 and (n+1)^2 + k^2

q|n^2 + k^2 and q|(n+1)^2 + k^2 => q|2n+1
q|4(n^2+k^2)=(2n+1)(2n-1) + 4k^2 + 1 => q|(2n+1)(2n-1) and q|4k^2 + 1

so q will be the largest prime factor of 4k^2 + 1

Using Sieve like algorithm to quickly find largest prime factor of 4k^2 + 1

Anwser:
    238518915714422000
--- 37.01978397369385 seconds ---
    
'''

import time
start_time = time.time()

def compute1(L): #First version got correct anwser in ~1050 seconds
    f = [0]+[int(4*(x**2)+1) for x in range(1, L+1)]
    maxelem = [0] + [0]*(L)
    for x in range(1,len(f)):
        #print("x ", str(x))
        list_max1 = int((L-x)/f[x])
        for k in range(0,list_max1+1):
            #print("k ", str(k))
            while f[x + k*f[x]] % f[x] == 0:
                if f[x + k*f[x]] / f[x] == 1:
                    
                    if maxelem[x + k*f[x]] < f[x]:
                        maxelem[x + k*f[x]] = f[x]
                        
                    break
                f[x + k*f[x]] /= f[x]
                
                if maxelem[x + k*f[x]] < f[x]:
                    maxelem[x + k*f[x]] = f[x]
                    
                f[x + k*f[x]] = int(f[x + k*f[x]])
       
        list_max2 = int((L+x)/f[x])
        for k in range(0,list_max2+1):
            while f[-x + k*f[x]] % f[x] == 0:
                if f[-x + k*f[x]] / f[x] == 1:
                    
                    if maxelem[-x + k*f[x]] < f[x]:
                        maxelem[-x + k*f[x]] = f[x]
                        
                    break
                
                f[-x + k*f[x]] /= f[x]
                
                if maxelem[-x + k*f[x]] < f[x]:
                    maxelem[-x + k*f[x]] = f[x]
                    
                f[-x + k*f[x]] = int(f[-x + k*f[x]])
                
    return sum(maxelem) % 10**18

def compute(limit): #Final version, gets anwser in ~ 40 seconds
    f = [int(4*(x**2)+1) for x in range(limit+1)]
    maxelem = [0]*(limit+1)
    for x in range(1,len(f)):
        div = f[x]
        if div > 1:
            curr1 = x % div
            while curr1 <= limit:
                if f[curr1] % div == 0:
                    maxelem[curr1] = max(maxelem[curr1], div)
                    while f[curr1] % div == 0:
                        f[curr1] //= div
                curr1 += div
            
            curr2 = -x % div
            while curr2 <= limit:
                if f[curr2] % div == 0:
                    maxelem[curr2] = max(maxelem[curr2], div)
                    while f[curr2] % div == 0:
                        f[curr2] //= div
                curr2 += div
    return sum(maxelem) % 10**18

if __name__ == "__main__":
    print(compute(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))