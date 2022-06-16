#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 23:37:35 2021

@author: igorvanloo
"""
'''
Project Euler Problem 407

a^2 ≡ a (mod n) -> a^2 - a = 0 (mod n) -> a(a-1) = 0 (mod n)

That means that a(a - 1) is a multiple of n.
Therefore if x is a divisor of n, then either a or a-1 is a multiple of x, or equivalently

a = 0 mod x or a = 1 mod x, and therefore with another divisors n/x we have the opposite a = 0 mod n/x or a = 1 mod n/x

I noticed that if one divisor is a multiple of another then the CRT is unsolvable, furthermore I notice that if the 2 divisors
are not co-prime then the CRT is unsolvable 

Why is this the case?

Clearly if gcd(m_1, m_2) = 1 and m_1 * m_2 = n => a = 0 mod m_1 and a = 1 mod m_2

We need to prove the converse

a = 0 mod m_1 and a = 1 mod m_2, then CRT requires gcd(m_1, m_2) = 1 because of bezouts identity to form a solution!

Anwser:
    39782849136421
--- 351.45206117630005 seconds ---
'''

import time, math
start_time = time.time()

def divisor_sieve(limit):
    array = [0] + [[(1, x)] for x in range(1, limit + 1)]
    for x in range(2, int(math.sqrt(limit)) + 1):
        for n in range(x*x, len(array), x):
            if math.gcd(n//x, x) == 1:
                array[n].append((x, n//x))
    return array
    
def Divisors_of(x):  # Find the divisors of a number
    divisors = [(1, x)]
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if math.gcd(x//i, i) == 1:
                divisors.append((i, x//i))
    return divisors

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                if d in factors:
                    factors[n] += 1
                else:
                    factors[n] = 1
            break
    return factors

def ChineseRemainderTheorem(a1, a2, n1, n2):
    if a1 > n1 or a2 > n2:
        return "Wrong values were input"
    #x = a1 (mod n1)
    #x = a2 (mod n2)
    #We find p = n1^-1 (mod n2), q = n2^-1 (mod n1)
    #try:
    p, q = pow(n1, -1, n2), pow(n2, -1, n1)
    #except ValueError:
    #   return -1
    #The unique solution to this system is a1*q*n2 + a2*p*n1 % n1*n2
    return (a1*q*n2+ a2*p*n1) % (n1*n2)

def M(n, divisors):
    curr_max = 0
    #divisors = Divisors_of(n)
    for (a, b) in divisors:
        t = max(ChineseRemainderTheorem(0, 1, a, b), ChineseRemainderTheorem(1, 0, a, b))
        if t > curr_max:
            curr_max = t
    return curr_max
        
def compute(limit):
    total = 0
    divisors = divisor_sieve(limit)
    print("Sieve done")
    for n in range(limit, 0, -1):
        if n % 100000 == 0:
            print(n)
        total += M(n, divisors.pop(-1))
    return total
    
if __name__ == "__main__":
    print(compute(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))