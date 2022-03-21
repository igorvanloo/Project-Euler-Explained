#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:24:10 2022

@author: igorvanloo
"""

'''
Project Euler Problem 510

I've solved a similar problem in class,

I know that 1/sqrt(c) = 1/sqrt(b) + 1/sqrt(a) => sqrt(c) = sqrt(a)sqrt(b)/(sqrt(a) + sqrt(b))

Therefore c = ab/(a+b+2sqrt(ab))
Let g = gcd(a,b)
then a = ga_1, b = gb_1 where gcd(a_1, b_1) = 1

This means c = a_1b_1g/(a_1+b_1+2sqrt(a_1b_1))
And we know a_1b_1 must be a an integer => a_1b_1 = z^2
therefore a_1 = x^2, b_1 = y^2

Finally we have:

c = x^2y^2g/(x^2 + y^2 + 2xy) = (xy)^2g/(x+y)^2, any because gcd(x, y) = 1 we conclude that g = n*(x+y)^2

a = n(x+y)^2x^2
b = n(x+y)^2y^2
c = nx^2y^2

if b ≤ l => n(x+y)^2y^2 ≤ l => y^4 < nx^2y^2 + 2nxy^3 + ny^4 ≤ l
We generate all co-prime (x,y) such that x < y and y^4 < l and find all multiples
sum of all multiples is triangular numbers

Anwser:
    315306518862563689 ~ Original solution
--- 199.28916096687317 seconds ---

    315306518862563689 ~ Upgraded solution
--- 0.01795673370361328 seconds ---
'''

import time, math
start_time = time.time()

def T(n):
    return (n*(n+1))//2

def compute(limit): #Initial solution
    total = 0
    sqrt = int(math.sqrt(limit)) + 1
    print(sqrt)
    for b in range(1, limit):
        if b % 1000 == 0:
            print(b)
        if b*b > limit:
            break
        for a in range(1, b + 1):
            if a*a > limit:
                break
            a1 = a*a
            b1 = b*b
            num = a1*b1
            den = (a+b)*(a+b)
            if num % den == 0:
                c = num//den
                if math.gcd(a1, b1, c) == 1:
                    m = (limit//b1)
                    total += (a1 + b1 + c) * T(m)
    return int(total)

def compute_modified(limit): #After solving I found a new algorithm
    total = 0
    for y in range(1, int(limit**(0.25)) + 1):
        x = 1
        while x <= y:
            if math.gcd(x, y) == 1:
                a = pow((x + y)*x, 2)
                b = pow((x + y)*y, 2)
                c = pow(y*x, 2)
                m = limit//b
                total += (a + b + c) * T(m)
            x += 1
    return total

if __name__ == "__main__":
    print(compute_modified(10**9))
    print("--- %s seconds ---" % (time.time() - start_time))