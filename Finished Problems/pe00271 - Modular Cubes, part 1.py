#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:53:34 2022

@author: igorvanloo
"""
'''
Project Euler Problem 271

Notice that 13082761331670030 = 2 * 3 * 5 *... * 43
Therefore we want to find 
x^3 = 1 mod 13082761331670030 by chinese remainder theorem this is equvialent to solving
x^3 = 1 mod 3
x^3 = 1 mod 5
...
x^3 = 1 mod 43

Anwser:
    4617456485273129588
--- 0.004601955413818359 seconds ---
'''
import time
start_time = time.time()

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                factors.append(n)
            break
    return list(set(factors))

def ChineseRemainderTheorem(a1, a2, n1, n2):
    #x = a1 (mod n1)
    #x = a2 (mod n2)
    #We find p = n1^-1 (mod n2), q = n2^-1 (mod n1)
    p ,q = pow(n1, -1, n2), pow(n2, -1, n1)
    #The unique oslution to this system is a1*q*n2 + a2*p*n1 % n1*n2
    return (a1*q*n2+ a2*p*n1) % (n1*n2)

def FindSolutions(p):
    solutions = set()
    for x in range(p):
        if (x*x*x % p) == 1:
            solutions.add(x)
    return solutions
    
def compute(N):
    factors = prime_factors(N)
    curr_solutions = FindSolutions(factors[0])
    curr_N = factors[0]
    for x in range(1, len(factors)):
        p = factors[x]
        sol1 = curr_solutions
        sol2 = FindSolutions(p)
        new_solutions = set()
        for a in sol1:
            for b in sol2:
                new_solutions.add(ChineseRemainderTheorem(a, b, curr_N, p))
        curr_N *= p
        curr_solutions = new_solutions
    return sum(curr_solutions) - 1
    

if __name__ == "__main__":
    print(compute(13082761331670030))
    print("--- %s seconds ---" % (time.time() - start_time))