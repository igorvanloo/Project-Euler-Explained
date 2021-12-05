#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:50:04 2021

@author: igorvanloo
"""

'''
Project Euler Problem 139

Given a triangle (a,b,c) a < b < c
the square in the middle is (b-a) x (b-a)
now if (b-a) square fits into c square then (b-a)|c
not if (b-a)|c then (kb-ka)|kc which means if a primitive pythagorean triple works, then all of it's multiples do as well

Anwser:
    10057761
--- 25.368075847625732 seconds ---
'''

import time, math
start_time = time.time()

def ppt(limit): #Pythagorean Triplet generator
    count = 0
    for m in range(2,int(math.sqrt(limit))+1):
        for n in range(1,m):
            if (m+n) % 2 == 1 and math.gcd(m,n) == 1:
                c = m**2 + n**2
                b = m**2 - n**2
                a = 2*m*n
                
                if a + b + c > limit:
                    break
                
                if c % abs(a-b) == 0:
                    p = a + b + c
                    for k in range(1, int(limit/p) + 1):
                        if k*p < limit:
                            count += 1
    return count

if __name__ == "__main__":
    print(ppt(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))