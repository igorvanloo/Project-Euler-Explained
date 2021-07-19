#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:01:25 2020

@author: igorvanloo
"""

'''
Project Euler Problem 75

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right 
angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, 
and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form 
exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided 
right angle triangle be formed?

Reasoning:
    This formula produces primitive pythagorean triples when, gcd(m,n)=1, m,n have the same parity
    a = (m**2 - n**2)/2
    b = m*n
    c = (m**2 + n**2)/2
    L = a + b + c = mn + m^2 = m(n+m)
    
    Our stopping limit will be when n = 1 and a+b+c > 1500000
    so when n = 1 L = m^2 + m therefore m = 1224.23 or -1225, we take ceiling(m) + 1 = 1226 as the limit
    We create all primitive triplets and then add on their multiples
    Then we check the count for each one, we look through the loop once and check its count if it is 1 count +=1
    *Still dont understand why it goes over the limit*
    
    a = (m^2 - n^2)
    b = 2nm
    c = (m^2 + n^2)
    if n = 1, a + b + c = (2m^2 + 2m) < 1,500,000 => maximum m is 866
Anwser:
    161667
--- 1.1126022338867188 seconds ---    
'''

import time
from math import gcd, ceil
from itertools import count
from collections import Counter
start_time = time.time()

def primitivepythagoreantriplet(limit): #This function will produce a list of all pythagorean triples under the limit
    triples = []
    for m in count(3,2):
        for n in range(1,m,2):
            if gcd(n,m) == 1:
                a = (m**2 - n**2)//2
                b = m*n
                c = (m**2 + n**2)//2
                if n==1 and a+b+c > limit:
                    return sorted(triples)
                    break
                triples.append(a+b+c)
                for z in range(2,ceil(limit/(a+b+c))):
                    if z*(a+b+c) <= limit:
                        triples.append(z*(a+b+c))
    
def compute():
    count = 0
    checking_list = primitivepythagoreantriplet(1500000)
    counter_list = Counter(checking_list)
    
    for x in range(len(checking_list)):
        if checking_list[x] <= 1500000:
            if counter_list[checking_list[x]] == 1:
                count += 1
    return count

def ppt(limit):
    arr = [0]*(limit+1)
    for m in range(2,1000):
        for n in range(1,m):
            if (m+n) % 2 == 1 and gcd(m,n) == 1:
                a = m**2 + n**2
                b = m**2 - n**2
                c = 2*m*n
                
                p = a+b+c
                k = 1
                
                while k*p <= limit:
                    arr[k*p] += 1
                    k += 1
    return arr.count(1)

if __name__ == "__main__":
    print(ppt(1000000))
    print("--- %s seconds ---" % (time.time() - start_time))