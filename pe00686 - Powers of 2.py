#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:15:37 2020

@author: igorvanloo
"""
'''
Project Euler Problem 686

2^7 = 128 is the first power of two whose leading digits are "12".
The next power of two whose leading digits are "12" is .

Define p(L, n) to be the nth-smallest value of j such that the base 10 representation of 2^j begins with the digits 
of L

You are also given that p(123, 45) = 12710

Find p(123, 678910)

Through testing I notice the next number such that 2^j starts with 123 is either 196, 289 or 485 away

we are looking for 
2^k = 123.....
2^k = 1.23... * 10^x
log(10)(2^k) = log(10)(1.23... * 10^x)
k*log(10)(2) = log(10)(1.23...) + x

Anwser:
    193060223
--- 65.81834173202515 seconds ---
    
'''

import time, math
start_time = time.time()

def compute(n):
    lower = math.log(1.23, 10)
    upper = math.log(1.24, 10)
    cons = math.log(2,10)
    count = 0
    j = 0
    while count != n:
        j += 1
        temp = j*cons
        if lower < temp - math.floor(temp) < upper:
            count += 1
    return j
    
if __name__ == "__main__":
    print(compute(678910))
    print("--- %s seconds ---" % (time.time() - start_time))
    

    