# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:32:01 2024

@author: Igor Van Loo
"""
'''
Project Euler Problem 885

There are (n + 9)C9 increasing strings 

Think of stars and bars, imagine you have an n-digit number place the first bar once you've gone
past the 0's, then the 1', etc. There are 9 bars, n digits and you need to choose where to place the nine bars

Example:
    d_0|d_1d_2d_3d_4|||||||| = 01111
    d_0|d_1d_2d_3||||||||d_4 = 01119
    d_0|d_1d_2||d_3||||||d_4 = 01139
    
Then there for n = 18 we have 27C9 = 4,686,825 possibilities, we can brute force.

Use itertools, for each combinations, count how many there are using n!/prod (d_i)!
where d_i is the number of times d_i appears. For example 00001 appears 5!/4! = 5 times
they are 1, 10, 100, 1000, 10000

Answer:
    827850196
--- 26.190982341766357 seconds ---
'''

import time, math, itertools
start_time = time.time()

def combs(x):
    n = len(x)
    total = math.factorial(n)
    for v in range(10):
        total //= math.factorial(x.count(str(v)))
    return total * int("".join(x))
    
def S(n):
    mod = 1123455689
    total = 0
    for x in itertools.combinations_with_replacement("0123456789", n):
        total += combs(x)
    return int(total % mod)

if __name__ == "__main__":
    print(S(18))
    print("--- %s seconds ---" % (time.time() - start_time))
