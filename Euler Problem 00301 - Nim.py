#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:02:53 2021

@author: igorvanloo
"""

'''
Project Euler Problem 301

The function X is called nim-sum and it cancels binary bits that are equal for example it is defined by the ^ operation
    1 0 1
+   0 1 0
=   1 1 1

but 
    1 0 1
+   1 1 1
=   0 1 0

1) n + 2n = 3n
2) a ^ b = 0 iff a = b
3) 2n = n with 1 extra 0 in binary

n^2n^3n = 0 is what we want
=> (n^2n)^3n = 0 therefore by point 2 n^2n = 3n = 2n + n
So we need n^2n = 2n + n

Using point 3, we deduce that n^2n = 2n + n, there cannot be any consecutive 1's in the binary representation of n
why? because then shitfing it one to the left and adding would cause a shift because of overlapping 1's,

    11
+   110
=   1001 but 11^110 = 101

So we must find all n that do not have consecutive 1's

Number of binary strings that do not contain consecutive 1's, denote this with a(n) where n is the length of the string

then consider a(n) can end with either 1) _ _ _ _ _ 1 or 2) _ _ _ _ _ 0

In case 1 the results in _ _ _ _ _ 0 1 which is a(n-2) strings with no 2 consectuive 1's
In case 2 it results in a(n-1) strings

So we get the recurrence a(n) = a(n-1) + a(n-2) where a(1) = 2, a(2) = 3

We notice that this is simply a shifting fibonnaci sequence by 2 so a(n) = f(n+2)

bin(2**30) = 0b1000000000000000000000000000000 which is 31 digits long, so we want to look for the number of strings with
length 30 that do not have consecutive 1's

that is a(30) = f(n+2)

Anwser:
    2178309
--- 0.00021505355834960938 seconds ---
    
'''

import time
start_time = time.time()

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2

def compute():
    count = 0
    for n in range(1,2**30 + 1):
        if n % 10**6 == 0:
            print(n)            
        if int(bin(n)[2:])^int(bin(2*n)[2:])^int(bin(3*n)[2:]) == 0:
            print(n)
            count += 1
    return count

if __name__ == "__main__":
    print(fibonnaci(32))
    print("--- %s seconds ---" % (time.time() - start_time))