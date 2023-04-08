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

Let n = p1^e1 * p2^e2 * ... * pk^ek

Anwser:

'''
import time, math
start_time = time.time()

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
        
def HenselsLemma(p, e):
    #New method using new Number Theory Knowledge
    #We are solving x^2 = 1 (mod p^e)
    #Suppose r is a solution to x^2 = 1 (mod p) <=> f(x) = x^2 - 1 = 0 (mod p)
    #We find r by using Tonelli Shanks algorithm to solve x^2 = 1 (mod p)
    r = p - 1 #p - r is also a solution
    
    # 1 if f'(r) = 2r ≠ 0 (mod p) then x = r + tp^(e - 1) where t = -(f'(r))^-1 * f(r)/p^(e - 1) (mod p) 
    #is a solution to f(x) = x^2 - 1 = 0 (mod p)
    
    f_prime_r = 2*r
    
    if (f_prime_r % p) != 0:
        t = -(pow(f_prime_r, -1, p) * (r*r - 13)//pow(p, e - 1)) 
        t %= p
        n = (r + t*pow(p, e - 1)) % pow(p, e) 
        #We know n^2 = 1 (mod p^e) therefore the other solution is (p^e - n)
        
        return n, pow(p, e) - n
    
    # 2 if f'(r) = 0 (mod p):
        
    elif (f_prime_r % p) == 0:
        
        # 2.1 if f(r) = 0 (mod p^e) then x = r + tp^(e - 1), t is an integer modulo p is a solution
        
        if (r*r - 1) % pow(p, e) == 0:
            n = min([(r+t*pow(p, e - 1)) % pow(p, e) for t in range(0, p)])
            return n, pow(p, e) - n
        
        # 2.2 if f(r) ≠ 0 (mod p^e) then there are no solutions
        return "No solution"

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

def I(n):
    pf = prime_factors(n)
    poss = None
    for p in pf:
        e = pf[p]
        if e == 1:
            # p has exponent 1 in n, then there is no need to use hensels lemma,
            # our solutions are 1 and p - 1
            sol = [x for x in range(1, n, p)]
            sol += [x for x in range(p-1, n, p)]
            sol = set(sol)
            print(p, e, sol)
            if poss == None:
                poss = sol
            else:
                poss = poss.intersection(sol)
        
        else:
            # p has exponent more than 1
            # We solve x^2 = 1 mod p first
            s, s1 = HenselsLemma(p, e)
            sol = [x for x in range(s, n, p)]
            sol += [x for x in range(s1, n, p)]
            sol = set(sol) 
            print(p, e, sol, s, s1)
            if poss == None:
                poss = sol
            else:
                poss = poss.intersection(sol)
    return poss
    
def compute():
    pass

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
