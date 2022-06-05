#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:49:26 2022

@author: igorvanloo
"""
'''
Project Euler Problem 304

For any positive integer n the function next_prime(n) returns the smallest prime p
such that p>n.

The sequence a(n) is defined by:
a(1)=next_prime(1014) and a(n)=next_prime(a(n-1)) for n>1.

The fibonacci sequence f(n) is defined by: f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n>1.

The sequence b(n) is defined as f(a(n)).

Find ∑ b(n) for 1≤n≤100 000. Give your answer mod 1234567891011.

Anwser:
    283988410192
--- 45.57677698135376 seconds --- Using fermat primality test
--- 74.50918412208557 seconds --- Using miller test
'''
import time
start_time = time.time()

def miller(n, millerrabin = False, numoftests = 2):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if not millerrabin:
        #Uses https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases 
        #to minimise bases to check, this version relies on the fact that The Riemann Hypothesis is true
        if n < 1373653:
            tests = [2, 3]
        elif n < 9080191:
            tests = [31, 73]
        elif n < 25326001:
            tests = [2, 3, 5]
        elif n < 4759123141:
            tests = [2, 7, 61]
        elif n < 2152302898747:
            tests = [2, 3, 5, 7, 11]
        elif n < 3474749660383:
            tests = [2, 3, 5, 7, 11, 13]
        elif n < 341550071728321:
            tests = [2, 3, 5, 7, 11, 13, 17]
        elif n < 3825123056546413051:
            tests = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        elif n < 318665857834031151167461: # < 2^64
            tests = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        elif n < 3317044064679887385961981:
            tests = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        else:
            tests = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    else:
        #If we want to use miller rabin test it finds random integers in the correct range as bases
        numoftests %= n
        tests = [x for x in range(2, 2 + numoftests)]
    d = n - 1
    r = 0
    while d % 2 == 0:
        #Divide 2 until no longer divisible
        d //= 2
        r += 1
    #n = 2^r*d + 1
    def is_composite(a):
        #Finds out if a number is a composite one
        if pow(a, d, n) == 1:
            return False
        for i in range(r):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True
    for k in tests:
        if is_composite(k):
            return False
    return True

def fermat_primality_test(n, tests):
    for x in range(tests):
        if pow(2*(x + 2), n - 1, n) != 1:
            return False
    return True
    
def next_prime(n):
    x = n + 1
    while True:
        if miller(x):
        #if fermat_primality_test(x, 5):
            return x
        x += 1
    
def fibonnaci_mod(n, mod): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    count = 0
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = pow(v2, 2, mod)
        v1, v2, v3 = (pow(v1, 2, mod)+calc) % mod, ((v1+v3)*v2) % mod, (calc+pow(v3, 2, mod)) % mod
        if rec=='1':
            v1, v2, v3 = v1+v2 % mod, v1 % mod, v2 % mod
        count += 1
    return v2 % mod

def compute(limit):
    mod = 1234567891011
    a1 = next_prime(10**14)
    total = 0
    for x in range(limit):
        total += fibonnaci_mod(a1, mod)
        a1 = next_prime(a1)
    return total % mod

if __name__ == "__main__":
    print(compute(100000))
    print("--- %s seconds ---" % (time.time() - start_time))
