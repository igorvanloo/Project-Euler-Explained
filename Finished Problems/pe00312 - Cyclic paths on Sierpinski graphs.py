#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:58:20 2022

@author: igorvanloo
"""
'''
Project Euler Problem 312

https://oeis.org/A246959

C(n) = (3*C(n - 1))^3 for n > 4

C(n) = 8 * 12^((3^(n-2) - 3)/2)

Now lets look for cycles,

Notice the following 

1. C(n) % 13 = C(n + 2) % 13
2. C(n) % 13^2 = C(n + 6) % 13^2
3. C(n) % 13^3 = C(n + 6*13) % 13^3
4. C(n) % 13^4 = C(n + 6*13*13) % 13^4
etc etc
8. C(n) % 13^8 = C(n + 6*13**8) % 13^8

Using this we have that 

C(C(C(10 000))) % 13^8 = C(C(C(10 000)) % 6*13**6) % 13^8

C(C(10 000)) % 6*13**6 = C(C(10 000) % 6*13**4) % 6*13**6

C(10 000) % 6*13**4 = C(10 000 % 6*13**2) % 6*13**4

10 000 % 6*13**2 = 874

Anwser:
    324681947
--- 0.738008975982666 seconds ---
'''
import time
start_time = time.time()

def C(n, mod = None): #Explicit formula
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 8
    return 8*pow(12, (pow(3, (n-2)) - 3)//2, mod) % mod
    
def C1(n, mod = None): #Recursive defintion
    #Used this function to finds periods
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 8
    if n == 4:
        return 13824
    c1 = 13824
    c = [1, 1, 8, 13824 % mod]
    
    for _ in range(n - 4):
        cn = pow(3*c1, 3, mod)
        c1 = cn
        if c1 in c:
            return (len(c) - c.index(c1))
        c.append(c1)

def compute():
    x1 = 10000 % (6*13**2)
    print(x1)
    x2 = C(x1, (6*13**4))
    print(x2)
    x3 = C(x2, (6*13**6))
    print(x3)
    x4 = C(x3, (13**8))
    return x4

if __name__ == "__main__":
    print(C(C(C(10000 % (6*13**2), (6*13**4)), (6*13**6)), (13**8)))
    print("--- %s seconds ---" % (time.time() - start_time))
