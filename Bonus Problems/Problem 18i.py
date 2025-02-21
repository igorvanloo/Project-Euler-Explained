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

Now R(p) in F_p (finite field of dimension p)

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
--- 73.76584506034851 seconds --- Using my  prime sieve
--- 55.798606157302856 seconds --- Using mCodings prime sieve 
'''

import time
from mathslib import tonelli_shanks, prime_sieve_in_range
start_time = time.time()
    
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
        
def compute_tonelli(upp_lim, low_lim):
    primes = prime_sieve_in_range(low_lim, upp_lim)
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
    primes = prime_sieve_in_range(low_lim, upp_lim)
    return sum(R(int(p)) for p in primes)

if __name__ == "__main__":
    print(compute(int(1.1*10**9), 10**9))
    print("--- %s seconds ---" % (time.time() - start_time))
