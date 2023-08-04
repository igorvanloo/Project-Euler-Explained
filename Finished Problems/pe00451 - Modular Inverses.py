# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 16:22:57 2022

@author: igorvanloo
"""
'''
Project Euler Problem 451

Consider the number 15.
There are eight positive numbers less than 15 which are coprime to 15: 1, 2, 4, 7, 8, 11, 13, 14.
The modular inverses of these numbers modulo 15 are: 1, 8, 4, 13, 2, 11, 7, 14
because
1 · 1 mod 15=1
2 · 8=16 mod 15=1
4 · 4=16 mod 15=1
7 · 13=91 mod 15=1
11 · 11=121 mod 15=1
14 · 14=196 mod 15=1

Let I(n) be the largest positive number m smaller than n-1 such that the modular inverse of m modulo n equals m itself.
So I(15)=11.
Also I(100)=51 and I(7)=1.

Find ∑ I(n) for 3≤n≤2×107

So the problem is asking for the largest x <= n - 1 such that x^2 = 1 (mod n)

We use hensels lemma and chinese remainder theorem to solve I(n)

Lets say n = p1^e1 * p2^e2 * ... * pk^ek

Then we solve x^2 - 1 = 0 (mod pi^ei) for 1 <= i <= k and we use chinese remainder theorem to find the solution
for x^2 - 1 = 0 (mod n)

We know that x^2 - 1 = 0 (mod p) has 2 solutions, 1 and p - 1

and we know we can lift these solutions to mod p^2 using hensels lemma

Given our 2 solutions 1, -1 we know that f'(r) = +-2 (mod p) ≠ 0 if p ≠ 2 and = 0 if p = 2

1. p ≠ 2
2 possible solutions 1, -1, but then f(+-1) = 0 which means t = 0 and the solutions for 
x^2 - 1 (mod p^2) are just +- 1

And then means actually that if p ≠ 2 then x^2 = 1 (mod p^e) only has solutions x = +- 1

2. p = 2
If p = 2 it is slightly more complicated

x^2 = 1 (mod 2) has only 1 solution, 1 since 1 = -1

x^2 = 1 (mod 2^2) we can use hensels lemma second case where we get 2 solutions +- 1 again

x^2 = 1 (mod 2^3) we use hensels lemma

Since our solutions to x^2 = 1 (mod 2^2) were +- 1 we again have f(+- 1) = 0
we have solutions 1, 1 + 2^2 = 5, -1, -1 + 2^2 = 3 so we have 4 solutions 1, 3, 5, 7

x^2 = 1 (mod 2^4) using solutions +- 1 again we get new solutions +-1 and 2^3 +- 1

using solutions 2^2 +- 1 we get no solutions

So we can find I(n) now
                            

Anwser:
    153651073760956
--- 266.4094407558441 seconds ---
'''
import time, math
from functools import cache
start_time = time.time()

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                factors[n] = 1
            break
    return factors

def solve(p, e):
    if p == 2:
        if e == 1:
            return [1]
        elif e == 2:
            return [1, 3]
        else:
            x = p**(e - 1)
            return [1, x - 1, x + 1, 2*x - 1]
    else:
        return [1, p**e - 1]

@cache
def chinese_remainder_theorem(a1, a2, n1, n2):
    p, q = pow(n1, -1, n2), pow(n2, -1, n1)
    return (a1*q*n2+ a2*p*n1) % (n1*n2)

def I(n):
    pf = prime_factors(n)
    sols = [1]
    curr_num = 1
    for p in pf:
        e = pf[p]
        num = p**e
        curr = solve(p, e)
        curr_sols = []
        for x in sols:
            for y in curr:
                curr_sols.append(chinese_remainder_theorem(x, y, curr_num, num))
        sols = curr_sols
        curr_num *= num
    return sorted(curr_sols)[-2]

def spf_sieve(N):
    #smallest prime factor sieve
    spf = [i for i in range(N + 1)]
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if spf[i] == i:
            for j in range(i*i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

@cache
def crt(n1, n2):
    p, q = pow(n1, -1, n2), pow(n2, -1, n1)
    return p, q

def get_exp(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return n, e

def compute(n):
    spf = spf_sieve(n)
    I = [[], [1], [1]]
    total = 0
    for x in range(3, n + 1):
        p = spf[x]
        t, e = get_exp(x, p)
        if t == 1:
            sols = solve(p, e)
        else:
            sols = []
            for y in I[t]:
                for z in solve(p, e):
                    w = x // t
                    a, b = crt(t, w)
                    v = (y*b*w + z*a*t) % (x)
                    sols.append(v)
            sols = sorted(sols)
        if x <= n//2:
            I.append(sols)
        total += sols[-2]
    return total

if __name__ == "__main__":
    print(compute(2*10**7))
    print("--- %s seconds ---" % (time.time() - start_time))
