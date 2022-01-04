#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 00:14:34 2021

@author: igorvanloo
"""

'''
Project Euler Problem 479

1/x = (k/x)^2*(k+x^2 - kx) => kx^3 - k^2x^2 + x - k^3 = 0 => x^3 - kx^2 + x/k - k^2 = 0

Now a general cubic d(x-a)(x-b)(x-c) = 0 => x^3 - x^2(a + b + c) + x(ab + ac + bc) - abc = 0

Therefore we have the following

a + b + c = k
ab + ac + bc = 1/k
abc = k^2

Now we also note that (a + b)^p * (a + c)^p * (b + c)^p = 2abc + a^2b + ab^2 + a^2c + ac^2 + b^2c + bc^2 = 

3abc + a^2b + ab^2 + a^2c + ac^2 + b^2c + bc^2 - abc = (a + b + c)*(ab + ac + bc) - abc = k * 1/k - k^2 = 1 - k^2

Therefore S(n) = sum_{1 ≤ p, k ≤ n} (1 - k^2)^p

Sum_{p = 1 to n} (1-k^2)^p = S

S - (1-k^2)S = (1- k^2) - (1-k^2)^(n+1)

=> S = ((1-k^2) - (1-k^2)^(n+1))/k^2 = (1-k^2)/(k^2) * (1 - (1-k^2)^(n))

Now this is simple to solve using modular division

Anwser:
    191541795
--- 3.9374263286590576 seconds ---
'''
import time, math
start_time = time.time()

def ModDivision(a,b,m):
    a = a % m
    inv = pow(b,-1,m)
    if(inv == -1):
        return "Division not defined"
    else:
        return (inv*a) % m
        
def compute(n):
    total = 0
    mod = 1000000007
    for k in range(2, n + 1):
        t = 1 - k*k
        total += (1 - pow(t, n, mod)) * ModDivision(t, 1 - t, mod)        
    return total % mod
            

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))