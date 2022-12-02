#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:28:33 2022

@author: igorvanloo
"""

'''
Project Euler Problem 457

f(n) = n^2 - 3n - 1
Let R(p) be the smallest positive integer n such that f(n) mod p^2 = 0 if such an integer n exists, otherwise R(p) = 0.

If we have such a number then n^2 - 3n - 1 = kp^2 => n^2 - 3n - (1 + kp^2) = 0

n = 3 ± √(13 + 4kp^2) / 2

n must be an integer therefore 13 + 4kp^2 = q^2

Notice that 13 + 4kp^2 is odd => q^2 is odd => q is odd, let q = 2x + 1

then we have 13 + 4kp^2 = 4x^2 + 4x + 1 => 4x^2 + 4x - 12 = 4kp^2 => x^2 + x - 3 = kp^2 =>

x^2 + x = 3 (mod p^2) <=> (2x + 1)^2 = 13 (mod p^2)

Note: q^2 = 13 (mod p^2)

By euler's criterion 13^((p-1)/2) = 1 mod p => there is a q such that q^2 = 13 mod p

Therefore using tonelli shanks, I find the smallest q such that q^2 = 13 mod p, if there is one (using legendre symbol)

using hensels lemma to lift it to find q^2 = 13 (mod p^2)

Anwser:
    2647787126797397063
--- 8.520723104476929 seconds ---
'''

import time, math
start_time = time.time()

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2*i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def legendre_symbol(a, p):
    t = pow(a, (p-1)//2, p)
    if t == p - 1:
        return -1
    return t

def tonelli_shanks(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1)//4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1
    s = int(s)
    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1)//2, p)
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

        gs = pow(g, 2**(r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m
        
def R1(p): #brute force
    x = 0
    while True:
        if (x*x + x) % (p*p) == 3:
            break
        x += 1
    
    q = 2*x + 1
    return (3 + q)//2

def R(p):
    d = tonelli_shanks(13, p)
    k = ((13 - d*d)//p) * pow(2*d, -1, p)
    n = (p*k + d) % (p*p)
    inv2 = (p*p - 1)//2
    return min(((n + 3)*inv2) % (p*p), ((p*p - n + 3)*inv2) % (p*p)) + 3

def HenselsLemma(p):
    #New method using new Number Theory Knowledge
    #We are solving x^2 = 13 (mod p^2)
    #Suppose r is a solution to x^2 = 13 (mod p) <=> f(x) = x^2 - 13 = 0 (mod p)
    #We find r by using Tonelli Shanks algorithm to solve x^2 = 13 (mod p)
    r = tonelli_shanks(13, p) #p - r is also a solution
    
    # 1 if f'(r) = 2r ≠ 0 (mod p) then x = r + tp where t = -(f'(r))^-1 * f(r)/p (mod p) is a solution to f(x) = x^2 - 13 = 0 (mod p)
    
    f_prime_r = 2*r
    
    if (f_prime_r % p) != 0:
        t = -(pow(f_prime_r, -1, p) * (r*r - 13)//p) 
        t %= p
        n = (r + t*p) % (p*p) #We know n^2 = 13 (mod p^2) therefore the other solution is (p*p - n)
        
        if n % 2 != 0:
            return (n + 3)//2
        return (p*p - n + 3)//2
    
    # 2 if f'(r) = 0 (mod p):
        
    elif (f_prime_r % p) == 0:
        
        # 2.1 if f(r) = 0 (mod p^2) then x = r + tp, t is an integer modulop is a solution
        
        if (r*r - 13) % (p*p) == 0:
            n = min([(r+t*p) % (p*p) for t in range(0, p)])
            if n % 2 != 0:
                return (n + 3)//2
            return (p*p - n + 3)//2
        
        # 2.2 if f(r) ≠ 0 (mod p^2) then there are no solutions
        return "No solution"
        
def compute(limit):
    primes = list_primes(limit + 1)
    total = 0
    for x in range(1, len(primes)):
        p = primes[x]
        if legendre_symbol(13, p) == 1:
            if p == 3:
                total += 5
            else:
                #print(p, R(p), HenselsLemma(p))
                total += HenselsLemma(p)
    return total
            
if __name__ == "__main__":
    print(compute(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))