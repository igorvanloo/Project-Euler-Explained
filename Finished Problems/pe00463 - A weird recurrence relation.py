#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:22:09 2022

@author: igorvanloo
"""

'''
Project Euler Problem 463

f(1) = 1
f(3) = 3
f(2n) = f(n)
f(4n + 1) = 2f(2n + 1) - f(n)
f(4n + 3) = 3f(2n + 1) - 2f(n)

1) if n is even then we take f(n/2)
2) if n = 1 mod 4 => x = 4n + 1 => (x + 1)/2 = 2n + 1 and (x - 1)/4 = n
so we apply 2f((n + 1)/2) - f((x - 1)/4)
3) n = 3 mod 4 => x = 4n + 3 => (x - 1)/2 = 2n + 1 and (x - 3)/4 = n
so we apply 3f((x - 1)/2) - 2f((x - 3)/4)


        0, n < 1
        1, n = 1
f(n) =  f(n/2), n = even
        2f((n + 1)/2) - f((n - 1)/4), n = 1 mod 4
        3f((n - 1)/2) - 2f((n - 3)/4), n = 3 mod 4
        
S(n) = sum f(i)

f(4n + 3) - f(4n + 2) = f(4n + 3) - f(2(2n + 1)) = f(4n + 3) - f(2n + 1) = 2f(2n + 1) - 2f(n)
f(4n + 2) - f(4n + 1) = f(2(2n + 1)) - f(4n + 1) = f(2n + 1) - (2f(2n + 1) - f(n)) = -f(2n + 1) + f(n)
f(4n + 1) - f(4n) = f(4n + 1) - f(2(2n)) = f(4n + 1) - f(2n) = f(4n + 1) - f(n) =  2f(2n + 1) - 2f(n)

Therefore
f(4n + 3) + f(4n + 2) + f(4n + 1) + f(4n) = 2f(2n + 1) - 2f(n) + 2(-f(2n + 1) + f(n)) + 3(2f(2n + 1) - 2f(n)) + 4f(4n)

= 6f(2n + 1) - 6f(n) + 4f(n) = 6f(2n + 1) - 2f(n) = 6(f(2n + 1) + f(2n)) - 8f(n)

Finally we have S(4n + 3) = 6S(2n + 1) - 8S(n)

Similarly 

S(4n + 2) = f(4n + 2) + f(4n + 1) + f(4n) = 2(-f(2n + 1) + f(n)) + 3(2f(2n + 1) - 2f(n)) + 4f(4n)
                                          = f(2n + 1) + 4f(2n) = S(2n + 1) - 3S(n)

f(1) = 1
f(2) = 1
f(3) = 3
f(4) = f(2) = 1
f(5) = 2f(3) - f(1) = 5

Anwser:
    808981553
--- 0.0008358955383300781 seconds ---
'''
import time
from functools import cache
start_time = time.time()

@cache
def f(n):
    if n == 1:
        return 1
    elif n == 3:
        return 3
    elif n % 2 == 0:
        return f(n//2)
    elif n % 4 == 1:
        return 2*f((n + 1)//2) - f((n - 1)//4)
    elif n % 4 == 3:
        return 3*f((n - 1)//2) - 2*f((n - 3)//4)

@cache
def S(n):
    total = 0
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 5
    
    t = (n - 3)//4
    if (n - 3) % 4 != 0:
        for x in range(4*t + 4, n + 1):
            total += f(x)
        
    total += (6*S(2*t + 1) - 8*S(t) - 1) % 10**9
             
    return total % 10**9

def bruteforce(limit):
    total = 0
    for n in range(1, limit + 1):
        total += f(n)
    return total

if __name__ == "__main__":
    print(S(3**37))
    print("--- %s seconds ---" % (time.time() - start_time))