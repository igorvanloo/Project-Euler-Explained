#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:12:41 2022

@author: igorvanloo
"""
'''
Project Euler Problem 272

Brute forcing a lot of values I found that the number of solutions to x^3 = 1 mod n is always of the form 3^k

We consider x^3 - 1 = 0 mod p, where p is a prime, brute force shows that either it has 1 solution or 3, why is this?

https://math.stackexchange.com/questions/2311500/how-many-solutions-are-there-of-the-congruence-x3-%E2%89%A1-1-pmod-p

The group of units mod p, (Z/pZ)*, is isomorphic to C_{p-1} therefore cubing become multiplication by 3

if gcd(3, p-1) = 1 then this means there is only one solution to 3x = 0 mod p, which is x = 0
if 3/(p-1) then we have 3 solutions 0, (p-1)/3, (p-2)/3

therefore if p = 1 mod 3 then x^3 = 1 mod p has 3 solutions, otherwise it has 1

Knowing this, We are looking for n such that x^3 = 1 mod n has 242 = 3^5 - 1 solutions

Ofc the solutions are multiplicative due to chinese remainder theorem, therefore n must have 5 prime factors such that p = 1 mod 3,
unless n is divisble by 9


Anwser:

'''
import time, math
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
    return list(factors.items())

def ChineseRemainderTheorem(a1, a2, n1, n2):
    #x = a1 (mod n1)
    #x = a2 (mod n2)
    #We find p = n1^-1 (mod n2), q = n2^-1 (mod n1)
    p ,q = pow(n1, -1, n2), pow(n2, -1, n1)
    #The unique solution to this system is a1*q*n2 + a2*p*n1 % n1*n2
    return (a1*q*n2+ a2*p*n1) % (n1*n2)

def FindSolutions(p):
    solutions = set()
    for x in range(p):
        if (x*x*x % p) == 1:
            solutions.add(x)
    return solutions
    
def C(N):
    factors = prime_factors(N)
    curr_solutions = FindSolutions(pow(factors[0][0], factors[0][1]))
    curr_N = pow(factors[0][0], factors[0][1])
    
    for x in range(1, len(factors)):
        p = pow(factors[x][0], factors[x][1])
        sol1 = curr_solutions
        sol2 = FindSolutions(p)
        new_solutions = set()
        for a in sol1:
            for b in sol2:
                new_solutions.add(ChineseRemainderTheorem(a, b, curr_N, p))
        curr_N *= p
        curr_solutions = new_solutions
    return sum(curr_solutions) - 1, len(curr_solutions)

def compute(limit):
    prime_limit = int(limit/(7*13*19*3*3))
    primes = list_primes(prime_limit)
    valid_primes = []
    extra_primes = []
    
    for p in primes:
        if p % 3 == 1:
            valid_primes.append(p)
        else:
            extra_primes.append(p)
    print(len(valid_primes))
    
    overall_sol = set()
    for a in range(len(valid_primes)):
        print(a)
        p1 = valid_primes[a]
        for b in range(a + 1, len(valid_primes)):
            p2 = valid_primes[b]
            if p1 * p2 <= limit:
                for c in range(b + 1, len(valid_primes)):
                    p3 = valid_primes[c]
                    if p1 * p2 * p3 <= limit:
                        for d in range(c + 1, len(valid_primes)):
                            p4 = valid_primes[d]
                            x = p1 * p2 * p3 * p4
                            if x <= limit:
                                x1 = 3*3*x
                                if x1 <= limit:
                                    overall_sol.add(x1)
                                    stack = set([x1])
                                    while len(stack) != 0:
                                        s = stack.pop()
                                        for p in primes:
                                            if s * p <= limit:
                                                stack.add(s*p)
                                                overall_sol.add(s * p)
                                    
                                    
                                for e in range(d + 1, len(valid_primes)):
                                    p5 = valid_primes[e]
                                    t = p1 * p2 * p3 * p4 * p5
                                    
                                    if t <= limit:
                                        overall_sol.add(t)
                                        stack = set([t])
                                        while len(stack) != 0:
                                            s = stack.pop()
                                            for p in primes:
                                                if s * p <= limit:
                                                    if C(s * p)[1] != 243:
                                                        
                                                        print(C(s*p), s, p1, p2, p3, p4, p5)
                                                    stack.add(s*p)
                                                    overall_sol.add(s * p)

    return sum(overall_sol), len(overall_sol)

if __name__ == "__main__":
    print(compute(3*10**7))
    print("--- %s seconds ---" % (time.time() - start_time))
