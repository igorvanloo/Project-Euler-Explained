#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:13:05 2022

@author: igorvanloo
"""
'''
Project Euler Problem 279

Law of cosine: c^2 = a^2 + b^2 -2abcos(C) where c is the hypotenuse
cos(C) = (c^2 - a^2 - b^2)/(2ab) therefore if a, b, c are rational then cos(C) will be rational which further implies that 
C = 60, 90, 120, cos(C) = 1/2, 0, -1/2 respectively

for 60 degree case
a = m^2 + n^2 - mn
b = 2mn - n^2
c = m^2 - n^2

for 90 degree case
We have pythagorean triples

for 120 degree case
a = m^2 + mn + n^2
b = 2mn + n^2
c = m^2 - n^2

Anwser:
    416577688
--- 182.64401006698608 seconds ---
'''
import time, math
start_time = time.time()

def DegreeIntegerTriangles90(limit):  # Pythagorean Triplet generator
    total = 0
    for m in range(2, int(math.sqrt(limit)) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1:
                if math.gcd(m, n) == 1:
                    a = m ** 2 + n ** 2
                    b = m ** 2 - n ** 2
                    c = 2 * m * n
                    p = a + b + c
                    if p <= limit:
                        total += limit//p
    return total

def DegreeIntegerTriangles60(limit):
    total = 0
    for m in range(2, int(math.sqrt(limit*1.5)) + 1):
        for n in range(1, m//2 + 1):
            if math.gcd(m, n) == 1:
                a = m ** 2 + n ** 2 - m*n
                b = 2 * m * n - n*n
                c = m*m - n*n
                p = a + b + c
                if (a % 3, b % 3, c % 3) == (0, 0, 0):
                    p //= 3
                if p <= limit:
                    total += limit//p
    return total

def DegreeIntegerTriangles120(limit):
    total = 0
    for m in range(2, int(math.sqrt(limit)) + 1):
        for n in range(1, m):
            if m % 3 != n % 3:
                if math.gcd(m, n) == 1:
                    a = m ** 2 + n ** 2 + m*n
                    b = 2 * m * n + n*n
                    c = m*m - n*n
                    p = a + b + c
                    if p <= limit:
                        total += limit//p
    return total

def compute(limit):
    a = DegreeIntegerTriangles60(limit)
    print(1)
    b = DegreeIntegerTriangles90(limit)
    print(2)
    c = DegreeIntegerTriangles120(limit)
    print(3)
    return a + b + c

if __name__ == "__main__":
    print(compute(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))
