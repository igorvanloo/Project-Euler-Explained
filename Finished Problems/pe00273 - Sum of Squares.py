#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:21:53 2022

@author: igorvanloo
"""
'''
Project Euler Problem 273

Consider equations of the form: a2 + b2 = N, 0 ≤ a ≤ b, a, b and N integer.
For N=65 there are two solutions:
a=1, b=8 and a=4, b=7.
We call S(N) the sum of the values of a of all solutions of a2 + b2 = N, 0 ≤ a ≤ b, a, b and N integer.

Thus S(65) = 1 + 4 = 5.
Find ∑ S(N), for all squarefree N only divisible by primes of the form 4k+1 with 4k+1 < 150

https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares

This says that if p = 4k + 1 iff p = x^2 + y^2 for some x and y

We want N divisble by only primes of this form, and squarefree, therefore we cannot have any factor twice or more
There are only 65534 numbers to check, but they can get very larger

For a given prime p, lets say it has solution (a, b), that is a^2 + b^2 = p
similary q has solution (c, d)

A well known identity is (a^2 + b^2)(c^2 + d^2) = (ac + bd)^2 + (ad - bc)^2
Therefore we know know a solutions to pq (ac + bd, |ad - bc|), (|ac - bd|, ad + bc)

Anwser:
    2032447591196869022
--- 38.90522003173828 seconds ---
'''
import time, math
from itertools import combinations
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

def is_quadratic(x):
    sqrt__root = (x ** (1 / 2))
    if round(sqrt__root) ** 2 == x:
        return True
    return False

def find_sol(p):
    sols = set()
    for x in range(0, int(math.sqrt(p)) + 1):
        t = p - x*x
        if is_quadratic(t):
            sols.add(tuple(sorted((x, int(math.sqrt(t))))))
    return sols

def prod(alist):
    total = 1
    for x in alist:
        total *= x
    return total
    
def compute(limit):
    allowed_primes = [p for p in list_primes(limit) if p % 4 == 1]
    allowed_numbers = [(p,) for p in list_primes(limit) if p % 4 == 1]
    
    array = [0]*(limit + 1) #We have an array such that array[x] = find_sol(x)
    for x in allowed_primes:
        array[x] = find_sol(x)
    for x in range(2, len(allowed_primes) + 1):
        #Now we have all the allowed tuples
        allowed_numbers += list(combinations(allowed_primes, x))
    
    total = 0
    for tup in allowed_numbers:
        temp_total = 0
        current_solutions = array[tup[0]]
        for x in range(1, len(tup)):
            sol1 = current_solutions
            sol2 = array[tup[x]]
            new_solutions = set()
            for p in sol1:
                a, b = p
                for q in sol2:
                    c, d = q
                    new_solutions.add(tuple(sorted((a*c + b*d, abs(a*d - b*c)))))
                    new_solutions.add(tuple(sorted((abs(a*c - b*d), a*d + b*c))))
            current_solutions = new_solutions  
        for x in current_solutions:
            temp_total += min(x)
        total += temp_total
    return total

if __name__ == "__main__":
    print(compute(150))
    print("--- %s seconds ---" % (time.time() - start_time))
