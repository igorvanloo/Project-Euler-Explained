# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:21:39 2022

@author: igorvanloo
"""
'''
Project Euler Problem 808

Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

We call a number a reversible prime square if:

1. It is not a palindrome, and
2. It is the square of a prime, and
3. Its reverse is also the square of a prime.
169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares.

Anwser:
    3807504276997394
--- 12.020212411880493 seconds ---
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
    
def is_not_palindrome(x):
    if x == x[::-1]:
        return False
    return True

def is_quadratic(x):
    sqrt__root = (x ** (1 / 2))
    if round(sqrt__root) ** 2 == x:
        return True
    return False

def compute(n, limit = 5*10**7):
    is_prime = list_primality(limit)
    primes = [i for (i, isprime) in enumerate(is_prime) if isprime]
    values = []
    for x in primes[4:]:
        sq = str(pow(x, 2))
        if is_not_palindrome(sq):
            rev = int(sq[::-1])
            if is_quadratic(rev):
                if is_prime[int(math.sqrt(rev))]:
                    values.append(int(sq))
                    values.append(rev)
    return sum(sorted(set(values))[:n]), len(sorted(set(values)))

if __name__ == "__main__":
    print(compute(50))
    print("--- %s seconds ---" % (time.time() - start_time))