#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:42:18 2021

@author: igorvanloo
"""

'''
Project Euler Problem 148

We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

 	 	 	 	 	 	 1
 	 	 	 	 	 1	 	 1
 	 	 	 	 1	 	 2	 	 1
 	 	 	 1	 	 3	 	 3	 	 1
 	 	 1	 	 4	 	 6	 	 4	 	 1
 	 1	 	 5	 	10	 	10	 	 5	 	 1
1	 	 6	 	15	 	20	 	15	 	 6	 	 1
However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (10^9) rows of Pascal's triangle.

Research

In the (n+1)th row of pascals triangle there are (n(k) + 1)(n(k-1) + 1)..(n(1) + 1)(n(0) + 1) numbers which are not divisble by p = a prime
where n = n(k)p^k + ... + n(1)p + n(0)

so for p = 7

we see row 7 = 10 in base 7 (1+1)(1+0) = 2 therefore there are 2 numbers in row 7 not divisble by 7

We can beging to see a pattern
1 = 1 = 2
...
6 = 6 = 7
7 = 10 = 2
8 = 11 = 4 
9 = 12 = 6
...
13 = 16 = 14
14 = 20 = 3
15 = 21 = 6
16 = 22 = 9
...
20 = 26 = 21
21 = 30 = 4
...
27 = 36 = 28
28 = 40 = 5
...
34 = 46 = 35
35 = 50 = 6
...
41 = 56 = 42
42 = 60 = 7
....
48 = 66 = 49
49 = 100 = 2

Therefore the sum of the first 7 rows = 28
the sum of the first 7^2 = 49 rows = 1*28 + 2*28 + 3*28 + 4*28 + ... + 7*28 = 28^2
sum of the first 7^3 = 343 rows = 28^3

They key is now to notice that floor(mod(10^9,7) = 10
so we start with x = 10^9 - 7^10, this adds 28^10 to the total number
now flor(mod(x,7)) = 10 so y = x - 7^10, but remember in the 2nd set of rows we will have 2*28^10 from our pattern

Here we can see that essentially we are given a pattern from the base 7 representation of 10**9

Anwser:
    2129970655314432
--- 2060.63307595253 seconds ---

    2129970655314432.0
--- 0.001024007797241211 seconds ---
    
'''

import time, math
start_time = time.time()

def n_choose_r(n, r): #nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
    
def pascalstraingle(row):
    rows = []
    for x in range(row):
        rows.append([n_choose_r(x,r) for r in range(x+1)])
    
    return rows
    
def modxpascal(mod, row):
    original = pascalstraingle(row)
    
    for x in range(len(original)):
        count = 0
        for y in range(len(original[x])):
            if original[x][y] % 7 != 0:
                count += 1
        print(count)

def findprod(x, prime):
    i = 0
    while prime**i <= x:
        i += 1
    
    total = 1
    while x != 0:
        n = x // (prime**i)
        x -= n*(prime**i)
        i -= 1
        total *= (n+1)
        
    return total

def numberToBase1(n, b):
    if n == 0:
        return [0]
    total = 1
    while n:
        total *= (int(n % b)+1)
        n //= b
        
    return total

def compute1():
    
    total = 1
    for x in range(1,10**9):
        if x % 10**8 == 0:
            print("closer")
        total += numberToBase(x, 7)
    
    return total

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits .append(int(n % b))
        n //= b
    return (digits)[::-1]

def compute():
    baserep = numberToBase(10**9,7)
    total = 0
    for x in range(len(baserep)):
        factor = 1
        for z in range(x):
            factor *= (baserep[z] + 1)

        y = baserep[x]

        total += (factor * (y*(1+y)/2) * (28**(10-x)))
        print(x, factor, (y*(1+y)/2), (10-x))

        
    return total
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))