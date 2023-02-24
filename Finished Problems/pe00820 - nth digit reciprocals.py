# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:42:24 2023

@author: igorvanloo
"""
'''
Project Euler Problem 820

d_n(x) = n-th decimal digit of fractional part of x, or 0 if fractional part has fewer than n digits

lets say 1/x = a.bcde ... n so that the n-th decimal digit is n
then 10^n/x = abcde ... n.op ...

We then have that n = floor(10^n/x) (mod 10) 
                    = floor(10*(10^(n - 1)))/x (mod 10)
                    = floor(10 * (10^(n - 1) (mod x)) / x)
                    
Anwser:
    44967734
--- 18.91725778579712 seconds ---
'''
import time
start_time = time.time()

def d(n, k):
    return (10 * pow(10, n - 1, k)) // k

def S(n):
    return sum([d(n, k) for k in range(1, n + 1)])

if __name__ == "__main__":
    print(S(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))
