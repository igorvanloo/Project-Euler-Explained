# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:27:09 2022

@author: igorvanloo
"""
'''
Project Euler Problem 634

F(n) = #x <= n such that x = a^2b^3, a, b > 1
F(100) = 2, F(2 * 10^4) = 130, F(3 * 10^6) = 2014

https://oeis.org/A001694 - 2-powerful numbers are of the form a^2b^3, however a,b can be 1
https://en.wikipedia.org/wiki/Powerful_number

We want all numbers a^2b^3 such that a, b not equal to 1

Suppose x = a^2b^3 is not square, this can be uniquely represented when b >= 2 and is squarefree, and a >= 2

Given that a >= 2, 4b^3 <= n => b <= (n/4)^(1/3)
For a given b, if we ensure that b is squarefree, then a <= sqrt(n/b^3) with the only restriction being a >= 1
Therefore for each squarefree b <= (n/4)^(1/3) we add floor(sqrt(n/b^3)) - 1 to a total

Suppose x is a square, then x = a^2b^6 and a is cubefree is unique, note that if b is prime, then this means a >= 2
For a given b, a <= sqrt(n/b^6) and a has to be cubefree, therefore we count all cubefree numbers less than this
If b is prime then we subtract 1 extra

For some reason I cannot fix the issue of being 1 off

Anwser:
    4019680945 - correct answer is 4019680944
--- 2.4134740829467773 seconds ---
'''
import time, math
start_time = time.time()

def mobius_k_sieve(n, k):
    isprime = [1]*(n + 1)
    isprime[0] = isprime[1] = 0
    mob = [0] + [1]*(n)
    for p in range(2, n + 1):
        if isprime[p]:
            mob[p] *= -1
            for i in range(2*p, n + 1, p):
                isprime[i] = 0
                mob[i] *= -1
            sq = pow(p, k)
            if sq <= n:
                for j in range(sq, n + 1, sq):
                    mob[j] = 0
    return isprime, mob

def count_kfree(n, k):
    '''
    I re-defined the the Mobius function:
                    1 if n is kpower-free positive integer with even number of prime factors
        μ_{k}(n) = -1 if n is kpower-free positive integer with odd number of prime factors
                    0 if n has a k power factor
                    
    Computes the number of integers x <= n such that x is k-free, denote this as S(n)
    We use the fact that S(n) = sum_{d = 1}^n |μ_k(d)| = sum_{d = 1}^{floor{n^(1/k)}} μ_{k}(d)*floor{n/d^k}
    '''
    sq = math.floor(n**(1/k))
    _, mobius_k = mobius_k_sieve(sq, 2)
    return sum([mobius_k[i]*(n//pow(i, k)) for i in range(1, sq + 1)])
    
def F(n):
    isprime, mob = mobius_k_sieve(int(pow(n/4, 1/3)), 2)
    total = 0
    b = 2
    while pow(b, 3)*4 <= n:
        total += pow(mob[b], 2)*(math.floor(math.sqrt(n/pow(b, 3))) - 1)
        b += 1
        
    b = 2
    while pow(b, 6) <= n:
        v = math.floor(math.sqrt(n/pow(b, 6)))
        if isprime[b]:
            total += (count_kfree(v, 3) - 1)
        else:
            total += count_kfree(v, 3)
        b += 1
    
    return total
    
if __name__ == "__main__":
    print(F(9*10**18))
    print("--- %s seconds ---" % (time.time() - start_time))
