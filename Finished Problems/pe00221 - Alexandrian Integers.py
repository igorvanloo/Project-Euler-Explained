#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:20:13 2022

@author: igorvanloo
"""
'''
Project Euler Problem 221

A = p(p + k)((p^2 + 1)/k + p) where k|p^2 + 1 and p is a postive integer

We only need to loop through the first half of the divisors
if p^2 + 1 = ab then 
A_1 = p(p + a)((p^2 + 1)/a + p) = p(p + a)(b + p)
                                        ||
A_2 = p(p + b)((p^2 + 1)/b + p) = p(p + b)(a + p)

Anwser:
    1884161251122450
'''
import time, math
start_time = time.time()

def Divisors_of(x):  # Find the divisors of a number
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
    return (divisors)

def compute():
    alexandrian_integers = []
    p = 1
    while len(alexandrian_integers) < 500000:
        for k in Divisors_of(p*p + 1):
            #print(p, k, p*(p + k)*((p*p + 1)//k + p))
            alexandrian_integers.append(p*(p + k)*((p*p + 1)//k + p))
        p += 1
    print(p)
    return sorted(alexandrian_integers)[149999]

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
