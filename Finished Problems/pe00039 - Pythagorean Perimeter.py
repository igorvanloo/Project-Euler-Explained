#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:41:11 2020

@author: igorvanloo
"""

'''
Project Euler Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Anwser:
    (8, 840)
--- 4.679589748382568 seconds ---
'''

import time, math
start_time = time.time()
            
def ppt(limit): #Pythagorean Triplet generator
    triples = [0] * (limit+1)
    for m in range(2,int(math.sqrt(limit))+1):
        for n in range(1,m):
            if (m+n) % 2 == 1 and math.gcd(m,n) == 1:
                a = m**2 + n**2
                b = m**2 - n**2
                c = 2*m*n
                
                p = sum([a,b,c])
                
                for k in range(1,int(limit/p)+1):
                    triples[k*p] += 1
    return triples.index(max(triples))
        
if __name__ == "__main__":
    print(ppt(1000))
    print("--- %s seconds ---" % (time.time() - start_time))