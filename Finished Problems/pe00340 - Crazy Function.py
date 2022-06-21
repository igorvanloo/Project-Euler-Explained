#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:55:34 2021

@author: igorvanloo
"""
'''
Project Euler Problem 340

It is clear that recursion will not work, we need to somehow simplify F(n) and S(n)

Notice that if n in range (b-a, b] then a + n > b, and then we have that 
F(a + n) = a + n - c

Therefore F(n) = F(a + F(a + F(a + a + n - c))) = F(a + F(a + F(2a + n - c))), therefore if a > c then 
2a + n - c > b => F(n) = F(a + F(a + 2a + n - 2c)) = F(a + F(3a + n - 2c)) = 
F(4a + n - 3c) = 4a + n - 4c

Notice in our problem a = 21^7 > 12^7 = c, so that part is fine, but what about numbers in the range
[0, b - a]?

Well notice that if n is in the range (b - 2a, b - a] then we have that a + n is in
the range (b - a, b]!

Therefore we have that F(a + n) = 5a + n - 4c, hence 
F(n) = F(a + F(a + F(a + 5a + n - 4c))) = 8a + n - 7c

Continuing we will get if n is in the range (b - 3a, b - 2a] then a + n is in preceding range, etc, etc
F(n) = 12a + n - 11c, etc, etc

Therefore we conclude:
If n is in the range (b - (k + 1)a, b - ka] k ≥ 0, then
F(n) = 4(k + 1)a + n - (3k + 4)c

We can now instantly solve F(n), but summing 7^21 terms will take forever, we need to efficiently compute S(a, b, c)

S(a, b, c) = sum_{n = 0 to b} F(n)
We split this up into the different k values

S(a, b, c) = sum_{k = 0 to b/a} a*(4(k + 1)a - (3k + 4)c) + sum_{n = b - (k + 1)a to b - ka} n
Therefore
S(a, b, c) = sum_{k = 0 to b/a} a*(4(k + 1)a - (3k + 4)c) + 1/2(a + 1)(2ak + a - 2b)

sum_{k = 0 to b/a} a*(4(k + 1)a - (3k + 4)c) = sum_{k = 0 to b/a} 4kaa + 4aa - 3kac - 4ac

Anwser:
    291504964
--- 4.9114227294921875e-05 seconds ---
'''
import time, math
start_time = time.time()

def S(a, b, c, mod):
    if c > a:
      return "a must be greater than c"
    k = b//a
    a %= mod
    b %= mod
    c %= mod
    total = (((b + 1)*b)//2) % mod #Sum of all n
    total += (((((k - 1)*k)//2)*(4*a*a - 3*a*c) % mod) + (4*a*k*(a-c) % mod)) % mod #sum_{k = 0 to b/a} a*(4(k + 1)a - (3k + 4)c)
    total += (b - k*a + 1)*(4*(k + 1)*a - (3*k + 4)*c) % mod #Sum of the remaining terms
    return total % mod
 
if __name__ == "__main__":
    print(S(50, 2000, 40, 10**9))
    print(S(21**7, 7**21, 12**7, 10**9))
    print("--- %s seconds ---" % (time.time() - start_time))