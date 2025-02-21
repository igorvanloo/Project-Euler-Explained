# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:02:26 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 171

https://oeis.org/A175396

Basically problem 725 + 885

885 gives us a way to generate increasing strings
725 tells us how to count the number of permutations and the sum of all of them

It is exactly the same except we omit the partition part of the problem

Answer:
    142989277
--- 88.24478936195374 seconds ---
''' 
import time, math
import itertools
start_time = time.time()

def f(n):
    return sum(int(i)*int(i) for i in str(n))

def is_square(x):
    sr = (x ** (1 / 2))
    if round(sr) ** 2 == x:
        return True
    return False

def combs(x):
    n = len(x)
    total = math.factorial(n)
    t = 0
    for v in range(10):
        c = x.count(str(v))
        total //= math.factorial(c)
        t += c*v
    return (total*t//n % 10**9) * int("1"*min(n, 9)) % 10**9

def compute(n):
    total = 0
    for i, x in enumerate(itertools.combinations_with_replacement("0123456789", n)):
        t = sum(int(i)*int(i) for i in x)
        if t == 0:
            pass
        elif is_square(t):
            total += combs(x)
            total %= 10**9
    return total
    
if __name__ == "__main__":
    print(compute(20))
    print("--- %s seconds ---" % (time.time() - start_time))
