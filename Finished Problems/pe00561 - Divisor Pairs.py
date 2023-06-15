# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 23:34:05 2023

@author: igorvanloo
"""
'''
Project Euler Problem 721

p_m# = p_1*p_2*...*p_m so it will have 2^m divisors

writing a brute force solution I can see that 

S((p_m) ^ 1) follows https://oeis.org/A001047 defined by 3^m - 2^m  
S((p_m)^2) follows https://oeis.org/A248225 defined by 6^m - 3^m  
S((p_m)^3) follows https://oeis.org/A248338 defined by 10^m - 4^m

I guess S((p_m)^4) = 15^m - 5^m? correct! For sanity S((p_m)^5) = 21^m - 6^m, also correct

So I guess that S((p_m)^n) =  ((n + 1)(n + 2)//2) ^ m - (n + 1)^m

E(m, n) = largest k such that 2^k divides S((p_m)^n) = ((n + 1)(n + 2)/2) ^ m - (n + 1)^m

Therefore for k to be greater than 0, n must be odd so that (n + 1) is even

and we need n + 1 = 4k since if n + 1 is even n + 2 is odd hence 2 divides n + 1

then if (n + 1)(n + 2)/2 needs to be even hence n + 1 must be divisible by 4

so n = 4k - 1           

When n = 4k - 1, we have that (n + 1)/2 is even we just need to see how many times 2 divides (n + 1)/2 then 
multiply it by m
              
If we can quickly find the highest power of 2 dividing (n + 1)/2 we are done https://oeis.org/A001511

This has partial sum https://oeis.org/A005187 = 2*n - bit_count(n)

so we just need to find the amount of terms 4k - 1 from 1 to N which is just (N - 3)//4
              
using this I get Q(8) = 2714883 which is 3 off and Q(10**12) = 452480499988235507 which is wrong

I'm forgetting about the case n = 4k
More in depth in problem explanation on website as it was getting messy without proper writing

Anwser:
    452480999988235494
--- 0.0 seconds ---
'''

import time
from mathslib.divisors import divisors

start_time = time.time()

def S_P_brute_force(m, n):
    div = divisors(m**n)
    total = 0
    for x in range(len(div)):
        d1 = div[x]
        t = 0
        for y in range(x + 1, len(div)):
            d2 = div[y]
            if d2 % d1 == 0:
                t += 1
        total += t
    return total
    
def Q(n):
    m = 904961
    c = (n - 3)//4 + 1
    return (2*(n//4) - bin(n//4).count("1")) + m*(2*c - bin(c).count("1")) 

if __name__ == "__main__":
    print(Q(10**12))
    print("--- %s seconds ---" % (time.time() - start_time))
