# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:19:33 2024

@author: Igor Van Loo
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

R(p)^2 = -324

Note that for a^2 = -1 (mod p) to exist we require p = 1 (mod 4)

Answer:
    842507000531275
--- 457.4489896297455 seconds --- Using my  prime sieve
--- 65.27984952926636 seconds --- Using mCodings prime sieve
--- 55.798606157302856 seconds --- Using ModExp for both cases 
'''

import time, math
from prime_sieve.array import PrimeArraySieve
start_time = time.time()

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

def bin_exp(a, b, c, n, m = None):
    if m == None:
        a_res, b_res = a, b
        for bit in bin(n)[3:]:
            a_res, b_res = (a_res*a_res + c*b_res*b_res), 2*a_res*b_res
            if bit == "1":
                a_res, b_res = (a*a_res + b*c*b_res), (b*a_res + a*b_res)
    else:
        a_res, b_res = a, b
        for bit in bin(n)[3:]:
            a_res, b_res = (a_res*a_res + c*b_res*b_res) % m, 2*a_res*b_res % m
            if bit == "1":
                a_res, b_res = (a*a_res + b*c*b_res) % m, (b*a_res + a*b_res) % m
    return a_res, b_res

def R(p):
    if p % 12 == 1:
        v = bin_exp(-2, 1, 3, (p - 1)//3, p)
        if v[1] == 0:
            return 0

        Rp = -18*v[1]*(1 - 2*v[0]) % p
        return Rp
    
    if p % 12 == 5:
        v = bin_exp(-2, 1, 3, (p + 1)//3, p)
        if v[1] == 0:
            return 0

        Rp = 18*v[1]*(1 - 2*v[0]) % p
        return Rp
    return 0

def prime_sieve(limit, segment = False, values = True):
    if (type(limit) != int) or (type(segment) != bool) or (type(values) != bool):
        return "n must be an integer"
    
    if segment:
        primes = []
        sqrtN = int(math.sqrt(limit))
        result = [True]*(sqrtN + 2)
        result[0] = result[1] = False
        for i in range(2, sqrtN + 1):
            if result[i]:
                primes.append(i)
                for j in range(2*i, sqrtN + 1, i):
                    result[j] = False
        all_primes = []
        marker = [0]*len(primes)
        block_size = sqrtN
        for k in range(1, limit//block_size):
            block_start = k*block_size + 1
            block_end = (k + 1)*block_size
            curr_result = [True]*block_size
            if k == 1:
                for p_index, p in enumerate(primes):
                    count = 0
                    while (block_start + count) % p != 0:
                        count += 1
                    for j in range(block_start + count, block_end + 1, p):
                        curr_result[j - block_start] = False
                        marker[p_index] = j
            else:
                for p_index, p in enumerate(primes):
                    for j in range(marker[p_index] + p, block_end + 1, p):
                        curr_result[j - block_start] = False
                        marker[p_index] = j
            if values:
                all_primes += [block_start + i for (i, isprime) in enumerate(curr_result) if isprime]
            else:
                all_primes = all_primes[:block_start + 1] + curr_result
        if values:
            return primes + all_primes
        else:
            return result[:sqrtN + 1] + all_primes
    else:
       	result = [True] * (limit + 1)
       	result[0] = result[1] = False
       	for i in range(int(math.sqrt(limit)) + 1):
       		if result[i]:
       			for j in range(2 * i, len(result), i):
       				result[j] = False
        if values:
            return [i for (i, isprime) in enumerate(result) if isprime]
        else:
            return result
        
def compute_tonelli(upp_lim, low_lim):
    sieve = PrimeArraySieve()
    primes = sieve.primes_in_range(low_lim, upp_lim)
    total = 0
    for p in primes:
        p =  int(p)
        if p % 12 == 1:
            s = tonelli_shanks(3, p)
            z = pow(-2 + s, (p - 1)//3, p)
            Rp = -6*s*z*(1 - z) % p
            total += Rp
        if p % 12 == 5:
            v = bin_exp(-2, 1, 3, (p + 1)//3, p)
            if v[1] != 0:
                Rp = 18*v[1]*(1 - 2*v[0]) % p
                total += Rp
    return total

def compute(upp_lim, low_lim):
    sieve = PrimeArraySieve()
    primes = sieve.primes_in_range(low_lim, upp_lim)
    return sum(R(int(p)) for p in primes)

if __name__ == "__main__":
    print(compute(1.1*10**9,10**9))
    print("--- %s seconds ---" % (time.time() - start_time))
