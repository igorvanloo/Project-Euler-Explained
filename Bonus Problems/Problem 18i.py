# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:19:33 2024

@author: IP176077
"""
'''
Project Euler Bonus Problem 18i

f(x) = x^3 - 3x + 4

R(p) = prod_{x = 0}^{p - 1} f(x) % p

Fix a prime p > 3

Now R(p) \in F_p (finite field of dimension p)

https://math.stackexchange.com/questions/4997555/project-euler-18i-remainder-of-prod-x-0p-1-x3-3x-4-mod-p
https://www.math.clemson.edu/~sgao/papers/GP97a.pdf
https://galois.readthedocs.io/_/downloads/en/latest/pdf/

if f(x) is reducible in F_p, R(p) = 0
Else R(p) = 18i, where i = sqrt(-1), that is find a such that a^2 = 1 (mod p)

Need to find a way to pick the correct a, they can be found with tonelli shanks algorithm.

Answer:

'''

import time, math, galois
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def legendre_symbol(a, p):
    t = pow(a, (p - 1) // 2, p)
    if t == p - 1:
        return -1
    return t

def tonelli_shanks(a, p):
    # Code is taken from: https://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python/
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1
    s = int(s)
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e
    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)
        if m == 0:
            return x
        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

def f(x):
    return x*x*x - 3*x + 4

def R(p):
    prod = 1
    for x in range(p):
        prod *= f(x)
        prod %= p
    return prod

def compute(upp_lim, low_lim = 4):
    primes = list_primes(upp_lim)
    total = 0
    for p in primes:
        if low_lim < p:
            v = R(p)
            if v != 0:
                print("prime: ", p)
                a = tonelli_shanks(-1, p)
                total += v
                if 18*a % p == v:
                    print(a)
                if -18*a % p == v:
                    print(-a % p)
                #print(p, R(p), a, 18*a % p, -18*a % p)

if __name__ == "__main__":
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
